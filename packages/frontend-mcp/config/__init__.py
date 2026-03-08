from __future__ import annotations

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .setup_generator import (
        GeneratedConfig,
        MCPServerCommand,
        SetupGenerator,
        detect_python_executable,
        generate_setup_config,
    )

__all__ = [
    "GeneratedConfig",
    "MCPServerCommand",
    "SetupGenerator",
    "detect_python_executable",
    "generate_setup_config",
]

_ATTRIBUTE_MODULE_MAP = {
    "GeneratedConfig": ".setup_generator",
    "MCPServerCommand": ".setup_generator",
    "SetupGenerator": ".setup_generator",
    "detect_python_executable": ".setup_generator",
    "generate_setup_config": ".setup_generator",
}


def __getattr__(name: str) -> Any:
    module_name = _ATTRIBUTE_MODULE_MAP.get(name)
    if module_name is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    module = import_module(module_name, __name__)
    return getattr(module, name)


def __dir__() -> list[str]:
    return sorted(set(globals()) | set(__all__))
