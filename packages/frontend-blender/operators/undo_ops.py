from __future__ import annotations

import importlib

from .chat_ops import (
    add_chat_message,
    deactivate_undo_entry,
    get_latest_undo_entry,
    get_message_by_id,
    get_undo_entry,
)

bpy = importlib.import_module("bpy")
StringProperty = bpy.props.StringProperty


def _find_latest_undoable_message(scene):
    for index in range(len(scene.blenderagent_messages) - 1, -1, -1):
        message = scene.blenderagent_messages[index]
        if message.can_undo:
            return message
    return None


class BLENDERAGENT_OT_undo_action(bpy.types.Operator):
    """撤销指定 AI 消息关联的操作。"""

    bl_idname = "blenderagent.undo_action"
    bl_label = "撤销 AI 操作"
    bl_description = "撤销该条 AI 操作对应的 Blender 变更"
    bl_options = {"REGISTER"}

    message_id = StringProperty(name="消息ID", default="")

    def execute(self, context):
        scene = context.scene

        message = None
        undo_entry = None

        if self.message_id:
            message = get_message_by_id(scene, self.message_id)
            undo_entry = get_undo_entry(scene, message_id=self.message_id)

        if undo_entry is None and message is not None and message.action_id:
            undo_entry = get_undo_entry(scene, action_id=message.action_id)

        if undo_entry is None:
            undo_entry = get_latest_undo_entry(scene)
            if undo_entry is not None:
                message = get_message_by_id(scene, undo_entry.message_id)

        if message is None:
            message = _find_latest_undoable_message(scene)

        if message is None and undo_entry is None:
            self.report({"WARNING"}, "没有可撤销的 AI 操作。")
            return {"CANCELLED"}

        steps = max(int(undo_entry.undo_steps), 1) if undo_entry is not None else max(int(message.undo_steps), 1)
        finished_steps = 0

        for _ in range(steps):
            result = bpy.ops.ed.undo()
            if "FINISHED" not in result:
                break
            finished_steps += 1

        if finished_steps <= 0:
            self.report({"WARNING"}, "撤销失败，当前状态不可回退。")
            return {"CANCELLED"}

        if message is not None:
            message.can_undo = False
            message.undo_steps = 0

        if undo_entry is not None:
            deactivate_undo_entry(scene, message_id=undo_entry.message_id)

        scene.blenderagent_ai_undo_depth = max(scene.blenderagent_ai_undo_depth - finished_steps, 0)
        add_chat_message(scene, role="SYSTEM", content=f"已撤销 {finished_steps} 步 AI 操作。")

        return {"FINISHED"}


class BLENDERAGENT_OT_undo_all(bpy.types.Operator):
    """撤销所有由 AI 触发的历史操作。"""

    bl_idname = "blenderagent.undo_all"
    bl_label = "撤销全部 AI 操作"
    bl_description = "回退到 AI 操作前状态"
    bl_options = {"REGISTER"}

    def execute(self, context):
        scene = context.scene
        active_entries = [entry for entry in scene.blenderagent_undo_stack if entry.is_active]
        planned_steps = sum(int(entry.undo_steps) for entry in active_entries)
        if planned_steps <= 0:
            self.report({"INFO"}, "当前没有 AI 操作需要撤销。")
            return {"CANCELLED"}

        finished_steps = 0
        for _ in range(planned_steps):
            result = bpy.ops.ed.undo()
            if "FINISHED" not in result:
                break
            finished_steps += 1

        scene.blenderagent_ai_undo_depth = max(scene.blenderagent_ai_undo_depth - finished_steps, 0)

        for entry in active_entries:
            entry.is_active = False
            linked_message = get_message_by_id(scene, entry.message_id)
            if linked_message is not None:
                linked_message.can_undo = False
                linked_message.undo_steps = 0

        add_chat_message(scene, role="SYSTEM", content=f"已完成批量撤销，共回退 {finished_steps} 步。")
        self.report({"INFO"}, f"已撤销 {finished_steps} 步。")
        return {"FINISHED"}


UNDO_OPERATOR_CLASSES = (
    BLENDERAGENT_OT_undo_action,
    BLENDERAGENT_OT_undo_all,
)


__all__ = [
    "BLENDERAGENT_OT_undo_action",
    "BLENDERAGENT_OT_undo_all",
    "UNDO_OPERATOR_CLASSES",
]
