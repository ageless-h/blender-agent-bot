from __future__ import annotations

import ast
from dataclasses import dataclass, field


@dataclass(slots=True)
class ASTViolation:
    kind: str
    detail: str
    lineno: int
    col_offset: int
    severity: str


@dataclass(slots=True)
class ASTAnalysis:
    level: str
    violations: list[ASTViolation] = field(default_factory=list)
    summary: str = ""


class ASTAnalyzer:
    """针对生成代码进行静态风险分析。"""

    FORBIDDEN_IMPORTS = {
        "subprocess": "critical",
        "socket": "critical",
        "requests": "critical",
        "httpx": "critical",
        "urllib": "high",
        "ftplib": "critical",
    }

    FORBIDDEN_CALLS = {
        "os.system": "critical",
        "os.popen": "critical",
        "subprocess.run": "critical",
        "subprocess.Popen": "critical",
        "subprocess.call": "critical",
        "eval": "critical",
        "exec": "critical",
        "compile": "high",
        "open": "medium",
    }

    DELETE_CALLS = {
        "os.remove": "critical",
        "os.unlink": "critical",
        "os.rmdir": "critical",
        "shutil.rmtree": "critical",
        "pathlib.Path.unlink": "critical",
    }

    def analyze(self, source_code: str) -> ASTAnalysis:
        try:
            tree = ast.parse(source_code)
        except SyntaxError as error:
            return ASTAnalysis(
                level="high",
                violations=[
                    ASTViolation(
                        kind="syntax_error",
                        detail=str(error),
                        lineno=error.lineno or 0,
                        col_offset=error.offset or 0,
                        severity="high",
                    )
                ],
                summary="代码语法错误，已阻断执行",
            )

        violations: list[ASTViolation] = []
        imported_aliases: dict[str, str] = {}

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imported_aliases[alias.asname or alias.name] = alias.name
                    severity = self.FORBIDDEN_IMPORTS.get(alias.name.split(".")[0])
                    if severity:
                        violations.append(
                            ASTViolation(
                                kind="forbidden_import",
                                detail=f"禁止导入模块: {alias.name}",
                                lineno=node.lineno,
                                col_offset=node.col_offset,
                                severity=severity,
                            )
                        )

            if isinstance(node, ast.ImportFrom):
                module = node.module or ""
                if module:
                    imported_aliases[module.split(".")[-1]] = module
                severity = self.FORBIDDEN_IMPORTS.get(module.split(".")[0])
                if severity:
                    violations.append(
                        ASTViolation(
                            kind="forbidden_import",
                            detail=f"禁止导入模块: {module}",
                            lineno=node.lineno,
                            col_offset=node.col_offset,
                            severity=severity,
                        )
                    )

            if isinstance(node, ast.Call):
                full_name = self._resolve_call_name(node.func)
                resolved_name = self._expand_alias(full_name, imported_aliases)
                severity = self.FORBIDDEN_CALLS.get(resolved_name)
                if severity is None:
                    severity = self.DELETE_CALLS.get(resolved_name)

                if severity:
                    violations.append(
                        ASTViolation(
                            kind="forbidden_call",
                            detail=f"危险调用: {resolved_name}",
                            lineno=node.lineno,
                            col_offset=node.col_offset,
                            severity=severity,
                        )
                    )

        level = self._summarize_level(violations)
        summary = self._build_summary(level, violations)
        return ASTAnalysis(level=level, violations=violations, summary=summary)

    def _resolve_call_name(self, node: ast.AST) -> str:
        if isinstance(node, ast.Name):
            return node.id
        if isinstance(node, ast.Attribute):
            parent = self._resolve_call_name(node.value)
            return f"{parent}.{node.attr}" if parent else node.attr
        return ""

    def _expand_alias(self, full_name: str, aliases: dict[str, str]) -> str:
        if "." not in full_name:
            return aliases.get(full_name, full_name)
        head, tail = full_name.split(".", 1)
        mapped = aliases.get(head)
        if mapped:
            return f"{mapped}.{tail}"
        return full_name

    def _summarize_level(self, violations: list[ASTViolation]) -> str:
        if not violations:
            return "safe"
        severities = {violation.severity for violation in violations}
        if "critical" in severities:
            return "critical"
        if "high" in severities:
            return "high"
        if "medium" in severities:
            return "medium"
        return "low"

    def _build_summary(self, level: str, violations: list[ASTViolation]) -> str:
        if not violations:
            return "未发现危险调用"
        return f"检测到 {len(violations)} 个风险点，安全等级={level}"
