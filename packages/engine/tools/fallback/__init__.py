from __future__ import annotations

from typing import Any

from ...executor.sandbox import SandboxExecutor
from ...protocol import SafetyLevel, ToolResult
from ..runtime import failure, require_bpy, success
from ..spec import ToolDefinition


def execute_script(arguments: dict[str, Any]) -> ToolResult:
    tool_name = "execute_script"
    try:
        script = str(arguments.get("script", "")).strip()
        if not script:
            raise ValueError("script is required")

        timeout = float(arguments.get("timeout", 2.0))
        executor = SandboxExecutor(timeout_seconds=max(timeout, 0.1))
        result = executor.execute(script)
        return ToolResult(
            tool_name=tool_name,
            success=result.success,
            data=result.data,
            error=result.error,
        )
    except Exception as exc:
        return failure(tool_name, exc)


def execute_operator(arguments: dict[str, Any]) -> ToolResult:
    tool_name = "execute_operator"
    try:
        bpy = require_bpy(tool_name)
        operator_id = str(arguments.get("operator_id", "")).strip()
        kwargs = dict(arguments.get("kwargs", {}))
        if not operator_id:
            raise ValueError("operator_id is required, e.g. object.select_all")

        parts = operator_id.split(".", 1)
        if len(parts) != 2:
            raise ValueError("operator_id must be in format 'category.name'")
        category, name = parts[0], parts[1]

        category_ops = getattr(bpy.ops, category, None)
        if category_ops is None:
            raise ValueError(f"operator category not found: {category}")
        operator = getattr(category_ops, name, None)
        if operator is None:
            raise ValueError(f"operator not found: {operator_id}")

        result = operator(**kwargs)
        return success(tool_name, {"operator_id": operator_id, "result": str(result)})
    except Exception as exc:
        return failure(tool_name, exc)


def import_export(arguments: dict[str, Any]) -> ToolResult:
    tool_name = "import_export"
    try:
        bpy = require_bpy(tool_name)
        action = str(arguments.get("action", "")).strip().lower()
        format_name = str(arguments.get("format", "")).strip().lower()
        filepath = str(arguments.get("filepath", "")).strip()

        if not action or not format_name or not filepath:
            raise ValueError("action, format and filepath are required")

        used_operator = ""

        def resolve_operator(operator_id: str) -> Any | None:
            parts = operator_id.split(".", 1)
            if len(parts) != 2:
                return None
            category, name = parts
            category_ops = getattr(bpy.ops, category, None)
            if category_ops is None:
                return None
            return getattr(category_ops, name, None)

        def call_compatible(candidates: list[str]) -> Any:
            nonlocal used_operator
            for candidate in candidates:
                operator = resolve_operator(candidate)
                if operator is None:
                    continue
                used_operator = candidate
                return operator(filepath=filepath)
            raise ValueError(f"no compatible operator available: {', '.join(candidates)}")

        if action == "import":
            if format_name == "obj":
                result = call_compatible(["wm.obj_import", "import_scene.obj"])
            elif format_name == "fbx":
                result = call_compatible(["import_scene.fbx"])
            elif format_name in {"glb", "gltf"}:
                result = call_compatible(["import_scene.gltf"])
            elif format_name == "blend":
                used_operator = "wm.open_mainfile"
                result = bpy.ops.wm.open_mainfile(filepath=filepath)
            else:
                raise ValueError(f"unsupported import format: {format_name}")
        elif action == "export":
            if format_name == "obj":
                result = call_compatible(["wm.obj_export", "export_scene.obj"])
            elif format_name == "fbx":
                result = call_compatible(["export_scene.fbx"])
            elif format_name in {"glb", "gltf"}:
                result = call_compatible(["export_scene.gltf"])
            elif format_name == "blend":
                used_operator = "wm.save_as_mainfile"
                result = bpy.ops.wm.save_as_mainfile(filepath=filepath)
            else:
                raise ValueError(f"unsupported export format: {format_name}")
        else:
            raise ValueError("action must be import or export")

        return success(
            tool_name,
            {
                "action": action,
                "format": format_name,
                "filepath": filepath,
                "operator_id": used_operator,
                "result": str(result),
            },
        )
    except Exception as exc:
        return failure(tool_name, exc)


def get_tool_definitions() -> list[ToolDefinition]:
    return [
        ToolDefinition("execute_script", "执行任意Python脚本", SafetyLevel.LEVEL_3, "fallback", execute_script),
        ToolDefinition("execute_operator", "调用bpy.ops操作符", SafetyLevel.LEVEL_3, "fallback", execute_operator),
        ToolDefinition("import_export", "导入导出文件", SafetyLevel.LEVEL_3, "fallback", import_export),
    ]


__all__ = ["get_tool_definitions"]
