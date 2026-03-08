from __future__ import annotations

from typing import Any

from .timers import pending_count


def _get_bpy() -> Any | None:
    try:
        import bpy  # type: ignore

        return bpy
    except Exception:
        return None


bpy = _get_bpy()

if bpy is not None:

    class BlenderAgentPtMain(bpy.types.Panel):
        bl_label = "BlenderAgent"
        bl_idname = "BLENDERAGENT_PT_main"
        bl_space_type = "VIEW_3D"
        bl_region_type = "UI"
        bl_category = "BlenderAgent"

        def draw(self, context: Any) -> None:
            del context
            layout = self.layout
            layout.label(text="Engine 状态")
            layout.label(text=f"待执行命令: {pending_count()}")
            row = layout.row()
            row.operator("blenderagent.execute", text="执行队列命令")

    PANEL_CLASSES = [BlenderAgentPtMain]

else:
    PANEL_CLASSES: list[type[Any]] = []
