from __future__ import annotations

import importlib

bpy = importlib.import_module("bpy")


SAFETY_ICON = {
    "CONSERVATIVE": "CHECKMARK",
    "STANDARD": "INFO",
    "ADVANCED": "ERROR",
}

STATUS_LABEL = {
    "PENDING": "待确认",
    "APPROVED": "已确认",
    "REJECTED": "已拒绝",
}


class BLENDERAGENT_UL_pending_actions(bpy.types.UIList):
    """待执行动作列表。"""

    bl_idname = "BLENDERAGENT_UL_pending_actions"

    def draw_item(
        self,
        _context,
        layout,
        _data,
        item,
        _icon,
        _active_data,
        _active_propname,
        _index,
    ):
        safety_level = str(item.safety_level)
        status = str(item.status)
        summary = str(item.summary or "未命名操作")

        icon = SAFETY_ICON.get(safety_level, "QUESTION")
        status_label = STATUS_LABEL.get(status, status)

        if self.layout_type in {"DEFAULT", "COMPACT"}:
            row = layout.row(align=True)
            row.alert = safety_level == "ADVANCED"
            row.label(text=summary, icon=icon)
            row.label(text=status_label)
        elif self.layout_type == "GRID":
            layout.alignment = "CENTER"
            layout.label(text="", icon=icon)


class BLENDERAGENT_PT_preview(bpy.types.Panel):
    """执行预览面板。"""

    bl_idname = "BLENDERAGENT_PT_preview"
    bl_label = "Action Preview"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "BlenderAgent"
    bl_order = 2
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        actions = scene.blenderagent_pending_actions
        active_index = int(scene.blenderagent_pending_action_index)

        layout.template_list(
            "BLENDERAGENT_UL_pending_actions",
            "",
            scene,
            "blenderagent_pending_actions",
            scene,
            "blenderagent_pending_action_index",
            rows=5,
        )

        selected_action = None
        if 0 <= active_index < len(actions):
            selected_action = actions[active_index]

        button_row = layout.row(align=True)
        confirm_operator = button_row.operator("blenderagent.confirm_action", text="确认", icon="CHECKMARK")
        reject_operator = button_row.operator("blenderagent.reject_action", text="拒绝", icon="CANCEL")
        modify_operator = button_row.operator("blenderagent.modify_action", text="修改", icon="GREASEPENCIL")

        if selected_action is not None:
            confirm_operator.action_id = selected_action.action_id
            reject_operator.action_id = selected_action.action_id
            modify_operator.action_id = selected_action.action_id

            detail_box = layout.box()
            detail_box.label(text=f"动作ID: {selected_action.action_id}", icon="DOT")
            safety_row = detail_box.row(align=True)
            safety_row.alert = str(selected_action.safety_level) == "ADVANCED"
            safety_row.label(
                text=f"安全等级: {selected_action.safety_level}",
                icon=SAFETY_ICON.get(str(selected_action.safety_level), "QUESTION"),
            )
            detail_box.label(text=f"状态: {STATUS_LABEL.get(str(selected_action.status), selected_action.status)}")
            detail_box.label(text=str(selected_action.summary))

            layout.prop(scene, "blenderagent_action_edit_payload", text="修改 JSON")
        else:
            layout.label(text="暂无待确认操作。", icon="INFO")

        layout.separator()
        layout.prop(scene, "blenderagent_preview_progress", text="执行进度", slider=True)


PREVIEW_PANEL_CLASSES = (
    BLENDERAGENT_UL_pending_actions,
    BLENDERAGENT_PT_preview,
)


__all__ = [
    "BLENDERAGENT_UL_pending_actions",
    "BLENDERAGENT_PT_preview",
    "PREVIEW_PANEL_CLASSES",
]
