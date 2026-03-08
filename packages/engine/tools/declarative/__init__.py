from __future__ import annotations

from typing import Any

from ...protocol import SafetyLevel
from ..runtime import failure, require_bpy, success
from ..spec import ToolDefinition


def edit_nodes(arguments: dict[str, Any]) -> Any:
    tool_name = "edit_nodes"
    try:
        bpy = require_bpy(tool_name)
        material_name = str(arguments.get("material_name", "")).strip() or "Material"
        clear_existing = bool(arguments.get("clear_existing", False))
        node_defs = arguments.get("nodes", [])
        link_defs = arguments.get("links", [])

        material = bpy.data.materials.get(material_name)
        if material is None:
            material = bpy.data.materials.new(name=material_name)
        material.use_nodes = True

        node_tree = material.node_tree
        if node_tree is None:
            raise RuntimeError("material node tree is unavailable")

        if clear_existing:
            node_tree.nodes.clear()

        created_nodes: dict[str, Any] = {}
        for node_def in node_defs:
            if not isinstance(node_def, dict):
                continue
            node_type = str(node_def.get("type", ""))
            if not node_type:
                continue
            node = node_tree.nodes.new(type=node_type)
            node.name = str(node_def.get("name", node.name))
            location = node_def.get("location", [0, 0])
            if isinstance(location, (list, tuple)) and len(location) >= 2:
                node.location = (float(location[0]), float(location[1]))
            created_nodes[node.name] = node

        for link_def in link_defs:
            if not isinstance(link_def, dict):
                continue
            from_node_name = str(link_def.get("from_node", ""))
            to_node_name = str(link_def.get("to_node", ""))
            from_socket_name = str(link_def.get("from_socket", ""))
            to_socket_name = str(link_def.get("to_socket", ""))

            from_node = created_nodes.get(from_node_name) or node_tree.nodes.get(from_node_name)
            to_node = created_nodes.get(to_node_name) or node_tree.nodes.get(to_node_name)
            if from_node is None or to_node is None:
                continue
            from_socket = from_node.outputs.get(from_socket_name)
            to_socket = to_node.inputs.get(to_socket_name)
            if from_socket is None or to_socket is None:
                continue
            node_tree.links.new(from_socket, to_socket)

        return success(
            tool_name,
            {
                "material_name": material.name,
                "node_count": len(node_tree.nodes),
                "link_count": len(node_tree.links),
            },
        )
    except Exception as exc:
        return failure(tool_name, exc)


def edit_animation(arguments: dict[str, Any]) -> Any:
    tool_name = "edit_animation"
    try:
        bpy = require_bpy(tool_name)
        object_name = str(arguments.get("object_name", "")).strip()
        if not object_name:
            raise ValueError("object_name is required")

        obj = bpy.data.objects.get(object_name)
        if obj is None:
            raise ValueError(f"object not found: {object_name}")

        keyframes = arguments.get("keyframes", [])
        inserted = 0
        for keyframe in keyframes:
            if not isinstance(keyframe, dict):
                continue
            data_path = str(keyframe.get("data_path", ""))
            frame = keyframe.get("frame")
            value = keyframe.get("value")
            if not data_path or frame is None or value is None:
                continue

            index = int(keyframe.get("index", -1))
            if index < 0:
                setattr(obj, data_path, value)
                obj.keyframe_insert(data_path=data_path, frame=float(frame))
            else:
                target = getattr(obj, data_path)
                target[index] = value
                obj.keyframe_insert(data_path=data_path, frame=float(frame), index=index)
            inserted += 1

        return success(tool_name, {"object_name": object_name, "inserted_keyframes": inserted})
    except Exception as exc:
        return failure(tool_name, exc)


def edit_sequencer(arguments: dict[str, Any]) -> Any:
    tool_name = "edit_sequencer"
    try:
        bpy = require_bpy(tool_name)
        scene_name = str(arguments.get("scene_name", bpy.context.scene.name))
        scene = bpy.data.scenes.get(scene_name)
        if scene is None:
            raise ValueError(f"scene not found: {scene_name}")

        if scene.sequence_editor is None:
            scene.sequence_editor_create()

        operations = arguments.get("operations", [])
        applied = 0
        for operation in operations:
            if not isinstance(operation, dict):
                continue
            action = str(operation.get("action", "")).strip()
            if action == "delete":
                strip_name = str(operation.get("strip_name", "")).strip()
                strip = scene.sequence_editor.sequences_all.get(strip_name)
                if strip is None:
                    continue
                scene.sequence_editor.sequences.remove(strip)
                applied += 1
                continue

            if action == "rename":
                strip_name = str(operation.get("strip_name", "")).strip()
                new_name = str(operation.get("new_name", "")).strip()
                strip = scene.sequence_editor.sequences_all.get(strip_name)
                if strip is None or not new_name:
                    continue
                strip.name = new_name
                applied += 1

        return success(tool_name, {"scene_name": scene_name, "applied_operations": applied})
    except Exception as exc:
        return failure(tool_name, exc)


def get_tool_definitions() -> list[ToolDefinition]:
    return [
        ToolDefinition("edit_nodes", "声明式节点编辑", SafetyLevel.LEVEL_1, "declarative", edit_nodes),
        ToolDefinition("edit_animation", "声明式动画编辑", SafetyLevel.LEVEL_1, "declarative", edit_animation),
        ToolDefinition("edit_sequencer", "声明式序列编辑器操作", SafetyLevel.LEVEL_1, "declarative", edit_sequencer),
    ]


__all__ = ["get_tool_definitions"]
