from __future__ import annotations

import importlib

from ..bridge import get_runtime

bpy = importlib.import_module("bpy")


def _addon_key() -> str:
    package_name = (__package__ or "").split(".")[0]
    return package_name or __name__.split(".")[0]


def _resolve_preferences(context):
    addon = context.preferences.addons.get(_addon_key())
    if addon is None:
        return None
    return addon.preferences


def _consume_bridge_events(scene, runtime) -> None:
    for event in runtime.poll_events(limit=20):
        event_name = str(event.get("event", "")).strip().lower()
        if event_name == "bridge_restarted":
            attempt = event.get("attempt")
            scene.blenderagent_bridge_status = f"RESTARTED({attempt})"
            scene.blenderagent_last_error = ""
        elif event_name == "bridge_parse_error":
            scene.blenderagent_last_error = str(event.get("message") or "Bridge 消息解析失败")


class BLENDERAGENT_PT_settings(bpy.types.Panel):
    """设置面板。"""

    bl_idname = "BLENDERAGENT_PT_settings"
    bl_label = "Settings"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "BlenderAgent"
    bl_order = 1
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        runtime = get_runtime()
        preferences = _resolve_preferences(context)

        _consume_bridge_events(scene, runtime)

        model_box = layout.box()
        model_box.label(text="模型配置", icon="PREFERENCES")
        model_box.prop(scene, "blenderagent_model_source", text="来源")
        model_box.prop(scene, "blenderagent_model_name", text="模型")

        if scene.blenderagent_model_source == "LOCAL":
            model_box.prop(scene, "blenderagent_local_endpoint", text="本地端点")

        safety_box = layout.box()
        safety_box.label(text="执行策略", icon="SHIELD")
        safety_box.prop(scene, "blenderagent_security_level", text="安全等级")
        safety_box.prop(scene, "blenderagent_persona_template", text="角色模板")

        addon_box = layout.box()
        addon_box.label(text="Addon 偏好", icon="TOOL_SETTINGS")
        if preferences is not None:
            addon_box.prop(preferences, "api_key", text="API Key")
            addon_box.prop(preferences, "agent_command", text="Agent 命令")
            addon_box.prop(preferences, "auto_start_core", text="启用时自动启动")
            addon_box.prop(preferences, "auto_restart_core", text="异常退出自动重启")
            addon_box.prop(preferences, "max_restart_attempts", text="最大重启次数")
            addon_box.prop(preferences, "restart_backoff_seconds", text="重启退避秒数")
        else:
            addon_box.label(text="未读取到 Addon 偏好（请确认插件安装名）。", icon="INFO")

        status_box = layout.box()
        status_box.label(text="连接状态", icon="LINKED")

        is_connected = runtime.health_check(auto_recover=True)
        icon = "CHECKMARK" if is_connected else "UNLINKED"
        text = "Agent Core 已连接" if is_connected else "Agent Core 未连接"
        status_box.label(text=text, icon=icon)
        scene.blenderagent_bridge_status = runtime.status()

        status_box.operator("blenderagent.restart_bridge", text="重连 Agent Core", icon="FILE_REFRESH")

        if scene.blenderagent_last_error:
            status_box.label(text=scene.blenderagent_last_error, icon="ERROR")

        logs = runtime.tail_logs(limit=3)
        if logs:
            status_box.separator()
            status_box.label(text="最近日志:", icon="CONSOLE")
            for line in logs:
                status_box.label(text=line[:110])


SETTINGS_PANEL_CLASSES = (BLENDERAGENT_PT_settings,)


__all__ = ["BLENDERAGENT_PT_settings", "SETTINGS_PANEL_CLASSES"]
