from __future__ import annotations

from typing import Any, Mapping

import pytest
from server.resource_provider import VIEWPORT_RESOURCE_URI, ResourceProvider

VIEWPORT_SAMPLE_BASE64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQIHWP4z8DwHwAFAAH/l7l8WQAAAABJRU5ErkJggg=="
)


class CountingBackend:
    def __init__(self) -> None:
        self.viewport_calls = 0

    async def get_scene(self) -> Mapping[str, Any]:
        return {"name": "Scene"}

    async def get_objects(self) -> list[Mapping[str, Any]]:
        return [{"name": "Cube"}]

    async def capture_viewport(self) -> Mapping[str, Any]:
        self.viewport_calls += 1
        return {
            "image_base64": VIEWPORT_SAMPLE_BASE64,
            "mimeType": "image/png",
        }


@pytest.mark.asyncio
async def test_viewport_cache_and_invalidation() -> None:
    backend = CountingBackend()
    provider = ResourceProvider(backend=backend, viewport_cache_ttl_seconds=60.0)

    first = await provider.read_resource(VIEWPORT_RESOURCE_URI)
    second = await provider.read_resource(VIEWPORT_RESOURCE_URI)

    assert backend.viewport_calls == 1
    assert len(first) == 1
    assert len(second) == 1
    assert first[0].mime_type == "image/png"

    provider.invalidate_viewport_cache()
    await provider.read_resource(VIEWPORT_RESOURCE_URI)
    assert backend.viewport_calls == 2


@pytest.mark.asyncio
async def test_unknown_resource_raises_value_error() -> None:
    provider = ResourceProvider()
    with pytest.raises(ValueError):
        await provider.read_resource("blender://unknown")
