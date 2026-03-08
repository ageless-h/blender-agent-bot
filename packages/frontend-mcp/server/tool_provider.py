from __future__ import annotations

import base64
import json
from dataclasses import dataclass
from typing import Any, Mapping, Protocol, Sequence

import mcp.types as mcp_types
from pydantic import AnyUrl, TypeAdapter

TOOL_RESULT_URI = "blender://tool-result"
VIEWPORT_SAMPLE_BASE64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQIHWP4z8DwHwAFAAH/l7l8WQAAAABJRU5ErkJggg=="
)
_ANY_URL_ADAPTER = TypeAdapter(AnyUrl)


def _as_any_url(uri: str) -> AnyUrl:
    return _ANY_URL_ADAPTER.validate_python(uri)


def _object_schema(
    properties: Mapping[str, Any],
    required: Sequence[str] | None = None,
    *,
    additional_properties: bool = False,
) -> dict[str, Any]:
    schema: dict[str, Any] = {
        "type": "object",
        "properties": dict(properties),
        "additionalProperties": additional_properties,
    }
    if required:
        schema["required"] = list(required)
    return schema


@dataclass(frozen=True)
class ToolSpec:
    name: str
    description: str
    input_schema: dict[str, Any]
    read_only: bool = False
    destructive: bool = False
    idempotent: bool | None = None
    open_world: bool | None = None

    def to_mcp_tool(self) -> mcp_types.Tool:
        annotation_data: dict[str, Any] = {}
        if self.read_only:
            annotation_data["readOnlyHint"] = True
            annotation_data["idempotentHint"] = True
        if self.destructive:
            annotation_data["destructiveHint"] = True
        if self.idempotent is not None:
            annotation_data["idempotentHint"] = self.idempotent
        if self.open_world is not None:
            annotation_data["openWorldHint"] = self.open_world
        annotations = mcp_types.ToolAnnotations(**annotation_data) if annotation_data else None
        return mcp_types.Tool(
            name=self.name,
            description=self.description,
            inputSchema=self.input_schema,
            annotations=annotations,
        )


class EngineInvoker(Protocol):
    async def invoke_tool(self, name: str, arguments: dict[str, Any]) -> Any: ...


class ToolExecutionError(RuntimeError):
    pass


