from __future__ import annotations

import base64
import os
import tempfile
from typing import Any

from ...protocol import SafetyLevel
from ..runtime import failure, require_bpy, success
from ..spec import ToolDefinition


def _vector(values: Any) -> list[float]:
    return [float(values[0]), float(values[1]), float(values[2])]


def get_objects(arguments: dict[str, Any]) -> Any:
    tool_name = "get_objects"
    try:
        bpy = require_bpy(tool_name)
        limit = int(arguments.get("limit", 500))
        items = []
        for obj in bpy.data.objects[: max(limit, 0)]:
            items.append(
                {
                    "name": obj.name,
                    "type": obj.type,
                    "location": _vector(obj.location),
                    "rotation_euler": _vector(obj.rotation_euler),
                    "scale": _vector(obj.scale),
                }
            )
        return success(tool_name, {"count": len(items), "objects": items})
    except Exception as exc:
        return failure(tool_name, exc)


def get_object_info(arguments: dict[str, Any]) -> Any:
    tool_name = "get_object_info"
    try:
        bpy = require_bpy(tool_name)
        object_name = str(arguments.get("object_name", "")).strip()
        if not object_name:
            raise ValueError("object_name is required")

        obj = bpy.data.objects.get(object_name)
        if obj is None:
            raise ValueError(f"object not found: {object_name}")

        payload = {
            "name": obj.name,
            "type": obj.type,
            "data_name": getattr(obj.data, "name", None),
            "parent": obj.parent.name if obj.parent else None,
            "location": _vector(obj.location),
            "rotation_euler": _vector(obj.rotation_euler),
            "scale": _vector(obj.scale),
            "modifiers": [modifier.name for modifier in obj.modifiers],
            "constraints": [constraint.name for constraint in obj.constraints],
            "material_slots": [slot.name for slot in obj.material_slots],
            "visible": bool(obj.visible_get()),
            "selected": bool(obj.select_get()),
        }
        return success(tool_name, payload)
    except Exception as exc:
        return failure(tool_name, exc)


def get_scene(arguments: dict[str, Any]) -> Any:
    tool_name = "get_scene"
    try:
        bpy = require_bpy(tool_name)
        scene_name = str(arguments.get("scene_name", bpy.context.scene.name))
        scene = bpy.data.scenes.get(scene_name)
        if scene is None:
            raise ValueError(f"scene not found: {scene_name}")

        payload = {
            "name": scene.name,
            "frame_start": int(scene.frame_start),
            "frame_end": int(scene.frame_end),
            "frame_current": int(scene.frame_current),
            "fps": int(scene.render.fps),
            "object_count": len(scene.objects),
            "collection_name": scene.collection.name,
            "camera": scene.camera.name if scene.camera else None,
        }
        return success(tool_name, payload)
    except Exception as exc:
        return failure(tool_name, exc)


def get_node_tree(arguments: dict[str, Any]) -> Any:
    tool_name = "get_node_tree"
    try:
        bpy = require_bpy(tool_name)
        target = str(arguments.get("target", "material"))
        target_name = str(arguments.get("target_name", ""))

        node_tree = None
        if target == "material":
            if not target_name:
                raise ValueError("target_name is required for material")
            material = bpy.data.materials.get(target_name)
            if material is None or material.node_tree is None:
                raise ValueError(f"material or node tree not found: {target_name}")
            node_tree = material.node_tree
        elif target == "world":
            world = bpy.context.scene.world if not target_name else bpy.data.worlds.get(target_name)
            if world is None or world.node_tree is None:
                raise ValueError("world or node tree not found")
            node_tree = world.node_tree
        elif target == "scene":
            scene = bpy.context.scene if not target_name else bpy.data.scenes.get(target_name)
            if scene is None or scene.node_tree is None:
                raise ValueError("scene or node tree not found")
            node_tree = scene.node_tree
        else:
            raise ValueError("target must be one of: material, world, scene")

        nodes = []
        links = []
        for node in node_tree.nodes:
            nodes.append(
                {
                    "name": node.name,
                    "type": node.bl_idname,
                    "location": [float(node.location[0]), float(node.location[1])],
                }
            )
        for link in node_tree.links:
            links.append(
                {
                    "from_node": link.from_node.name,
                    "from_socket": link.from_socket.name,
                    "to_node": link.to_node.name,
                    "to_socket": link.to_socket.name,
                }
            )

        return success(tool_name, {"node_count": len(nodes), "nodes": nodes, "links": links})
    except Exception as exc:
        return failure(tool_name, exc)


