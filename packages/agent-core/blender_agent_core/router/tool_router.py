from __future__ import annotations

from typing import Any, Mapping

from shared.protocol import EngineRequest, EngineRequestType

DEFAULT_TOOL_MAPPING: dict[str, str] = {
    "get_objects": "blender.get_objects",
    "get_object_data": "blender.get_object_data",
    "get_node_tree": "blender.get_node_tree",
    "get_animation_data": "blender.get_animation_data",
    "get_materials": "blender.get_materials",
    "get_scene": "blender.get_scene",
    "get_collections": "blender.get_collections",
    "get_armature_data": "blender.get_armature_data",
    "get_images": "blender.get_images",
    "capture_viewport": "blender.capture_viewport",
    "get_selection": "blender.get_selection",
    "edit_nodes": "blender.edit_nodes",
    "edit_animation": "blender.edit_animation",
    "edit_sequencer": "blender.edit_sequencer",
    "create_object": "blender.create_object",
    "modify_object": "blender.modify_object",
    "manage_material": "blender.manage_material",
    "manage_modifier": "blender.manage_modifier",
    "manage_collection": "blender.manage_collection",
    "manage_uv": "blender.manage_uv",
    "manage_constraints": "blender.manage_constraints",
    "manage_physics": "blender.manage_physics",
    "setup_scene": "blender.setup_scene",
    "execute_operator": "blender.execute_operator",
    "execute_script": "blender.execute_script",
    "import_export": "blender.import_export",
}


class ToolRouter:
    """Map Agent tool names to Engine capability requests."""

    def __init__(self, tool_mapping: Mapping[str, str] | None = None) -> None:
        self._tool_mapping: dict[str, str] = dict(DEFAULT_TOOL_MAPPING)
        if tool_mapping is not None:
            self._tool_mapping.update(tool_mapping)

    def map_to_engine(self, tool_name: str, args: Mapping[str, Any] | None = None) -> EngineRequest:
        """Translate an Agent tool call into an ``EngineRequest``."""

        capability = self._resolve_capability(tool_name)
        if capability is None:
            raise KeyError(f"unknown tool: {tool_name}")

        return EngineRequest(
            request_type=EngineRequestType.EXECUTE_CAPABILITY,
            capability=capability,
            payload=dict(args or {}),
        )

    def list_tools(self) -> list[dict[str, str]]:
        """Return the registered Agent-tool to Engine-capability mappings."""

        return [
            {"name": tool_name, "capability": capability}
            for tool_name, capability in sorted(self._tool_mapping.items())
        ]

    def _resolve_capability(self, tool_name: str) -> str | None:
        if tool_name.startswith("blender.") and tool_name in self._tool_mapping.values():
            return tool_name
        return self._tool_mapping.get(tool_name)
