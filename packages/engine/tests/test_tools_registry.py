from __future__ import annotations

from packages.engine.tools import build_default_registry


def test_default_registry_contains_26_tools() -> None:
    registry = build_default_registry()
    tools = registry.list_tools()
    names = {item.name for item in tools}

    assert len(tools) == 26
    assert "get_objects" in names
    assert "edit_nodes" in names
    assert "create_object" in names
    assert "execute_script" in names


def test_registry_unknown_tool_returns_error() -> None:
    registry = build_default_registry()
    result = registry.execute("missing_tool", {})

    assert not result.success
    assert result.error is not None