def get_modifiers(arguments: dict[str, Any]) -> Any:
    tool_name = "get_modifiers"
    try:
        bpy = require_bpy(tool_name)
        object_name = str(arguments.get("object_name", "")).strip()
        if not object_name:
            raise ValueError("object_name is required")
        obj = bpy.data.objects.get(object_name)
        if obj is None:
            raise ValueError(f"object not found: {object_name}")

        modifiers = []
        for modifier in obj.modifiers:
            modifiers.append(
                {"name": modifier.name, "type": modifier.type, "show_viewport": bool(modifier.show_viewport)}
            )
        return success(tool_name, {"object_name": object_name, "modifiers": modifiers})
    except Exception as exc:
        return failure(tool_name, exc)


def get_constraints(arguments: dict[str, Any]) -> Any:
    tool_name = "get_constraints"
    try:
        bpy = require_bpy(tool_name)
        object_name = str(arguments.get("object_name", "")).strip()
        if not object_name:
            raise ValueError("object_name is required")
        obj = bpy.data.objects.get(object_name)
        if obj is None:
            raise ValueError(f"object not found: {object_name}")

        constraints = []
        for constraint in obj.constraints:
            constraints.append(
                {
                    "name": constraint.name,
                    "type": constraint.type,
                    "influence": float(getattr(constraint, "influence", 1.0)),
                }
            )
        return success(tool_name, {"object_name": object_name, "constraints": constraints})
    except Exception as exc:
        return failure(tool_name, exc)


def get_materials(arguments: dict[str, Any]) -> Any:
    tool_name = "get_materials"
    try:
        bpy = require_bpy(tool_name)
        include_users = bool(arguments.get("include_users", True))
        materials = []
        for material in bpy.data.materials:
            item = {"name": material.name, "use_nodes": bool(material.use_nodes)}
            if include_users:
                item["users"] = int(material.users)
            materials.append(item)
        return success(tool_name, {"count": len(materials), "materials": materials})
    except Exception as exc:
        return failure(tool_name, exc)


def get_animation_data(arguments: dict[str, Any]) -> Any:
    tool_name = "get_animation_data"
    try:
        bpy = require_bpy(tool_name)
        object_name = str(arguments.get("object_name", "")).strip()
        if not object_name:
            raise ValueError("object_name is required")
        obj = bpy.data.objects.get(object_name)
        if obj is None:
            raise ValueError(f"object not found: {object_name}")

        animation_data = obj.animation_data
        if animation_data is None or animation_data.action is None:
            return success(tool_name, {"object_name": object_name, "fcurves": []})

        fcurves = []
        for fcurve in animation_data.action.fcurves:
            keyframes = []
            for keyframe in fcurve.keyframe_points:
                keyframes.append(
                    {
                        "frame": float(keyframe.co[0]),
                        "value": float(keyframe.co[1]),
                        "interpolation": str(keyframe.interpolation),
                    }
                )
            fcurves.append(
                {
                    "data_path": fcurve.data_path,
                    "array_index": int(fcurve.array_index),
                    "keyframes": keyframes,
                }
            )
        return success(tool_name, {"object_name": object_name, "fcurves": fcurves})
    except Exception as exc:
        return failure(tool_name, exc)


