from __future__ import annotations

import json
import importlib
import os
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any

from ..bridge import RuntimeSettings, get_runtime

bpy = importlib.import_module("bpy")
IntProperty = bpy.props.IntProperty
StringProperty = bpy.props.StringProperty


ROLE_ITEMS = {
    "USER": "用户",
    "ASSISTANT": "AI",
    "SYSTEM": "系统",
}

SUPPORTED_IMAGE_SUFFIXES = {
    ".png",
    ".jpg",
    ".jpeg",
    ".bmp",
    ".tga",
    ".tif",
    ".tiff",
    ".webp",
    ".exr",
    ".hdr",
}


def _addon_key() -> str:
    package_name = (__package__ or "").split(".")[0]
    return package_name or __name__.split(".")[0]


def _resolve_preferences(context):
    addon = context.preferences.addons.get(_addon_key())
    if addon is None:
        return None
    return addon.preferences


def _runtime_settings_from_preferences(context) -> RuntimeSettings:
    preferences = _resolve_preferences(context)
    env_overrides: dict[str, str] = {}
    command: str | None = None
    auto_restart = True
    max_restart_attempts = 3
    restart_backoff_seconds = 1.0

    if preferences is not None:
        api_key = str(getattr(preferences, "api_key", "")).strip()
        if api_key:
            env_overrides["BLENDERAGENT_API_KEY"] = api_key

        preferred_command = str(getattr(preferences, "agent_command", "")).strip()
        if preferred_command:
            command = preferred_command

        auto_restart = bool(getattr(preferences, "auto_restart_core", True))
        max_restart_attempts = int(getattr(preferences, "max_restart_attempts", 3))
        restart_backoff_seconds = float(getattr(preferences, "restart_backoff_seconds", 1.0))

    return RuntimeSettings(
        command=command,
        env_overrides=env_overrides,
        auto_restart=auto_restart,
        max_restart_attempts=max_restart_attempts,
        restart_backoff_seconds=restart_backoff_seconds,
    )


def _current_timestamp() -> str:
    return datetime.now().strftime("%H:%M:%S")


def _refresh_view3d(context) -> None:
    window_manager = getattr(context, "window_manager", None)
    if window_manager is None:
        return

    for window in window_manager.windows:
        screen = getattr(window, "screen", None)
        if screen is None:
            continue
        for area in screen.areas:
            if area.type == "VIEW_3D":
                area.tag_redraw()


def _normalize_file_path(raw_path: str) -> str:
    candidate = str(raw_path or "").strip()
    if not candidate:
        return ""

    if candidate.startswith("//"):
        try:
            candidate = bpy.path.abspath(candidate)
        except Exception:
            pass

    expanded = Path(candidate).expanduser()
    return str(expanded)


def _is_supported_image(path: str) -> bool:
    suffix = Path(path).suffix.lower()
    return suffix in SUPPORTED_IMAGE_SUFFIXES


def assign_reference_image(scene, raw_path: str) -> tuple[bool, str]:
    normalized_path = _normalize_file_path(raw_path)
    if not normalized_path:
        scene.blenderagent_reference_image_name = ""
        scene.blenderagent_reference_image_path = ""
        return False, "参考图路径为空。"

    if not _is_supported_image(normalized_path):
        return False, "参考图格式不受支持。"

    if not os.path.exists(normalized_path):
        return False, "参考图文件不存在。"

    try:
        image = bpy.data.images.load(normalized_path, check_existing=True)
    except Exception as exc:
        return False, f"参考图加载失败: {exc}"

    scene.blenderagent_reference_image_path = normalized_path
    scene.blenderagent_reference_image_name = image.name
    return True, "参考图已加载。"


def _collect_scene_context(context) -> dict[str, Any]:
    scene = context.scene
    selected_object_names = [obj.name for obj in context.selected_objects]

    active_object = None
    active_ref = context.view_layer.objects.active
    if active_ref is not None:
        active_object = active_ref.name

    editor_type = "UNKNOWN"
    if context.area is not None:
        editor_type = context.area.type

    return {
        "scene_name": scene.name,
        "selected_objects": selected_object_names,
        "active_object": active_object,
        "active_editor": editor_type,
    }


