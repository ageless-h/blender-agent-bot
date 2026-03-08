from __future__ import annotations

import ast
import json
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import typer
import yaml
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

from .runtime import ensure_runtime

VARIABLE_PATTERN = re.compile(r"{{\s*([\w.]+)\s*}}")


@dataclass(slots=True)
class StepReport:
    step: str
    tool: str
    status: str
    attempts: int
    duration_ms: int
    detail: dict[str, Any]


class BatchExecutionError(RuntimeError):
    """批处理执行异常。"""


def run_script_command(
    ctx: typer.Context,
    script_path: Path = typer.Argument(
        ..., exists=True, dir_okay=False, readable=True, help="YAML 脚本路径"
    ),
    dry_run: bool = typer.Option(False, "--dry-run", help="仅解析并输出执行计划"),
    output: str = typer.Option("text", "--output", "-o", help="报告格式: text/json"),
    report_file: Path | None = typer.Option(
        None, "--report-file", help="将报告写入文件"
    ),
    stop_on_error: bool = typer.Option(
        False, "--stop-on-error", help="任一步骤失败后立即终止"
    ),
) -> None:
    runtime = ensure_runtime(ctx)
    script = _load_script(script_path)
    variables = _extract_variables(script)
    steps = _extract_steps(script)
    reports: list[StepReport] = []

    estimated_total = _estimate_total_steps(steps, variables)

    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
            console=runtime.console,
        ) as progress:
            task_id = progress.add_task("执行批处理脚本", total=estimated_total)
            for index, step in enumerate(steps, start=1):
                step_name = str(step.get("name") or step.get("id") or f"step-{index}")
                iterations = _expand_step_iterations(step, variables)

                for iter_context, transient_keys in iterations:
                    progress.update(task_id, description=f"执行 {step_name}")
                    report = _execute_step(
                        runtime=runtime,
                        step_name=step_name,
                        step=step,
                        variables=iter_context,
                        dry_run=dry_run,
                    )
                    reports.append(report)
                    progress.advance(task_id)

                    for key, value in iter_context.items():
                        if key in transient_keys:
                            continue
                        variables[key] = value

                    if report.status != "success":
                        policy = str(step.get("on_error", "stop")).lower()
                        if stop_on_error or policy == "stop":
                            raise BatchExecutionError(f"步骤失败: {step_name}")
    except BatchExecutionError as exc:
        runtime.console.print(f"[red]批处理失败:[/red] {exc}")
        _render_report(runtime=runtime, output=output, reports=reports)
        _write_report_if_needed(output=output, report_file=report_file, reports=reports)
        raise typer.Exit(code=1) from exc

    _render_report(runtime=runtime, output=output, reports=reports)
    _write_report_if_needed(output=output, report_file=report_file, reports=reports)


