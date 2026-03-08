from __future__ import annotations

from typing import Any, Callable

from .operators import OPERATOR_CLASSES, set_executor_callback
from .panels import PANEL_CLASSES
from .timers import register_timer, unregister_timer

bl_info = {
    "name": "BlenderAgentBot Engine",
    "author": "BlenderAgentBot",
    "version": (0, 1, 0),
    "blender": (4, 2, 0),
    "location": "View3D > Sidebar > BlenderAgent",
    "description": "BlenderAgentBot runtime bridge",
    "category": "3D View",
}


def _get_bpy() -> Any | None:
    try:
        import bpy  # type: ignore

        return bpy
    except Exception:
        return None


def register(executor_callback: Callable[[dict[str, Any]], dict[str, Any]] | None = None) -> None:
    bpy = _get_bpy()
    if executor_callback is not None:
        set_executor_callback(executor_callback)

    if bpy is None:
        register_timer()
        return

    for cls in [*OPERATOR_CLASSES, *PANEL_CLASSES]:
        bpy.utils.register_class(cls)
    register_timer()


def unregister() -> None:
    bpy = _get_bpy()
    unregister_timer()

    if bpy is None:
        return

    for cls in reversed([*OPERATOR_CLASSES, *PANEL_CLASSES]):
        try:
            bpy.utils.unregister_class(cls)
        except Exception:
            continue