def add_chat_message(
    scene,
    *,
    role: str,
    content: str,
    preview_path: str = "",
    action_id: str = "",
    can_undo: bool = False,
    is_streaming: bool = False,
    undo_steps: int = 0,
) -> str:
    message = scene.blenderagent_messages.add()
    message.message_id = uuid.uuid4().hex
    message.role = role if role in ROLE_ITEMS else "SYSTEM"
    message.content = content
    message.created_at = _current_timestamp()
    message.preview_path = preview_path
    message.action_id = action_id
    message.can_undo = can_undo
    message.is_streaming = is_streaming
    message.undo_steps = max(undo_steps, 0)

    scene.blenderagent_message_index = len(scene.blenderagent_messages) - 1
    return message.message_id


def push_undo_entry(
    scene,
    *,
    action_id: str,
    message_id: str,
    undo_steps: int,
) -> None:
    stack_entry = scene.blenderagent_undo_stack.add()
    stack_entry.action_id = action_id
    stack_entry.message_id = message_id
    stack_entry.undo_steps = max(1, int(undo_steps))
    stack_entry.is_active = True
    scene.blenderagent_undo_stack_index = len(scene.blenderagent_undo_stack) - 1


def get_undo_entry(scene, *, message_id: str = "", action_id: str = ""):
    if message_id:
        for entry in scene.blenderagent_undo_stack:
            if entry.is_active and entry.message_id == message_id:
                return entry

    if action_id:
        for entry in scene.blenderagent_undo_stack:
            if entry.is_active and entry.action_id == action_id:
                return entry

    return None


def get_latest_undo_entry(scene):
    for index in range(len(scene.blenderagent_undo_stack) - 1, -1, -1):
        entry = scene.blenderagent_undo_stack[index]
        if entry.is_active:
            return entry
    return None


def deactivate_undo_entry(scene, *, message_id: str = "", action_id: str = "") -> int:
    disabled_count = 0
    for entry in scene.blenderagent_undo_stack:
        if not entry.is_active:
            continue

        matched = False
        if message_id and entry.message_id == message_id:
            matched = True
        if action_id and entry.action_id == action_id:
            matched = True

        if matched:
            entry.is_active = False
            disabled_count += 1

    return disabled_count


def get_message_by_id(scene, message_id: str):
    for message in scene.blenderagent_messages:
        if message.message_id == message_id:
            return message
    return None


def mark_message_as_undoable(scene, message_id: str, undo_steps: int = 1) -> None:
    target = get_message_by_id(scene, message_id)
    if target is None:
        return

    target.can_undo = True
    target.undo_steps = max(undo_steps, 1)


def _update_message_content(
    scene,
    *,
    message_id: str,
    content: str,
    is_streaming: bool,
) -> None:
    target = get_message_by_id(scene, message_id)
    if target is None:
        return

    target.content = content
    target.is_streaming = is_streaming


def _set_bridge_status(scene) -> None:
    runtime = get_runtime()
    scene.blenderagent_bridge_status = runtime.status()


def _apply_pending_actions(scene, actions: list[dict[str, Any]]) -> None:
    scene.blenderagent_pending_actions.clear()

    for action in actions:
        pending = scene.blenderagent_pending_actions.add()
        pending.action_id = str(action.get("action_id") or uuid.uuid4().hex)
        pending.summary = str(action.get("summary") or action.get("name") or "未命名操作")
        pending.safety_level = str(action.get("safety_level") or "STANDARD").upper()
        pending.payload = json.dumps(action, ensure_ascii=False, separators=(",", ":"))
        pending.status = "PENDING"

    scene.blenderagent_pending_action_index = 0 if scene.blenderagent_pending_actions else -1


