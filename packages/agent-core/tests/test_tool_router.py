"""Tests for ToolRouter."""

import pytest

from blender_agent_core.router import ToolRouter


def test_map_to_engine():
    """Test mapping tool call to engine request."""
    router = ToolRouter()

    request = router.map_to_engine("create_object", {"name": "Cube", "type": "MESH"})

    assert request.capability == "blender_create_object"
    assert request.payload["name"] == "Cube"
    assert request.payload["type"] == "MESH"


def test_map_unknown_tool():
    """Test mapping unknown tool raises error."""
    router = ToolRouter()

    with pytest.raises(ValueError, match="Unknown tool"):
        router.map_to_engine("unknown_tool", {})


def test_is_valid_tool():
    """Test tool validation."""
    router = ToolRouter()

    assert router.is_valid_tool("create_object") is True
    assert router.is_valid_tool("get_scene") is True
    assert router.is_valid_tool("unknown_tool") is False


def test_list_tools():
    """Test listing available tools."""
    router = ToolRouter()

    tools = router.list_tools()

    assert len(tools) > 0
    assert "create_object" in tools
    assert "get_scene" in tools
