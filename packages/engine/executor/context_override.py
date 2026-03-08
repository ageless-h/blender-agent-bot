from __future__ import annotations

from contextlib import contextmanager, nullcontext
from typing import Any, Iterator


def get_bpy() -> Any | None:
    try:
        import bpy  # type: ignore

        return bpy
    except Exception:
        return None


def blender_version(bpy_module: Any | None = None) -> tuple[int, int, int]:
    bpy = bpy_module or get_bpy()
    if bpy is None:
        return (0, 0, 0)
    version = bpy.app.version
    return (int(version[0]), int(version[1]), int(version[2]))


def find_view3d_context(bpy_module: Any | None = None) -> dict[str, Any] | None:
    bpy = bpy_module or get_bpy()
    if bpy is None:
        return None

    windows = getattr(bpy.context.window_manager, "windows", [])
    for window in windows:
        screen = window.screen
        for area in screen.areas:
            if area.type != "VIEW_3D":
                continue
            region = next((item for item in area.regions if item.type == "WINDOW"), None)
            if region is None:
                continue
            return {
                "window": window,
                "screen": screen,
                "area": area,
                "region": region,
            }
    return None


@contextmanager
def view3d_override(bpy_module: Any | None = None) -> Iterator[Any]:
    bpy = bpy_module or get_bpy()
    if bpy is None:
        with nullcontext(None):
            yield None
        return

    override = find_view3d_context(bpy)
    if override is None:
        with nullcontext(bpy.context):
            yield bpy.context
        return

    supports_temp_override = hasattr(bpy.context, "temp_override")
    if supports_temp_override:
        with bpy.context.temp_override(**override):
            yield bpy.context
        return

    with nullcontext(bpy.context):
        yield bpy.context
