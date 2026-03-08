from __future__ import annotations

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .mcp_server import MCPFrontendServer
    from .resource_provider import (
        DEFAULT_RESOURCE_URIS,
        OBJECTS_RESOURCE_URI,
        SCENE_RESOURCE_URI,
        VIEWPORT_RESOURCE_URI,
        ResourceProvider,
    )
    from .tool_provider import DEFAULT_TOOL_SPECS, ToolProvider

__all__ = [
    "DEFAULT_RESOURCE_URIS",
    "DEFAULT_TOOL_SPECS",
    "MCPFrontendServer",
    "OBJECTS_RESOURCE_URI",
    "SCENE_RESOURCE_URI",
    "VIEWPORT_RESOURCE_URI",
    "ResourceProvider",
    "ToolProvider",
]

_ATTRIBUTE_MODULE_MAP = {
    "MCPFrontendServer": ".mcp_server",
    "DEFAULT_RESOURCE_URIS": ".resource_provider",
    "OBJECTS_RESOURCE_URI": ".resource_provider",
    "SCENE_RESOURCE_URI": ".resource_provider",
    "VIEWPORT_RESOURCE_URI": ".resource_provider",
    "ResourceProvider": ".resource_provider",
    "DEFAULT_TOOL_SPECS": ".tool_provider",
    "ToolProvider": ".tool_provider",
}


def __getattr__(name: str) -> Any:
    module_name = _ATTRIBUTE_MODULE_MAP.get(name)
    if module_name is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    module = import_module(module_name, __name__)
    return getattr(module, name)


def __dir__() -> list[str]:
    return sorted(set(globals()) | set(__all__))