class BLENDERAGENT_OT_send_message(bpy.types.Operator):
    """发送用户消息到 Agent Core。"""

    bl_idname = "blenderagent.send_message"
    bl_label = "发送消息"
    bl_description = "发送当前输入并请求 AI 响应"
    bl_options = {"REGISTER"}

    def execute(self, context) -> set[str]:
        scene = context.scene
        text = scene.blenderagent_input_text.strip()
        if not text:
            self.report({"WARNING"}, "请输入消息后再发送。")
            return {"CANCELLED"}

        if scene.blenderagent_reference_image_path:
            image_ok, image_message = assign_reference_image(scene, scene.blenderagent_reference_image_path)
            if not image_ok:
                scene.blenderagent_last_error = image_message
                self.report({"WARNING"}, image_message)
                return {"CANCELLED"}

        scene.blenderagent_last_error = ""
        scene.blenderagent_last_command = text
        add_chat_message(scene, role="USER", content=text)

        assistant_message_id = add_chat_message(
            scene,
            role="ASSISTANT",
            content="",
            is_streaming=True,
        )
        scene.blenderagent_input_text = ""
        scene.blenderagent_is_generating = True

        runtime = get_runtime()

        try:
            if not runtime.is_connected():
                runtime.start(_runtime_settings_from_preferences(context))

            _set_bridge_status(scene)

            request_payload = {
                "type": "chat",
                "message": text,
                "context": _collect_scene_context(context),
                "reference_image": scene.blenderagent_reference_image_path,
                "security_level": scene.blenderagent_security_level.lower(),
                "persona": scene.blenderagent_persona_template,
                "model": {
                    "source": scene.blenderagent_model_source.lower(),
                    "name": scene.blenderagent_model_name,
                    "local_endpoint": scene.blenderagent_local_endpoint,
                },
            }

            def on_stream(token: str, _raw: dict[str, Any]) -> None:
                current = get_message_by_id(scene, assistant_message_id)
                if current is None:
                    return
                current.content = f"{current.content}{token}"
                current.is_streaming = True
                _refresh_view3d(context)

            response = runtime.send_request(request_payload, timeout=60.0, on_stream=on_stream)

            content = str(response.get("content") or response.get("message") or "").strip()
            if not content:
                content = "已收到请求，但 Agent Core 没有返回文本内容。"

            actions = response.get("actions")
            if isinstance(actions, list):
                normalized_actions: list[dict[str, Any]] = []
                for action in actions:
                    if isinstance(action, dict):
                        normalized_actions.append(action)
                _apply_pending_actions(scene, normalized_actions)
                scene.blenderagent_preview_progress = 100.0 if normalized_actions else 0.0
            else:
                scene.blenderagent_preview_progress = 0.0

            _update_message_content(
                scene,
                message_id=assistant_message_id,
                content=content,
                is_streaming=False,
            )
        except Exception as exc:
            error_text = f"请求失败: {exc}"
            scene.blenderagent_last_error = error_text
            _update_message_content(
                scene,
                message_id=assistant_message_id,
                content=error_text,
                is_streaming=False,
            )
            self.report({"ERROR"}, error_text)
        finally:
            scene.blenderagent_is_generating = False
            _set_bridge_status(scene)
            _refresh_view3d(context)

        return {"FINISHED"}


class BLENDERAGENT_OT_clear_history(bpy.types.Operator):
    """清空聊天历史和预览队列。"""

    bl_idname = "blenderagent.clear_history"
    bl_label = "清空历史"
    bl_description = "清空消息记录和待确认操作"
    bl_options = {"REGISTER"}

    def execute(self, context) -> set[str]:
        scene = context.scene
        scene.blenderagent_messages.clear()
        scene.blenderagent_pending_actions.clear()
        scene.blenderagent_undo_stack.clear()
        scene.blenderagent_message_index = -1
        scene.blenderagent_pending_action_index = -1
        scene.blenderagent_undo_stack_index = -1
        scene.blenderagent_preview_progress = 0.0
        scene.blenderagent_history_offset = 0
        scene.blenderagent_ai_undo_depth = 0
        scene.blenderagent_is_generating = False
        scene.blenderagent_last_error = ""
        self.report({"INFO"}, "聊天历史已清空。")
        return {"FINISHED"}


