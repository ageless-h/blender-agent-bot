from __future__ import annotations

from typing import Any

from ...protocol import SafetyLevel
from ..runtime import failure, require_bpy, success
from ..spec import ToolDefinition


def _set_xyz(target: Any, values: list[Any] | tuple[Any, ...]) -> None:
    if len(values) < 3:
        raise ValueError("xyz values must contain 3 elements")
    target[0] = float(values[0])
    target[1] = float(values[1])
    target[2] = float(values[2])


def create_object(arguments: dict[str, Any]) -> Any:
    tool_name = "create_object"
    try:
        bpy = require_bpy(tool_name)
        object_type = str(arguments.get("object_type", "MESH")).upper()
        primitive = str(arguments.get("primitive", "cube")).lower()
        name = str(arguments.get("name", "")).strip()
        location = arguments.get("location", [0.0, 0.0, 0.0])

        if object_type == "MESH":
            if primitive == "cube":
                bpy.ops.mesh.primitive_cube_add(location=location)
            elif primitive == "uv_sphere":
                bpy.ops.mesh.primitive_uv_sphere_add(location=location)
            elif primitive == "plane":
                bpy.ops.mesh.primitive_plane_add(location=location)
            elif primitive == "cylinder":
                bpy.ops.mesh.primitive_cylinder_add(location=location)
            else:
                raise ValueError(f"unsupported primitive: {primitive}")
        elif object_type == "EMPTY":
            bpy.ops.object.empty_add(location=location)
        elif object_type == "LIGHT":
            light_type = str(arguments.get("light_type", "POINT")).upper()
            bpy.ops.object.light_add(type=light_type, location=location)
        elif object_type == "CAMERA":
            bpy.ops.object.camera_add(location=location)
        else:
            raise ValueError(f"unsupported object_type: {object_type}")

        obj = bpy.context.active_object
        if obj is None:
            raise RuntimeError("failed to create object")

        if name:
            obj.name = name
        if isinstance(arguments.get("rotation"), (list, tuple)):
            _set_xyz(obj.rotation_euler, arguments["rotation"])
        if isinstance(arguments.get("scale"), (list, tuple)):
            _set_xyz(obj.scale, arguments["scale"])

        return success(
            tool_name,
            {
                "name": obj.name,
                "type": obj.type,
                "location": [float(obj.location[0]), float(obj.location[1]), float(obj.location[2])],
            },
        )
    except Exception as exc:
        return failure(tool_name, exc)


def modify_object(arguments: dict[str, Any]) -> Any:
    tool_name = "modify_object"
    try:
        bpy = require_bpy(tool_name)
        object_name = str(arguments.get("object_name", "")).strip()
        if not object_name:
            raise ValueError("object_name is required")

        obj = bpy.data.objects.get(object_name)
        if obj is None:
            raise ValueError(f"object not found: {object_name}")

        if isinstance(arguments.get("location"), (list, tuple)):
            _set_xyz(obj.location, arguments["location"])
        if isinstance(arguments.get("rotation"), (list, tuple)):
            _set_xyz(obj.rotation_euler, arguments["rotation"])
        if isinstance(arguments.get("scale"), (list, tuple)):
            _set_xyz(obj.scale, arguments["scale"])

        if "hide_viewport" in arguments:
            obj.hide_viewport = bool(arguments["hide_viewport"])
        if "hide_render" in arguments:
            obj.hide_render = bool(arguments["hide_render"])

        return success(tool_name, {"object_name": obj.name})
    except Exception as exc:
        return failure(tool_name, exc)


def delete_object(arguments: dict[str, Any]) -> Any:
    tool_name = "delete_object"
    try:
        bpy = require_bpy(tool_name)
        object_names = arguments.get("object_names")
        if object_names is None:
            object_name = str(arguments.get("object_name", "")).strip()
            object_names = [object_name] if object_name else []
        if not object_names:
            raise ValueError("object_name or object_names is required")

        deleted: list[str] = []
        for name in object_names:
            obj = bpy.data.objects.get(str(name))
            if obj is None:
                continue
            bpy.data.objects.remove(obj, do_unlink=True)
            deleted.append(obj.name)

        return success(tool_name, {"deleted": deleted, "count": len(deleted)})
    except Exception as exc:
        return failure(tool_name, exc)