def _load_script(script_path: Path) -> dict[str, Any]:
    payload = yaml.safe_load(script_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise typer.BadParameter("脚本格式错误：顶层必须是对象")
    return payload


def _extract_variables(script: dict[str, Any]) -> dict[str, Any]:
    raw = script.get("vars", script.get("variables", {}))
    if raw is None:
        return {}
    if not isinstance(raw, dict):
        raise typer.BadParameter("vars/variables 必须是对象")
    return dict(raw)


def _extract_steps(script: dict[str, Any]) -> list[dict[str, Any]]:
    raw_steps = script.get("steps")
    if not isinstance(raw_steps, list):
        raise typer.BadParameter("steps 必须是数组")
    parsed = [step for step in raw_steps if isinstance(step, dict)]
    if len(parsed) != len(raw_steps):
        raise typer.BadParameter("steps 中每一项都必须是对象")
    return parsed


def _estimate_total_steps(
    steps: list[dict[str, Any]], variables: dict[str, Any]
) -> int:
    total = 0
    for step in steps:
        total += max(1, len(_expand_step_iterations(step, variables)))
    return total


def _expand_step_iterations(
    step: dict[str, Any], variables: dict[str, Any]
) -> list[tuple[dict[str, Any], set[str]]]:
    loop_config = step.get("for", step.get("loop"))
    if loop_config is None:
        return [(dict(variables), set())]

    if isinstance(loop_config, dict):
        var_name = str(loop_config.get("var", "item"))
        source = loop_config.get("in", [])
    else:
        var_name = "item"
        source = loop_config

    resolved = _resolve_templates(source, variables)
    if not isinstance(resolved, list):
        raise typer.BadParameter("loop/for 的输入必须解析为列表")

    contexts: list[tuple[dict[str, Any], set[str]]] = []
    for index, item in enumerate(resolved):
        iter_context = dict(variables)
        iter_context[var_name] = item
        iter_context[f"{var_name}_index"] = index
        contexts.append((iter_context, {var_name, f"{var_name}_index"}))
    return contexts


def _execute_step(
    runtime: Any,
    step_name: str,
    step: dict[str, Any],
    variables: dict[str, Any],
    dry_run: bool,
) -> StepReport:
    condition = step.get("if")
    if condition is not None and not _evaluate_condition(condition, variables):
        return StepReport(
            step=step_name,
            tool=str(step.get("tool", "")),
            status="skipped",
            attempts=0,
            duration_ms=0,
            detail={"reason": "condition=false"},
        )

    tool_name = str(_resolve_templates(step.get("tool", ""), variables)).strip()
    if not tool_name:
        raise BatchExecutionError(f"步骤 {step_name} 缺少 tool")

    args = _resolve_templates(step.get("args", {}), variables)
    if not isinstance(args, dict):
        raise BatchExecutionError(f"步骤 {step_name} 的 args 必须是对象")

    retry_count = int(step.get("retry", 0))
    on_error = str(step.get("on_error", "stop")).lower()
    if on_error == "retry" and retry_count == 0:
        retry_count = 1

    attempts = 0
    started = time.perf_counter()
    while attempts <= retry_count:
        attempts += 1
        try:
            if dry_run:
                result = {
                    "dry_run": True,
                    "tool": tool_name,
                    "args": args,
                }
            else:
                result = runtime.backend.call_tool(tool_name, args)

            _save_step_outputs(step=step, variables=variables, result=result)
            duration = int((time.perf_counter() - started) * 1000)
            return StepReport(
                step=step_name,
                tool=tool_name,
                status="success",
                attempts=attempts,
                duration_ms=duration,
                detail=result if isinstance(result, dict) else {"result": result},
            )
        except Exception as exc:  # noqa: BLE001
            if attempts <= retry_count:
                continue

            duration = int((time.perf_counter() - started) * 1000)
            status = "failed"
            if on_error in {"continue", "retry"}:
                status = "error_ignored"

            return StepReport(
                step=step_name,
                tool=tool_name,
                status=status,
                attempts=attempts,
                duration_ms=duration,
                detail={"error": str(exc), "args": args},
            )

    raise BatchExecutionError(f"步骤 {step_name} 执行异常")


def _save_step_outputs(
    step: dict[str, Any], variables: dict[str, Any], result: dict[str, Any]
) -> None:
    save_as = step.get("save_as")
    if isinstance(save_as, str) and save_as:
        variables[save_as] = result

    assignments = step.get("set", {})
    if isinstance(assignments, dict):
        for key, value in assignments.items():
            variables[str(key)] = _resolve_templates(value, variables)


def _evaluate_condition(condition: Any, variables: dict[str, Any]) -> bool:
    if isinstance(condition, bool):
        return condition
    if not isinstance(condition, str):
        return bool(condition)

    expression = condition.strip()
    expression = VARIABLE_PATTERN.sub(
        lambda match: repr(_lookup_variable(match.group(1), variables)), expression
    )
    lowered = expression.lower()
    if lowered in {"true", "false"}:
        return lowered == "true"

    _validate_safe_expression(expression)
    return bool(eval(expression, {"__builtins__": {}}, dict(variables)))  # noqa: S307


def _validate_safe_expression(expression: str) -> None:
    tree = ast.parse(expression, mode="eval")
    allowed_nodes = (
        ast.Expression,
        ast.BoolOp,
        ast.Compare,
        ast.Name,
        ast.Load,
        ast.Constant,
        ast.UnaryOp,
        ast.BinOp,
        ast.And,
        ast.Or,
        ast.Not,
        ast.Eq,
        ast.NotEq,
        ast.Gt,
        ast.GtE,
        ast.Lt,
        ast.LtE,
        ast.In,
        ast.NotIn,
        ast.Add,
        ast.Sub,
        ast.Mult,
        ast.Div,
        ast.Mod,
        ast.USub,
        ast.List,
        ast.Tuple,
        ast.Dict,
        ast.Subscript,
        ast.Index,
        ast.Slice,
    )
    for node in ast.walk(tree):
        if not isinstance(node, allowed_nodes):
            raise BatchExecutionError(f"条件表达式不安全: {expression}")


def _resolve_templates(value: Any, variables: dict[str, Any]) -> Any:
    if isinstance(value, str):
        matches = VARIABLE_PATTERN.findall(value)
        if not matches:
            return value
        if (
            value.strip().startswith("{{")
            and value.strip().endswith("}}")
            and len(matches) == 1
        ):
            return _lookup_variable(matches[0], variables)

        return VARIABLE_PATTERN.sub(
            lambda match: str(_lookup_variable(match.group(1), variables)), value
        )

    if isinstance(value, list):
        return [_resolve_templates(item, variables) for item in value]

    if isinstance(value, dict):
        return {
            str(key): _resolve_templates(item, variables) for key, item in value.items()
        }

    return value


def _lookup_variable(path: str, variables: dict[str, Any]) -> Any:
    current: Any = variables
    for segment in path.split("."):
        if isinstance(current, dict) and segment in current:
            current = current[segment]
        else:
            raise BatchExecutionError(f"变量不存在: {path}")
    return current


def _render_report(runtime: Any, output: str, reports: list[StepReport]) -> None:
    normalized = output.lower()
    payload = [
        {
            "step": report.step,
            "tool": report.tool,
            "status": report.status,
            "attempts": report.attempts,
            "duration_ms": report.duration_ms,
            "detail": report.detail,
        }
        for report in reports
    ]

    if normalized == "json":
        runtime.console.print_json(data=payload)
        return

    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("Step")
    table.add_column("Tool")
    table.add_column("Status")
    table.add_column("Attempts")
    table.add_column("Duration(ms)")
    table.add_column("Detail", overflow="fold")

    for report in reports:
        table.add_row(
            report.step,
            report.tool,
            report.status,
            str(report.attempts),
            str(report.duration_ms),
            json.dumps(report.detail, ensure_ascii=False),
        )

    runtime.console.print(table)


def _write_report_if_needed(
    output: str, report_file: Path | None, reports: list[StepReport]
) -> None:
    if report_file is None:
        return

    payload = [
        {
            "step": report.step,
            "tool": report.tool,
            "status": report.status,
            "attempts": report.attempts,
            "duration_ms": report.duration_ms,
            "detail": report.detail,
        }
        for report in reports
    ]

    report_file.parent.mkdir(parents=True, exist_ok=True)
    if output.lower() == "json":
        report_file.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        return

    lines = [
        (
            f"{row['step']} | {row['tool']} | {row['status']} | "
            f"attempts={row['attempts']} | duration={row['duration_ms']}ms"
        )
        for row in payload
    ]
    report_file.write_text("\n".join(lines), encoding="utf-8")
