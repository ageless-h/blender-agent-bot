from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import typer

from .runtime import ensure_runtime, render_data


def tools_command(
    ctx: typer.Context,
    tool_name: str | None = typer.Argument(None, help="工具名"),
    tool_args: str | None = typer.Argument(None, help="工具参数(JSON 字符串，可选)"),
    list_tools: bool = typer.Option(False, "--list", help="列出全部工具"),
    info: str | None = typer.Option(None, "--info", help="查看指定工具详情"),
    args: str | None = typer.Option(None, "--args", help="JSON 参数字符串"),
    args_file: Path | None = typer.Option(None, "--args-file", help="JSON 参数文件"),
    output: str = typer.Option("json", "--output", help="输出格式: json/table/tree"),
) -> None:
    runtime = ensure_runtime(ctx)

    if output.lower() not in {"json", "table", "tree"}:
        raise typer.BadParameter("--output 仅支持 json/table/tree")

    if list_tools or (tool_name is None and info is None):
        tools_payload = [tool.as_dict() for tool in runtime.backend.list_tools()]
        render_data(runtime.console, tools_payload, output=output)
        return

    if info is not None:
        details = runtime.backend.get_tool_info(info)
        if details is None:
            raise typer.BadParameter(f"未知工具: {info}")
        render_data(runtime.console, details.as_dict(), output=output)
        return

    if tool_name is None:
        raise typer.BadParameter("请提供工具名，或使用 --list/--info")

    parsed_args = _parse_args(args=args, tool_args=tool_args, args_file=args_file)
    result = runtime.backend.call_tool(tool_name, parsed_args)
    render_data(runtime.console, result, output=output)


def _parse_args(args: str | None, tool_args: str | None, args_file: Path | None) -> dict[str, Any]:
    if args_file is not None:
        raw = args_file.expanduser().read_text(encoding="utf-8")
    elif args is not None:
        raw = args
    elif tool_args is not None:
        raw = tool_args
    else:
        raw = "{}"

    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise typer.BadParameter(f"参数 JSON 解析失败: {exc}") from exc

    if not isinstance(parsed, dict):
        raise typer.BadParameter("工具参数必须是 JSON 对象")
    return parsed
