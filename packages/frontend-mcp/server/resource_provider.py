from __future__ import annotations

import base64
import json
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Any, Mapping, Protocol

import mcp.types as mcp_types
from mcp.server.lowlevel.helper_types import ReadResourceContents
from pydantic import AnyUrl, TypeAdapter

SCENE_RESOURCE_URI = "blender://scene"
OBJECTS_RESOURCE_URI = "blender://objects"
VIEWPORT_RESOURCE_URI = "blender://viewport"
DEFAULT_RESOURCE_URIS = (SCENE_RESOURCE_URI, OBJECTS_RESOURCE_URI, VIEWPORT_RESOURCE_URI)
VIEWPORT_SAMPLE_BASE64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQIHWP4z8DwHwAFAAH/l7l8WQAAAABJRU5ErkJggg=="
)
_ANY_URL_ADAPTER = TypeAdapter(AnyUrl)


def _as_any_url(uri: str) -> AnyUrl:
    return _ANY_URL_ADAPTER.validate_python(uri)


class ResourceBackend(Protocol):
    async def get_scene(self) -> Mapping[str, Any]: ...

    async def get_objects(self) -> list[Mapping[str, Any]]: ...

    async def capture_viewport(self) -> Mapping[str, Any] | str | bytes: ...


class DefaultResourceBackend:
    async def get_scene(self) -> Mapping[str, Any]:
        return {
            "name": "Scene",
            "frame_start": 1,
            "frame_end": 250,
            "frame_current": 1,
            "render_engine": "BLENDER_EEVEE",
        }

    async def get_objects(self) -> list[Mapping[str, Any]]:
        return [
            {
                "name": "Cube",
                "type": "MESH",
                "location": [0.0, 0.0, 0.0],
            }
        ]

    async def capture_viewport(self) -> Mapping[str, Any] | str | bytes:
        return {
            "image_base64": VIEWPORT_SAMPLE_BASE64,
            "mimeType": "image/png",
        }


@dataclass
class _ViewportCacheEntry:
    contents: list[ReadResourceContents]
    expires_at: datetime


class ResourceProvider:
    def __init__(
        self,
        backend: ResourceBackend | None = None,
        *,
        viewport_cache_ttl_seconds: float = 2.0,
    ) -> None:
        self._backend = backend or DefaultResourceBackend()
        self._viewport_cache_ttl_seconds = viewport_cache_ttl_seconds
        self._viewport_cache: _ViewportCacheEntry | None = None

    def list_resources(self) -> list[mcp_types.Resource]:
        return [
            mcp_types.Resource(
                uri=_as_any_url(SCENE_RESOURCE_URI),
                name="Blender Scene",
                description="当前场景概要信息",
                mimeType="application/json",
            ),
            mcp_types.Resource(
                uri=_as_any_url(OBJECTS_RESOURCE_URI),
                name="Blender Objects",
                description="场景对象列表",
                mimeType="application/json",
            ),
            mcp_types.Resource(
                uri=_as_any_url(VIEWPORT_RESOURCE_URI),
                name="Blender Viewport",
                description="视口截图（支持缓存）",
                mimeType="image/png",
            ),
        ]

    async def read_resource(self, uri: str) -> list[ReadResourceContents]:
        uri_text = str(uri)
        if uri_text.startswith(SCENE_RESOURCE_URI):
            return await self._read_scene_resource()
        if uri_text.startswith(OBJECTS_RESOURCE_URI):
            return await self._read_objects_resource()
        if uri_text.startswith(VIEWPORT_RESOURCE_URI):
            return await self._read_viewport_resource()
        raise ValueError(f"未知资源 URI: {uri_text}")

    def invalidate_viewport_cache(self) -> None:
        self._viewport_cache = None

    async def notify_resource_updated(self, session: Any, uri: str) -> None:
        if uri.startswith(VIEWPORT_RESOURCE_URI):
            self.invalidate_viewport_cache()

        if session is None:
            return

        sender = getattr(session, "send_resource_updated", None)
        if sender is None:
            return

        await sender(_as_any_url(uri))

    async def notify_default_resources_changed(self, session: Any) -> None:
        for uri in DEFAULT_RESOURCE_URIS:
            await self.notify_resource_updated(session, uri)

    async def _read_scene_resource(self) -> list[ReadResourceContents]:
        scene = await self._backend.get_scene()
        payload = json.dumps(scene, ensure_ascii=False, indent=2)
        return [ReadResourceContents(content=payload, mime_type="application/json")]

    async def _read_objects_resource(self) -> list[ReadResourceContents]:
        objects = await self._backend.get_objects()
        payload = json.dumps(objects, ensure_ascii=False, indent=2)
        return [ReadResourceContents(content=payload, mime_type="application/json")]

    async def _read_viewport_resource(self) -> list[ReadResourceContents]:
        now = datetime.now(timezone.utc)
        if self._viewport_cache and self._viewport_cache.expires_at > now:
            return list(self._viewport_cache.contents)

        viewport_payload = await self._backend.capture_viewport()
        image_bytes, mime_type = self._normalize_viewport_payload(viewport_payload)
        contents = [ReadResourceContents(content=image_bytes, mime_type=mime_type)]

        self._viewport_cache = _ViewportCacheEntry(
            contents=contents,
            expires_at=now + timedelta(seconds=self._viewport_cache_ttl_seconds),
        )
        return list(contents)

    def _normalize_viewport_payload(self, payload: Mapping[str, Any] | str | bytes) -> tuple[bytes, str]:
        if isinstance(payload, bytes):
            return payload, "image/png"

        if isinstance(payload, str):
            return self._decode_base64(payload), "image/png"

        mime_type = str(payload.get("mimeType") or payload.get("mime_type") or "image/png")
        image_data = payload.get("image_base64") or payload.get("image") or payload.get("data")

        if isinstance(image_data, bytes):
            return image_data, mime_type

        if isinstance(image_data, str):
            return self._decode_base64(image_data), mime_type

        raise ValueError("视口资源返回格式无效：缺少 image_base64/image/data")

    def _decode_base64(self, data: str) -> bytes:
        normalized = data.strip()
        if normalized.startswith("data:") and "," in normalized:
            normalized = normalized.split(",", maxsplit=1)[1]
        try:
            return base64.b64decode(normalized, validate=False)
        except ValueError as error:
            raise ValueError("视口图片内容不是有效 Base64") from error
