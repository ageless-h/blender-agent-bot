from __future__ import annotations

import importlib
import os
from pathlib import Path

from ..bridge import get_runtime

bpy = importlib.import_module("bpy")


ROLE_ICON = {
    "USER": "USER",
    "ASSISTANT": "OUTLINER_OB_LIGHT",
    "SYSTEM": "INFO",
}

ROLE_LABEL = {
    "USER": "你",
    "ASSISTANT": "AI",
    "SYSTEM": "系统",
}


def _trim_message(text: str, max_length: int = 92) -> str:
    cleaned = (text or "").replace("\n", " ").strip()
    if len(cleaned) <= max_length:
        return cleaned
    return f"{cleaned[:max_length]}..."


def _visible_message_window(scene, page_size: int = 10) -> tuple[int, int]:
    total = len(scene.blenderagent_messages)
    if total <= 0:
        return 0, 0

    max_offset = max(total - page_size, 0)
    offset = min(max(scene.blenderagent_history_offset, 0), max_offset)
    scene.blenderagent_history_offset = offset

    end = total - offset
    start = max(end - page_size, 0)
    return start, end


def _draw_image_thumbnail(layout, image_path: str, *, label: str, scale: float = 4.0) -> None:
    resolved_path = str(image_path or "").strip()
    if not resolved_path:
        return

    if resolved_path.startswith("//"):
        try:
            resolved_path = bpy.path.abspath(resolved_path)
        except Exception:
            pass

    box = layout.box()
    box.label(text=label, icon="IMAGE_DATA")

    try:
        if os.path.exists(resolved_path):
            image = bpy.data.images.load(resolved_path, check_existing=True)
            icon_value = image.preview.icon_id if image.preview is not None else 0
            if icon_value:
                box.template_icon(icon_value=icon_value, scale=scale)
            box.label(text=Path(resolved_path).name)
            return
    except Exception:
        pass

    box.label(text=resolved_path)


def _draw_reference_preview(layout, scene) -> None:
    image_name = str(scene.blenderagent_reference_image_name or "").strip()
    if image_name:
        image = bpy.data.images.get(image_name)
        if image is not None:
            preview_box = layout.box()
            preview_box.label(text="参考图预览", icon="IMAGE_DATA")
            icon_value = image.preview.icon_id if image.preview is not None else 0
            if icon_value:
                preview_box.template_icon(icon_value=icon_value, scale=5.0)
            preview_box.label(text=image.name)
            return

    _draw_image_thumbnail(layout, scene.blenderagent_reference_image_path, label="参考图预览", scale=5.0)


class BLENDERAGENT_PT_chat(bpy.types.Panel):
    """主聊天面板。"""

    bl_idname = "BLENDERAGENT_PT_chat"
    bl_label = "AI Chat"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "BlenderAgent"
    bl_order = 0

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        runtime = get_runtime()

        status_row = layout.row(align=True)
        status_row.prop(scene, "blenderagent_model_name", text="模型")

        is_connected = runtime.is_connected()
        status_icon = "CHECKMARK" if is_connected else "ERROR"
        status_text = "已连接" if is_connected else "未连接"
        status_row.label(text=status_text, icon=status_icon)

        toolbar = layout.row(align=True)
        toolbar.operator("blenderagent.send_message", text="发送", icon="PLAY")
        toolbar.operator("blenderagent.stop_generation", text="", icon="CANCEL")
        toolbar.operator("blenderagent.retry_last", text="", icon="FILE_REFRESH")
        toolbar.operator("blenderagent.clear_history", text="", icon="TRASH")

        layout.prop(scene, "blenderagent_input_text", text="")

        reference_row = layout.row(align=True)
        reference_row.prop(scene, "blenderagent_reference_image_path", text="参考图")
        reference_row.operator("blenderagent.pick_reference_image", text="", icon="FILE_FOLDER")
        reference_row.operator("blenderagent.apply_reference_image", text="", icon="FILE_TICK")
        reference_row.operator("blenderagent.paste_reference_image", text="", icon="PASTEDOWN")
        reference_row.operator("blenderagent.clear_reference_image", text="", icon="X")

        if scene.blenderagent_reference_image_path:
            _draw_reference_preview(layout, scene)

        if scene.blenderagent_is_generating:
            layout.label(text="AI 正在生成中...", icon="TIME")

        history_row = layout.row(align=True)
        up_operator = history_row.operator("blenderagent.shift_history", text="", icon="TRIA_UP")
        up_operator.delta = -1
        down_operator = history_row.operator("blenderagent.shift_history", text="", icon="TRIA_DOWN")
        down_operator.delta = 1
        history_row.label(text=f"历史偏移: {scene.blenderagent_history_offset}")

        messages = scene.blenderagent_messages
        if len(messages) <= 0:
            layout.label(text="还没有消息，输入内容开始对话。", icon="TEXT")
        else:
            start, end = _visible_message_window(scene)
            list_box = layout.box()

            for index in range(start, end):
                message = messages[index]
                role = str(message.role)
                icon = ROLE_ICON.get(role, "DOT")
                role_label = ROLE_LABEL.get(role, "消息")

                msg_box = list_box.box()
                header = msg_box.row(align=True)
                header.label(text=f"{role_label} · {message.created_at}", icon=icon)

                if message.is_streaming:
                    header.label(text="生成中", icon="TIME")

                content_row = msg_box.row()
                content_row.label(text=_trim_message(message.content))

                if message.preview_path:
                    _draw_image_thumbnail(msg_box, message.preview_path, label="截图预览", scale=3.0)

                action_row = msg_box.row(align=True)
                copy_operator = action_row.operator("blenderagent.copy_message", text="复制", icon="COPYDOWN")
                copy_operator.message_id = message.message_id

                if role == "ASSISTANT" and message.can_undo:
                    undo_operator = action_row.operator("blenderagent.undo_action", text="撤销", icon="LOOP_BACK")
                    undo_operator.message_id = message.message_id

        if scene.blenderagent_last_error:
            layout.separator()
            error_box = layout.box()
            error_box.label(text="最近错误", icon="ERROR")
            error_box.label(text=_trim_message(scene.blenderagent_last_error, max_length=120))


CHAT_PANEL_CLASSES = (BLENDERAGENT_PT_chat,)


__all__ = ["BLENDERAGENT_PT_chat", "CHAT_PANEL_CLASSES"]