class BLENDERAGENT_OT_copy_message(bpy.types.Operator):
    """复制指定消息内容。"""

    bl_idname = "blenderagent.copy_message"
    bl_label = "复制消息"
    bl_description = "复制消息到系统剪贴板"

    message_id = StringProperty(name="消息ID", default="")

    def execute(self, context) -> set[str]:
        scene = context.scene
        target_message = get_message_by_id(scene, self.message_id)
        if target_message is None:
            self.report({"WARNING"}, "未找到要复制的消息。")
            return {"CANCELLED"}

        context.window_manager.clipboard = target_message.content
        self.report({"INFO"}, "已复制到剪贴板。")
        return {"FINISHED"}


class BLENDERAGENT_OT_retry_last(bpy.types.Operator):
    """重试上一条用户指令。"""

    bl_idname = "blenderagent.retry_last"
    bl_label = "重试上一条"
    bl_description = "重新发送上一条用户消息"
    bl_options = {"REGISTER"}

    def execute(self, context) -> set[str]:
        scene = context.scene
        last_command = scene.blenderagent_last_command.strip()
        if not last_command:
            self.report({"WARNING"}, "没有可重试的上一条指令。")
            return {"CANCELLED"}

        scene.blenderagent_input_text = last_command
        result = bpy.ops.blenderagent.send_message("EXEC_DEFAULT")
        if "FINISHED" in result:
            return {"FINISHED"}
        return {"CANCELLED"}


class BLENDERAGENT_OT_stop_generation(bpy.types.Operator):
    """停止当前生成请求。"""

    bl_idname = "blenderagent.stop_generation"
    bl_label = "停止生成"
    bl_description = "取消当前进行中的 AI 请求"
    bl_options = {"REGISTER"}

    def execute(self, context) -> set[str]:
        scene = context.scene
        runtime = get_runtime()
        runtime.cancel_all_requests()
        scene.blenderagent_is_generating = False

        for message in scene.blenderagent_messages:
            if message.is_streaming:
                message.is_streaming = False

        self.report({"INFO"}, "已请求停止当前生成。")
        _refresh_view3d(context)
        return {"FINISHED"}


class BLENDERAGENT_OT_restart_bridge(bpy.types.Operator):
    """重启 Agent Core 子进程。"""

    bl_idname = "blenderagent.restart_bridge"
    bl_label = "重连 Agent Core"
    bl_description = "停止并重新启动 Agent Core 子进程"
    bl_options = {"REGISTER"}

    def execute(self, context) -> set[str]:
        scene = context.scene
        runtime = get_runtime()

        try:
            runtime.restart(_runtime_settings_from_preferences(context))
            _set_bridge_status(scene)
            scene.blenderagent_last_error = ""
            self.report({"INFO"}, "Agent Core 已重连。")
            return {"FINISHED"}
        except Exception as exc:
            scene.blenderagent_last_error = str(exc)
            _set_bridge_status(scene)
            self.report({"ERROR"}, f"重连失败: {exc}")
            return {"CANCELLED"}


class BLENDERAGENT_OT_shift_history(bpy.types.Operator):
    """滚动查看历史消息。"""

    bl_idname = "blenderagent.shift_history"
    bl_label = "滚动历史"
    bl_description = "向上或向下滚动聊天历史"

    delta = IntProperty(name="偏移增量", default=0)

    def execute(self, context) -> set[str]:
        scene = context.scene
        total_messages = len(scene.blenderagent_messages)
        max_offset = max(total_messages - 1, 0)

        next_offset = scene.blenderagent_history_offset + self.delta
        scene.blenderagent_history_offset = min(max(next_offset, 0), max_offset)
        return {"FINISHED"}


class BLENDERAGENT_OT_apply_reference_image(bpy.types.Operator):
    """加载并应用参考图路径。"""

    bl_idname = "blenderagent.apply_reference_image"
    bl_label = "应用参考图"
    bl_description = "加载参考图并生成缩略预览"
    bl_options = {"REGISTER"}

    def execute(self, context) -> set[str]:
        scene = context.scene
        success, message = assign_reference_image(scene, scene.blenderagent_reference_image_path)
        if not success:
            self.report({"WARNING"}, message)
            return {"CANCELLED"}

        self.report({"INFO"}, message)
        _refresh_view3d(context)
        return {"FINISHED"}


