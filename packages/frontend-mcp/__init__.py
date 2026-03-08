try:
    from .config import (
        GeneratedConfig,
        MCPServerCommand,
        SetupGenerator,
        detect_python_executable,
        generate_setup_config,
    )
    from .server import (
        DEFAULT_RESOURCE_URIS,
        DEFAULT_TOOL_SPECS,
        OBJECTS_RESOURCE_URI,
        SCENE_RESOURCE_URI,
        VIEWPORT_RESOURCE_URI,
        MCPFrontendServer,
        ResourceProvider,
        ToolProvider,
    )
except ImportError:
    from config import (
        GeneratedConfig,
        MCPServerCommand,
        SetupGenerator,
        detect_python_executable,
        generate_setup_config,
    )
    from server import (
        DEFAULT_RESOURCE_URIS,
        DEFAULT_TOOL_SPECS,
        OBJECTS_RESOURCE_URI,
        SCENE_RESOURCE_URI,
        VIEWPORT_RESOURCE_URI,
        MCPFrontendServer,
        ResourceProvider,
        ToolProvider,
    )

__all__ = [
    "DEFAULT_RESOURCE_URIS",
    "DEFAULT_TOOL_SPECS",
    "GeneratedConfig",
    "MCPFrontendServer",
    "MCPServerCommand",
    "OBJECTS_RESOURCE_URI",
    "SCENE_RESOURCE_URI",
    "VIEWPORT_RESOURCE_URI",
    "ResourceProvider",
    "SetupGenerator",
    "ToolProvider",
    "detect_python_executable",
    "generate_setup_config",
]