def manage_material(arguments: dict[str, Any]) -> Any:
    tool_name = "manage_material"
    try:
        bpy = require_bpy(tool_name)
        action = str(arguments.get("action", "create")).lower()
        material_name = str(arguments.get("material_name", "")).strip() or "Material"

        material = bpy.data.materials.get(material_name)
        if action == "create":
            if material is None:
                material = bpy.data.materials.new(name=material_name)
            material.use_nodes = bool(arguments.get("use_nodes", True))
        elif action == "assign":
            object_name = str(arguments.get("object_name", "")).strip()
            if not object_name:
                raise ValueError("object_name is required for assign action")
            obj = bpy.data.objects.get(object_name)
            if obj is None:
                raise ValueError(f"object not found: {object_name}")
            if material is None:
                material = bpy.data.materials.new(name=material_name)
            if not obj.data.materials:
                obj.data.materials.append(material)
            else:
                obj.data.materials[0] = material
        elif action == "set_base_color":
            if material is None:
                raise ValueError(f"material not found: {material_name}")
            color = arguments.get("color", [1.0, 1.0, 1.0, 1.0])
            if len(color) < 4:
                raise ValueError("color must have 4 channels")
            material.diffuse_color = (float(color[0]), float(color[1]), float(color[2]), float(color[3]))
        else:
            raise ValueError(f"unsupported action: {action}")

        return success(tool_name, {"action": action, "material_name": material.name if material else material_name})
    except Exception as exc:
        return failure(tool_name, exc)


def add_modifier(arguments: dict[str, Any]) -> Any:
    tool_name = "add_modifier"
    try:
        bpy = require_bpy(tool_name)
        object_name = str(arguments.get("object_name", "")).strip()
        modifier_type = str(arguments.get("modifier_type", "")).strip().upper()
        modifier_name = str(arguments.get("modifier_name", modifier_type or "Modifier")).strip()
        if not object_name or not modifier_type:
            raise ValueError("object_name and modifier_type are required")

        obj = bpy.data.objects.get(object_name)
        if obj is None:
            raise ValueError(f"object not found: {object_name}")

        modifier = obj.modifiers.new(name=modifier_name, type=modifier_type)
        for key, value in dict(arguments.get("properties", {})).items():
            if hasattr(modifier, key):
                setattr(modifier, key, value)

        return success(
            tool_name, {"object_name": object_name, "modifier_name": modifier.name, "modifier_type": modifier.type}
        )
    except Exception as exc:
        return failure(tool_name, exc)


def add_constraint(arguments: dict[str, Any]) -> Any:
    tool_name = "add_constraint"
    try:
        bpy = require_bpy(tool_name)
        object_name = str(arguments.get("object_name", "")).strip()
        constraint_type = str(arguments.get("constraint_type", "")).strip().upper()
        constraint_name = str(arguments.get("constraint_name", constraint_type or "Constraint")).strip()
        if not object_name or not constraint_type:
            raise ValueError("object_name and constraint_type are required")

        obj = bpy.data.objects.get(object_name)
        if obj is None:
            raise ValueError(f"object not found: {object_name}")

        constraint = obj.constraints.new(type=constraint_type)
        constraint.name = constraint_name
        for key, value in dict(arguments.get("properties", {})).items():
            if hasattr(constraint, key):
                setattr(constraint, key, value)

        return success(
            tool_name,
            {"object_name": object_name, "constraint_name": constraint.name, "constraint_type": constraint.type},
        )
    except Exception as exc:
        return failure(tool_name, exc)


def set_parent(arguments: dict[str, Any]) -> Any:
    tool_name = "set_parent"
    try:
        bpy = require_bpy(tool_name)
        child_name = str(arguments.get("child_name", "")).strip()
        parent_name = str(arguments.get("parent_name", "")).strip()
        if not child_name or not parent_name:
            raise ValueError("child_name and parent_name are required")

        child = bpy.data.objects.get(child_name)
        parent = bpy.data.objects.get(parent_name)
        if child is None or parent is None:
            raise ValueError("child or parent object not found")

        child.parent = parent
        return success(tool_name, {"child_name": child.name, "parent_name": parent.name})
    except Exception as exc:
        return failure(tool_name, exc)


