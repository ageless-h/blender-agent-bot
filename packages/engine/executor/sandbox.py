from __future__ import annotations

import ast
import traceback
from dataclasses import asdict, dataclass
from multiprocessing import get_context
from queue import Empty
from typing import Any

_SAFE_BUILTINS: dict[str, Any] = {
    "abs": abs,
    "all": all,
    "any": any,
    "bool": bool,
    "dict": dict,
    "enumerate": enumerate,
    "float": float,
    "int": int,
    "len": len,
    "list": list,
    "max": max,
    "min": min,
    "pow": pow,
    "range": range,
    "round": round,
    "set": set,
    "str": str,
    "sum": sum,
    "tuple": tuple,
    "zip": zip,
}
_STARTUP_GRACE_SECONDS = 0.5


@dataclass(slots=True)
class SandboxViolation:
    rule: str
    line: int
    col: int
    detail: str


@dataclass(slots=True)
class SandboxExecutionResult:
    success: bool
    data: dict[str, Any]
    error: str | None = None


@dataclass(slots=True)
class SandboxPolicy:
    blocked_modules: tuple[str, ...] = ("os", "subprocess", "socket", "shutil", "pathlib", "requests", "urllib")
    blocked_calls: tuple[str, ...] = (
        "eval",
        "exec",
        "compile",
        "open",
        "input",
        "__import__",
        "os.system",
        "os.remove",
        "os.rmdir",
        "os.unlink",
        "subprocess.run",
        "subprocess.Popen",
    )


def _attr_chain(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        base = _attr_chain(node.value)
        if base:
            return f"{base}.{node.attr}"
        return node.attr
    return ""


def _run_script_in_worker(script: str, queue: Any) -> None:
    safe_globals: dict[str, Any] = {"__builtins__": _SAFE_BUILTINS}
    safe_locals: dict[str, Any] = {}

    try:
        compiled = compile(script, "<sandbox>", "exec")
        exec(compiled, safe_globals, safe_locals)
        safe_outputs = {
            key: value
            for key, value in safe_locals.items()
            if not key.startswith("_")
            and isinstance(value, (str, int, float, bool, list, tuple, dict, set, type(None)))
        }
        queue.put({"success": True, "data": {"locals": safe_outputs}})
    except Exception as exc:
        queue.put(
            {
                "success": False,
                "data": {},
                "error": f"{exc.__class__.__name__}: {exc}",
                "traceback": traceback.format_exc(),
            }
        )


class SandboxExecutor:
    def __init__(self, timeout_seconds: float = 2.0, policy: SandboxPolicy | None = None) -> None:
        self.timeout_seconds = max(timeout_seconds, 0.1)
        self.policy = policy or SandboxPolicy()

    def validate(self, script: str) -> list[SandboxViolation]:
        tree = ast.parse(script)
        violations: list[SandboxViolation] = []

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    module_name = alias.name.split(".")[0]
                    if module_name in self.policy.blocked_modules:
                        violations.append(
                            SandboxViolation(
                                rule="blocked_module",
                                line=node.lineno,
                                col=node.col_offset,
                                detail=f"import of module '{alias.name}' is not allowed",
                            )
                        )
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    module_name = node.module.split(".")[0]
                    if module_name in self.policy.blocked_modules:
                        violations.append(
                            SandboxViolation(
                                rule="blocked_module",
                                line=node.lineno,
                                col=node.col_offset,
                                detail=f"import from module '{node.module}' is not allowed",
                            )
                        )
            elif isinstance(node, ast.Call):
                call_name = _attr_chain(node.func)
                if call_name in self.policy.blocked_calls:
                    violations.append(
                        SandboxViolation(
                            rule="blocked_call",
                            line=node.lineno,
                            col=node.col_offset,
                            detail=f"call '{call_name}' is not allowed",
                        )
                    )

        return violations

    def execute(self, script: str) -> SandboxExecutionResult:
        violations = self.validate(script)
        if violations:
            formatted = "; ".join(f"{item.rule}@{item.line}:{item.col} {item.detail}" for item in violations)
            return SandboxExecutionResult(
                success=False, data={"violations": [asdict(item) for item in violations]}, error=formatted
            )

        context = get_context("spawn")
        queue = context.Queue(maxsize=1)
        worker = context.Process(target=_run_script_in_worker, args=(script, queue), daemon=True)
        worker.start()
        worker.join(self.timeout_seconds + _STARTUP_GRACE_SECONDS)

        if worker.is_alive():
            worker.terminate()
            worker.join(0.2)
            return SandboxExecutionResult(success=False, data={}, error="script execution timed out")

        try:
            result = queue.get_nowait()
        except Empty:
            return SandboxExecutionResult(success=False, data={}, error="sandbox worker returned no result")

        success = bool(result.get("success", False))
        data = dict(result.get("data", {}))
        error = result.get("error")
        if "traceback" in result:
            data["traceback"] = result["traceback"]

        return SandboxExecutionResult(success=success, data=data, error=error)
