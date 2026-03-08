from __future__ import annotations

import pytest
from server.tool_provider import ToolExecutionError, ToolProvider


def test_list_tools_contains_all_26_specs() -> None:
    provider = ToolProvider()
    tools = provider.list_tools()

    assert len(tools) == 26
    names = {tool.name for tool in tools}
    assert "get_objects" in names
    assert "capture_viewport" in names
    assert "execute_script" in names


@pytest.mark.asyncio
async def test_capture_viewport_returns_image_content() -> None:
    provider = ToolProvider()
    contents = await provider.call_tool("capture_viewport", {"format": "png"})

    image_items = [item for item in contents if getattr(item, "type", "") == "image"]
    assert image_items
    assert image_items[0].mimeType == "image/png"


@pytest.mark.asyncio
async def test_unknown_tool_raises_error() -> None:
    provider = ToolProvider()
    with pytest.raises(ToolExecutionError):
        await provider.call_tool("tool_not_exists", {})
