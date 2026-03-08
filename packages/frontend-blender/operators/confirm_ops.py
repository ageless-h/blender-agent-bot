from __future__ import annotations

import importlib
import json
from typing import Any

from ..bridge import get_runtime
from .chat_ops import add_chat_message, mark_message_as_undoable, push_undo_entry

bpy = importlib.import_module("bpy")
StringProperty = bpy.props.StringProperty


def _find_action_by_id(scene, action_id: str):
    if not action_id:
        index = int(scene.blenderagent_pending_action_index)
        if 0 <= index < len(scene.blenderagent_pending_actions):
            return scene.blenderagent_pending_actions[index], index
        return None, -1

    for index, action in enumerate(scene.blenderagent_pending_actions):
        if action.action_id == action_id:
            return action, index

    return None, -1


def _action_payload(action) -> dict[str, Any]:
    raw_payload = str(action.payload).strip()
    if not raw_payload:
        return {}

    try:
        parsed = json.loads(raw_payload)
    except json.JSONDecodeError:
        return {"raw": raw_payload}

    if isinstance(parsed, dict):
        return parsed
    return {"value": parsed}


def _remove_action(scene, index: int) -> None:
    if not (0 <= index < len(scene.blenderagent_pending_actions)):
        return

    scene.blenderagent_pending_actions.remove(index)

    if len(scene.blenderagent_pending_actions) == 0:
        scene.blenderagent_pending_action_index = -1
    else:
        scene.blenderagent_pending_action_index = min(index, len(scene.blenderagent_pending_actions) - 1)


class BLENDERAGENT_OT_confirm_action(bpy.types.Operator):
    """确认并执行预览动作。"""

    bl_idname = "blenderagent.confirm_action"
    bl_label = "确认执行"
    bl_description = "确认执行当前预览操作"
    bl_options = {"REGISTER", "UNDO"}

    action_id = StringProperty(name="动作ID", default="")

    def execute(self, context):
        scene = context.scene
        action, action_index = _find_action_by_id(scene, self.action_id)
        if action is None:
            self.report({"WARNING"}, "没有找到可确认的操作。")
            return {"CANCELLED"}

        if str(action.safety_level) == "ADVANCED":
            if scene.blenderagent_high_risk_confirm_id != action.action_id:
                scene.blenderagent_high_risk_confirm_id = action.action_id
                self.report({"WARNING"}, "高风险操作，请再次点击“确认”执行。")
                return {"CANCELLED"}
        else:
            scene.blenderagent_high_risk_confirm_id = ""

        scene.blenderagent_preview_progress = 20.0

        payload = _action_payload(action)
        runtime = get_runtime()
        summary = str(action.summary or "未命名操作")
        if not runtime.is_connected():
            self.report({"ERROR"}, "Agent Core 未连接，无法确认执行。")
            scene.blenderagent_preview_progress = 0.0
            return {"CANCELLED"}

        request = {
            "type": "confirm_action",
            "action_id": action.action_id,
            "action": payload,
        }
        try:
            response = runtime.send_request(request, timeout=45.0)
        except Exception as exc:
            scene.blenderagent_last_error = str(exc)
            scene.blenderagent_preview_progress = 0.0
            self.report({"ERROR"}, f"确认执行失败: {exc}")
            return {"CANCELLED"}

        result_text = str(response.get("content") or response.get("message") or "").strip()
        if not result_text:
            result_text = f"已确认执行：{summary}"

        undo_steps = 1
        try:
            undo_steps = max(1, int(response.get("undo_steps", 1)))
        except (TypeError, ValueError):
            undo_steps = 1

        assistant_message_id = add_chat_message(
            scene,
            role="ASSISTANT",
            content=result_text,
            action_id=action.action_id,
            can_undo=True,
            undo_steps=undo_steps,
        )
        mark_message_as_undoable(scene, assistant_message_id, undo_steps=undo_steps)
        push_undo_entry(
            scene,
            action_id=action.action_id,
            message_id=assistant_message_id,
            undo_steps=undo_steps,
        )

        scene.blenderagent_ai_undo_depth += undo_steps
        scene.blenderagent_preview_progress = 100.0

        action.status = "APPROVED"
        _remove_action(scene, action_index)
        scene.blenderagent_high_risk_confirm_id = ""
        scene.blenderagent_preview_progress = 0.0
        return {"FINISHED"}


class BLENDERAGENT_OT_reject_action(bpy.types.Operator):
    """拒绝预览动作。"""

    bl_idname = "blenderagent.reject_action"
    bl_label = "拒绝操作"
    bl_description = "拒绝执行当前预览操作"
    bl_options = {"REGISTER"}

    action_id = StringProperty(name="动作ID", default="")

    def execute(self, context):
        scene = context.scene
        action, action_index = _find_action_by_id(scene, self.action_id)
        if action is None:
            self.report({"WARNING"}, "没有找到可拒绝的操作。")
            return {"CANCELLED"}

        action.status = "REJECTED"
        add_chat_message(scene, role="SYSTEM", content=f"已拒绝操作：{action.summary}")
        if scene.blenderagent_high_risk_confirm_id == action.action_id:
            scene.blenderagent_high_risk_confirm_id = ""
        _remove_action(scene, action_index)
        scene.blenderagent_preview_progress = 0.0

        return {"FINISHED"}


class BLENDERAGENT_OT_modify_action(bpy.types.Operator):
    """修改预览动作参数。"""

    bl_idname = "blenderagent.modify_action"
    bl_label = "修改并保存"
    bl_description = "修改预览操作参数（JSON）"
    bl_options = {"REGISTER"}

    action_id = StringProperty(name="动作ID", default="")
    new_payload = StringProperty(name="新参数", default="")

    def execute(self, context):
        scene = context.scene
        action, _action_index = _find_action_by_id(scene, self.action_id)
        if action is None:
            self.report({"WARNING"}, "没有找到要修改的操作。")
            return {"CANCELLED"}

        candidate = self.new_payload.strip() or scene.blenderagent_action_edit_payload.strip()
        if not candidate:
            self.report({"WARNING"}, "请输入有效的 JSON 参数。")
            return {"CANCELLED"}

        try:
            parsed = json.loads(candidate)
        except json.JSONDecodeError as exc:
            self.report({"ERROR"}, f"JSON 解析失败: {exc}")
            return {"CANCELLED"}

        action.payload = json.dumps(parsed, ensure_ascii=False, separators=(",", ":"))
        action.status = "PENDING"
        if scene.blenderagent_high_risk_confirm_id == action.action_id:
            scene.blenderagent_high_risk_confirm_id = ""

        if isinstance(parsed, dict):
            action.summary = str(parsed.get("summary") or parsed.get("name") or action.summary)
            maybe_safety = str(parsed.get("safety_level") or "").upper()
            if maybe_safety in {"CONSERVATIVE", "STANDARD", "ADVANCED"}:
                action.safety_level = maybe_safety

        scene.blenderagent_action_edit_payload = ""
        add_chat_message(scene, role="SYSTEM", content=f"已更新操作参数：{action.summary}")
        return {"FINISHED"}


CONFIRM_OPERATOR_CLASSES = (
    BLENDERAGENT_OT_confirm_action,
    BLENDERAGENT_OT_reject_action,
    BLENDERAGENT_OT_modify_action,
)


__all__ = [
    "BLENDERAGENT_OT_confirm_action",
    "BLENDERAGENT_OT_reject_action",
    "BLENDERAGENT_OT_modify_action",
    "CONFIRM_OPERATOR_CLASSES",
]