DEFAULT_TOOL_SPECS: tuple[ToolSpec, ...] = (
    ToolSpec(
        name="get_objects",
        description="获取场景对象列表（只读）",
        input_schema=_object_schema(
            {
                "collection": {"type": "string"},
                "include_hidden": {"type": "boolean", "default": False},
            }
        ),
        read_only=True,
    ),
    ToolSpec(
        name="get_object_info",
        description="获取单个对象详细信息（只读）",
        input_schema=_object_schema(
            {
                "name": {"type": "string", "description": "对象名称"},
            },
            required=["name"],
        ),
        read_only=True,
    ),
    ToolSpec(
        name="get_scene",
        description="获取场景全局信息（只读）",
        input_schema=_object_schema({}),
        read_only=True,
    ),
    ToolSpec(
        name="get_node_tree",
        description="获取节点树结构（只读）",
        input_schema=_object_schema(
            {
                "node_tree": {"type": "string", "description": "节点树名称"},
            },
            required=["node_tree"],
        ),
        read_only=True,
    ),
    ToolSpec(
        name="get_modifiers",
        description="获取对象修改器列表（只读）",
        input_schema=_object_schema(
            {
                "object_name": {"type": "string"},
            },
            required=["object_name"],
        ),
        read_only=True,
    ),
    ToolSpec(
        name="get_constraints",
        description="获取对象约束列表（只读）",
        input_schema=_object_schema(
            {
                "object_name": {"type": "string"},
            },
            required=["object_name"],
        ),
        read_only=True,
    ),
    ToolSpec(
        name="get_materials",
        description="获取材质列表（只读）",
        input_schema=_object_schema(
            {
                "object_name": {"type": "string"},
            }
        ),
        read_only=True,
    ),
    ToolSpec(
        name="get_animation_data",
        description="获取动画数据（只读）",
        input_schema=_object_schema(
            {
                "object_name": {"type": "string"},
            }
        ),
        read_only=True,
    ),
    ToolSpec(
        name="get_render_settings",
        description="获取渲染设置（只读）",
        input_schema=_object_schema({}),
        read_only=True,
    ),
    ToolSpec(
        name="get_world_settings",
        description="获取世界环境设置（只读）",
        input_schema=_object_schema({}),
        read_only=True,
    ),
    ToolSpec(
        name="capture_viewport",
        description="截图当前视口（只读）",
        input_schema=_object_schema(
            {
                "format": {"type": "string", "enum": ["png", "jpeg"], "default": "png"},
                "width": {"type": "integer", "minimum": 1},
                "height": {"type": "integer", "minimum": 1},
            }
        ),
        read_only=True,
    ),
    ToolSpec(
        name="edit_nodes",
        description="声明式节点编辑",
        input_schema=_object_schema(
            {
                "node_tree": {"type": "string"},
                "operations": {"type": "array", "items": {"type": "object"}},
            },
            required=["node_tree", "operations"],
            additional_properties=True,
        ),
        destructive=False,
    ),
    ToolSpec(
        name="edit_animation",
        description="声明式动画编辑",
        input_schema=_object_schema(
            {
                "target": {"type": "string"},
                "keyframes": {"type": "array", "items": {"type": "object"}},
            },
            required=["target", "keyframes"],
            additional_properties=True,
        ),
    ),
    ToolSpec(
        name="edit_sequencer",
        description="声明式序列编辑",
        input_schema=_object_schema(
            {
                "operations": {"type": "array", "items": {"type": "object"}},
            },
            required=["operations"],
            additional_properties=True,
        ),
    ),
    ToolSpec(
        name="create_object",
        description="创建对象",
        input_schema=_object_schema(
            {
                "name": {"type": "string"},
                "object_type": {
                    "type": "string",
                    "enum": ["MESH", "CURVE", "LIGHT", "CAMERA", "EMPTY"],
                    "default": "MESH",
                },
                "primitive": {"type": "string", "default": "cube"},
                "location": {
                    "type": "array",
                    "items": {"type": "number"},
                    "minItems": 3,
                    "maxItems": 3,
                },
            },
            required=["name"],
        ),
    ),
    ToolSpec(
        name="modify_object",
        description="修改对象属性",
        input_schema=_object_schema(
            {
                "name": {"type": "string"},
                "location": {"type": "array", "items": {"type": "number"}},
                "rotation": {"type": "array", "items": {"type": "number"}},
                "scale": {"type": "array", "items": {"type": "number"}},
            },
            required=["name"],
            additional_properties=True,
        ),
    ),
    ToolSpec(
        name="delete_object",
        description="删除对象",
        input_schema=_object_schema(
            {
                "name": {"type": "string"},
            },
            required=["name"],
        ),
        destructive=True,
    ),
    ToolSpec(
        name="manage_material",
        description="管理材质",
        input_schema=_object_schema(
            {
                "action": {"type": "string", "enum": ["create", "assign", "update"]},
                "material_name": {"type": "string"},
                "object_name": {"type": "string"},
            },
            required=["action"],
            additional_properties=True,
        ),
    ),
    ToolSpec(
        name="add_modifier",
        description="添加修改器",
        input_schema=_object_schema(
            {
                "object_name": {"type": "string"},
                "modifier_type": {"type": "string"},
                "name": {"type": "string"},
            },
            required=["object_name", "modifier_type"],
            additional_properties=True,
        ),
    ),
    ToolSpec(
        name="add_constraint",
        description="添加约束",
        input_schema=_object_schema(
            {
                "object_name": {"type": "string"},
                "constraint_type": {"type": "string"},
            },
            required=["object_name", "constraint_type"],
            additional_properties=True,
        ),
    ),
    ToolSpec(
        name="set_parent",
        description="设置父子关系",
        input_schema=_object_schema(
            {
                "child": {"type": "string"},
                "parent": {"type": "string"},
            },
            required=["child", "parent"],
        ),
    ),
    ToolSpec(
        name="manage_collection",
        description="管理集合",
        input_schema=_object_schema(
            {
                "action": {"type": "string", "enum": ["create", "move", "delete"]},
                "collection_name": {"type": "string"},
                "object_name": {"type": "string"},
            },
            required=["action", "collection_name"],
        ),
    ),
    ToolSpec(
        name="setup_scene",
        description="设置场景参数",
        input_schema=_object_schema(
            {
                "render_engine": {"type": "string"},
                "resolution_x": {"type": "integer", "minimum": 1},
                "resolution_y": {"type": "integer", "minimum": 1},
                "frame_start": {"type": "integer"},
                "frame_end": {"type": "integer"},
            },
            additional_properties=True,
        ),
    ),
    ToolSpec(
        name="execute_script",
        description="执行脚本（高权限）",
        input_schema=_object_schema(
            {
                "script": {"type": "string"},
                "timeout_seconds": {"type": "number", "minimum": 0.1},
            },
            required=["script"],
        ),
        destructive=True,
        open_world=True,
    ),
    ToolSpec(
        name="execute_operator",
        description="执行 bpy.ops 操作符",
        input_schema=_object_schema(
            {
                "operator": {"type": "string"},
                "kwargs": {"type": "object"},
            },
            required=["operator"],
            additional_properties=True,
        ),
    ),
    ToolSpec(
        name="import_export",
        description="导入导出文件",
        input_schema=_object_schema(
            {
                "action": {"type": "string", "enum": ["import", "export"]},
                "format": {
                    "type": "string",
                    "enum": ["blend", "fbx", "glb", "obj", "usd"],
                },
                "filepath": {"type": "string"},
            },
            required=["action", "format", "filepath"],
        ),
    ),
)