def get_render_settings(arguments: dict[str, Any]) -> Any:
    tool_name = "get_render_settings"
    try:
        bpy = require_bpy(tool_name)
        scene_name = str(arguments.get("scene_name", bpy.context.scene.name))
        scene = bpy.data.scenes.get(scene_name)
        if scene is None:
            raise ValueError(f"scene not found: {scene_name}")
        render = scene.render
        return success(
            tool_name,
            {
                "scene_name": scene_name,
                "engine": str(render.engine),
                "resolution": [int(render.resolution_x), int(render.resolution_y)],
                "resolution_percentage": int(render.resolution_percentage),
                "filepath": str(render.filepath),
                "fps": int(render.fps),
            },
        )
    except Exception as exc:
        return failure(tool_name, exc)


def get_world_settings(arguments: dict[str, Any]) -> Any:
    tool_name = "get_world_settings"
    try:
        bpy = require_bpy(tool_name)
        world_name = str(arguments.get("world_name", "")).strip()
        world = bpy.context.scene.world if not world_name else bpy.data.worlds.get(world_name)
        if world is None:
            raise ValueError("world not found")

        payload = {
            "name": world.name,
            "use_nodes": bool(world.use_nodes),
            "color": [float(world.color[0]), float(world.color[1]), float(world.color[2])],
        }
        if world.node_tree is not None:
            payload["node_count"] = len(world.node_tree.nodes)
        return success(tool_name, payload)
    except Exception as exc:
        return failure(tool_name, exc)


def capture_viewport(arguments: dict[str, Any]) -> Any:
    tool_name = "capture_viewport"
    temp_path = ""
    try:
        bpy = require_bpy(tool_name)
        filepath = str(arguments.get("filepath", "")).strip()
        if filepath:
            temp_path = filepath
        else:
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as handle:
                temp_path = handle.name

        bpy.ops.screen.screenshot(filepath=temp_path, full=False)
        with open(temp_path, "rb") as image_file:
            content = image_file.read()

        encoded = base64.b64encode(content).decode("utf-8")
        return success(tool_name, {"base64": encoded, "bytes": len(content)})
    except Exception as exc:
        return failure(tool_name, exc)
    finally:
        if temp_path and not arguments.get("filepath") and os.path.exists(temp_path):
            try:
                os.remove(temp_path)
            except OSError:
                pass


def get_tool_definitions() -> list[ToolDefinition]:
    return [
        ToolDefinition("get_objects", "获取场景中所有对象列表", SafetyLevel.LEVEL_0, "perception", get_objects),
        ToolDefinition("get_object_info", "获取单个对象详细信息", SafetyLevel.LEVEL_0, "perception", get_object_info),
        ToolDefinition("get_scene", "获取场景全局信息", SafetyLevel.LEVEL_0, "perception", get_scene),
        ToolDefinition("get_node_tree", "获取节点树结构", SafetyLevel.LEVEL_0, "perception", get_node_tree),
        ToolDefinition("get_modifiers", "获取修改器列表", SafetyLevel.LEVEL_0, "perception", get_modifiers),
        ToolDefinition("get_constraints", "获取约束列表", SafetyLevel.LEVEL_0, "perception", get_constraints),
        ToolDefinition("get_materials", "获取材质列表", SafetyLevel.LEVEL_0, "perception", get_materials),
        ToolDefinition("get_animation_data", "获取动画数据", SafetyLevel.LEVEL_0, "perception", get_animation_data),
        ToolDefinition("get_render_settings", "获取渲染设置", SafetyLevel.LEVEL_0, "perception", get_render_settings),
        ToolDefinition("get_world_settings", "获取世界环境设置", SafetyLevel.LEVEL_0, "perception", get_world_settings),
        ToolDefinition("capture_viewport", "截取视口截图(base64)", SafetyLevel.LEVEL_0, "perception", capture_viewport),
    ]


__all__ = ["get_tool_definitions"]
