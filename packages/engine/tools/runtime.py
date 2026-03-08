from __future__ import annotations

from typing import Any

from ..protocol import ToolResult


def get_bpy() -> Any | None:
    try:
        import bpy  # type: ignore

        return bpy
    except Exception:
        return None


def require_bpy(tool_name: str) -> Any:
    bpy = get_bpy()
    if bpy is None:
        raise RuntimeError(f"{tool_name} requires Blender runtime (bpy)")
    return bpy


def success(tool_name: str, data: dict[str, Any], message: str | None = None) -> ToolResult:
    payload = dict(data)
    if message:
        payload.setdefault("message", message)
    return ToolResult(tool_name=tool_name, success=True, data=payload)


def failure(tool_name: str, error: Exception | str) -> ToolResult:
    message = str(error)
    return ToolResult(tool_name=tool_name, success=False, error=message)