class DefaultEngineInvoker:
    async def invoke_tool(self, name: str, arguments: dict[str, Any]) -> Any:
        if name == "capture_viewport":
            return {
                "message": "已返回示例视口截图，接入 engine 后将返回真实截图。",
                "image_base64": VIEWPORT_SAMPLE_BASE64,
                "mimeType": "image/png",
                "arguments": arguments,
            }
        if name == "get_scene":
            return {
                "name": "Scene",
                "frame_current": 1,
                "render_engine": "BLENDER_EEVEE",
            }
        if name == "get_objects":
            return {
                "objects": [{"name": "Cube", "type": "MESH"}],
                "count": 1,
            }
        return {
            "status": "queued",
            "tool": name,
            "arguments": arguments,
        }


class ToolProvider:
    def __init__(
        self,
        *,
        engine_invoker: EngineInvoker | None = None,
        tool_specs: Sequence[ToolSpec] = DEFAULT_TOOL_SPECS,
    ) -> None:
        self._engine_invoker = engine_invoker or DefaultEngineInvoker()
        self._tool_specs = tuple(tool_specs)
        self._tool_by_name = {spec.name: spec for spec in self._tool_specs}

    def list_tool_specs(self) -> tuple[ToolSpec, ...]:
        return self._tool_specs

    def list_tools(self) -> list[mcp_types.Tool]:
        return [tool_spec.to_mcp_tool() for tool_spec in self._tool_specs]

    def is_read_only(self, tool_name: str) -> bool:
        spec = self._tool_by_name.get(tool_name)
        return bool(spec and spec.read_only)

    async def call_tool(
        self,
        tool_name: str,
        arguments: Mapping[str, Any] | None,
    ) -> list[mcp_types.TextContent | mcp_types.ImageContent | mcp_types.EmbeddedResource]:
        spec = self._tool_by_name.get(tool_name)
        if spec is None:
            raise ToolExecutionError(f"未知工具: {tool_name}")

        normalized_arguments = dict(arguments or {})
        try:
            raw_result = await self._engine_invoker.invoke_tool(spec.name, normalized_arguments)
        except Exception as error:
            raise ToolExecutionError(f"工具执行失败: {spec.name}: {error}") from error

        return self._normalize_result(raw_result)

    def _normalize_result(
        self,
        raw_result: Any,
    ) -> list[mcp_types.TextContent | mcp_types.ImageContent | mcp_types.EmbeddedResource]:
        if raw_result is None:
            return [mcp_types.TextContent(type="text", text="执行完成")]

        if isinstance(raw_result, (mcp_types.TextContent, mcp_types.ImageContent, mcp_types.EmbeddedResource)):
            return [raw_result]

        if isinstance(raw_result, Sequence) and not isinstance(raw_result, (str, bytes, bytearray)):
            if all(
                isinstance(item, (mcp_types.TextContent, mcp_types.ImageContent, mcp_types.EmbeddedResource))
                for item in raw_result
            ):
                return list(raw_result)

        if isinstance(raw_result, Mapping):
            return self._normalize_mapping_result(dict(raw_result))

        if isinstance(raw_result, (str, int, float, bool)):
            return [mcp_types.TextContent(type="text", text=str(raw_result))]

        serialized = json.dumps(raw_result, ensure_ascii=False, indent=2, default=str)
        return [mcp_types.TextContent(type="text", text=serialized)]

    def _normalize_mapping_result(
        self,
        result: dict[str, Any],
    ) -> list[mcp_types.TextContent | mcp_types.ImageContent | mcp_types.EmbeddedResource]:
        if "image_base64" in result or "image" in result or "data" in result:
            image_payload = result.get("image_base64") or result.get("image") or result.get("data")
            mime_type = str(result.get("mimeType") or result.get("mime_type") or "image/png")
            contents: list[mcp_types.TextContent | mcp_types.ImageContent | mcp_types.EmbeddedResource] = []
            if result.get("message"):
                contents.append(mcp_types.TextContent(type="text", text=str(result["message"])))

            if isinstance(image_payload, bytes):
                encoded = base64.b64encode(image_payload).decode("utf-8")
            elif isinstance(image_payload, str):
                encoded = image_payload
            else:
                raise ToolExecutionError("图片结果格式无效：image_base64/image/data 不是字符串或字节")

            if encoded.startswith("data:") and "," in encoded:
                encoded = encoded.split(",", maxsplit=1)[1]

            contents.append(
                mcp_types.ImageContent(
                    type="image",
                    data=encoded,
                    mimeType=mime_type,
                )
            )
            return contents

        if "resource_text" in result:
            resource_uri = str(result.get("resource_uri") or TOOL_RESULT_URI)
            resource_mime = str(result.get("mimeType") or result.get("mime_type") or "text/plain")
            resource_text = str(result["resource_text"])
            resource = mcp_types.TextResourceContents(
                uri=_as_any_url(resource_uri),
                mimeType=resource_mime,
                text=resource_text,
            )
            return [mcp_types.EmbeddedResource(type="resource", resource=resource)]

        if "resource_blob" in result:
            resource_uri = str(result.get("resource_uri") or TOOL_RESULT_URI)
            resource_mime = str(result.get("mimeType") or result.get("mime_type") or "application/octet-stream")
            blob_payload = result["resource_blob"]
            if isinstance(blob_payload, bytes):
                encoded_blob = base64.b64encode(blob_payload).decode("utf-8")
            elif isinstance(blob_payload, str):
                encoded_blob = blob_payload
            else:
                raise ToolExecutionError("二进制资源结果格式无效：resource_blob 不是字符串或字节")
            resource = mcp_types.BlobResourceContents(
                uri=_as_any_url(resource_uri),
                mimeType=resource_mime,
                blob=encoded_blob,
            )
            return [mcp_types.EmbeddedResource(type="resource", resource=resource)]

        serialized = json.dumps(result, ensure_ascii=False, indent=2, default=str)
        return [mcp_types.TextContent(type="text", text=serialized)]