class BLENDERAGENT_OT_paste_reference_image(bpy.types.Operator):
    """从剪贴板粘贴参考图路径。"""

    bl_idname = "blenderagent.paste_reference_image"
    bl_label = "粘贴截图"
    bl_description = "从系统剪贴板粘贴图片路径并加载"
    bl_options = {"REGISTER"}

    def execute(self, context) -> set[str]:
        scene = context.scene
        clipboard_text = str(context.window_manager.clipboard or "").strip()
        if not clipboard_text:
            self.report({"WARNING"}, "剪贴板为空，无法粘贴参考图。")
            return {"CANCELLED"}

        scene.blenderagent_reference_image_path = clipboard_text
        success, message = assign_reference_image(scene, clipboard_text)
        if not success:
            self.report({"WARNING"}, message)
            return {"CANCELLED"}

        self.report({"INFO"}, message)
        _refresh_view3d(context)
        return {"FINISHED"}


class BLENDERAGENT_OT_clear_reference_image(bpy.types.Operator):
    """清空参考图。"""

    bl_idname = "blenderagent.clear_reference_image"
    bl_label = "清空参考图"
    bl_description = "清空当前参考图路径和预览"
    bl_options = {"REGISTER"}

    def execute(self, context) -> set[str]:
        scene = context.scene
        scene.blenderagent_reference_image_path = ""
        scene.blenderagent_reference_image_name = ""
        self.report({"INFO"}, "已清空参考图。")
        _refresh_view3d(context)
        return {"FINISHED"}


class BLENDERAGENT_OT_pick_reference_image(bpy.types.Operator):
    """打开文件选择器选择参考图。"""

    bl_idname = "blenderagent.pick_reference_image"
    bl_label = "选择参考图"
    bl_description = "通过文件选择器加载参考图"
    bl_options = {"REGISTER"}

    filepath = StringProperty(name="文件路径", subtype="FILE_PATH", default="")

    def invoke(self, context, _event):
        context.window_manager.fileselect_add(self)
        return {"RUNNING_MODAL"}

    def execute(self, context) -> set[str]:
        scene = context.scene
        success, message = assign_reference_image(scene, self.filepath)
        if not success:
            self.report({"WARNING"}, message)
            return {"CANCELLED"}

        self.report({"INFO"}, message)
        _refresh_view3d(context)
        return {"FINISHED"}


CHAT_OPERATOR_CLASSES = (
    BLENDERAGENT_OT_send_message,
    BLENDERAGENT_OT_clear_history,
    BLENDERAGENT_OT_copy_message,
    BLENDERAGENT_OT_retry_last,
    BLENDERAGENT_OT_stop_generation,
    BLENDERAGENT_OT_restart_bridge,
    BLENDERAGENT_OT_shift_history,
    BLENDERAGENT_OT_apply_reference_image,
    BLENDERAGENT_OT_paste_reference_image,
    BLENDERAGENT_OT_clear_reference_image,
    BLENDERAGENT_OT_pick_reference_image,
)


__all__ = [
    "CHAT_OPERATOR_CLASSES",
    "BLENDERAGENT_OT_send_message",
    "BLENDERAGENT_OT_clear_history",
    "BLENDERAGENT_OT_copy_message",
    "BLENDERAGENT_OT_retry_last",
    "BLENDERAGENT_OT_stop_generation",
    "BLENDERAGENT_OT_restart_bridge",
    "BLENDERAGENT_OT_shift_history",
    "BLENDERAGENT_OT_apply_reference_image",
    "BLENDERAGENT_OT_paste_reference_image",
    "BLENDERAGENT_OT_clear_reference_image",
    "BLENDERAGENT_OT_pick_reference_image",
    "assign_reference_image",
    "add_chat_message",
    "push_undo_entry",
    "get_undo_entry",
    "get_latest_undo_entry",
    "deactivate_undo_entry",
    "get_message_by_id",
    "mark_message_as_undoable",
]