def manage_collection(arguments: dict[str, Any]) -> Any:
    tool_name = "manage_collection"
    try:
        bpy = require_bpy(tool_name)
        action = str(arguments.get("action", "create")).lower()
        collection_name = str(arguments.get("collection_name", "")).strip()
        if not collection_name:
            raise ValueError("collection_name is required")

        collection = bpy.data.collections.get(collection_name)
        if action == "create":
            if collection is None:
                collection = bpy.data.collections.new(collection_name)
                bpy.context.scene.collection.children.link(collection)
        elif action == "link_object":
            object_name = str(arguments.get("object_name", "")).strip()
            if not object_name:
                raise ValueError("object_name is required for link_object")
            obj = bpy.data.objects.get(object_name)
            if obj is None:
                raise ValueError(f"object not found: {object_name}")
            if collection is None:
                collection = bpy.data.collections.new(collection_name)
                bpy.context.scene.collection.children.link(collection)
            if obj not in collection.objects:
                collection.objects.link(obj)
        elif action == "unlink_object":
            object_name = str(arguments.get("object_name", "")).strip()
            if collection is None:
                raise ValueError(f"collection not found: {collection_name}")
            obj = bpy.data.objects.get(object_name)
            if obj is None:
                raise ValueError(f"object not found: {object_name}")
            if obj in collection.objects:
                collection.objects.unlink(obj)
        else:
            raise ValueError(f"unsupported action: {action}")

        return success(
            tool_name, {"action": action, "collection_name": collection.name if collection else collection_name}
        )
    except Exception as exc:
        return failure(tool_name, exc)


def setup_scene(arguments: dict[str, Any]) -> Any:
    tool_name = "setup_scene"
    try:
        bpy = require_bpy(tool_name)
        scene_name = str(arguments.get("scene_name", bpy.context.scene.name))
        scene = bpy.data.scenes.get(scene_name)
        if scene is None:
            raise ValueError(f"scene not found: {scene_name}")

        render = scene.render
        if "render_engine" in arguments:
            render.engine = str(arguments["render_engine"])
        if isinstance(arguments.get("resolution"), (list, tuple)) and len(arguments["resolution"]) >= 2:
            render.resolution_x = int(arguments["resolution"][0])
            render.resolution_y = int(arguments["resolution"][1])
        if "fps" in arguments:
            render.fps = int(arguments["fps"])
        if "camera_name" in arguments:
            camera = bpy.data.objects.get(str(arguments["camera_name"]))
            if camera is None:
                raise ValueError(f"camera not found: {arguments['camera_name']}")
            scene.camera = camera

        world_color = arguments.get("world_color")
        if isinstance(world_color, (list, tuple)) and len(world_color) >= 3 and scene.world is not None:
            scene.world.color = (float(world_color[0]), float(world_color[1]), float(world_color[2]))

        return success(tool_name, {"scene_name": scene_name, "render_engine": str(render.engine)})
    except Exception as exc:
        return failure(tool_name, exc)


def get_tool_definitions() -> list[ToolDefinition]:
    return [
        ToolDefinition("create_object", "创建对象", SafetyLevel.LEVEL_1, "imperative", create_object),
        ToolDefinition("modify_object", "修改对象属性", SafetyLevel.LEVEL_1, "imperative", modify_object),
        ToolDefinition("delete_object", "删除对象", SafetyLevel.LEVEL_2, "imperative", delete_object),
        ToolDefinition("manage_material", "创建/编辑/分配材质", SafetyLevel.LEVEL_1, "imperative", manage_material),
        ToolDefinition("add_modifier", "添加修改器", SafetyLevel.LEVEL_1, "imperative", add_modifier),
        ToolDefinition("add_constraint", "添加约束", SafetyLevel.LEVEL_1, "imperative", add_constraint),
        ToolDefinition("set_parent", "设置父子关系", SafetyLevel.LEVEL_1, "imperative", set_parent),
        ToolDefinition("manage_collection", "管理集合", SafetyLevel.LEVEL_1, "imperative", manage_collection),
        ToolDefinition("setup_scene", "设置场景参数", SafetyLevel.LEVEL_1, "imperative", setup_scene),
    ]


__all__ = ["get_tool_definitions"]
