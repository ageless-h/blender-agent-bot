from __future__ import annotations

import importlib

bl_info = {
    "name": "BlenderAgentBot Frontend",
    "author": "BlenderAgentBot",
    "version": (0, 1, 0),
    "blender": (4, 2, 0),
    "location": "View3D > Sidebar > BlenderAgent",
    "description": "Blender 内置 AI 聊天前端，支持预览确认与安全撤销",
    "warning": "",
    "category": "3D View",
}


try:
    bpy = importlib.import_module("bpy")
except ModuleNotFoundError:
    bpy = None


if bpy is not None:
    _bpy = bpy
    BoolProperty = _bpy.props.BoolProperty
    CollectionProperty = _bpy.props.CollectionProperty
    EnumProperty = _bpy.props.EnumProperty
    FloatProperty = _bpy.props.FloatProperty
    IntProperty = _bpy.props.IntProperty
    StringProperty = _bpy.props.StringProperty

    from .bridge import RuntimeSettings, get_runtime, stop_runtime
    from .operators import OPERATOR_CLASSES
    from .panels import PANEL_CLASSES

    class BLENDERAGENT_PG_message(_bpy.types.PropertyGroup):
        """聊天消息记录。"""

        message_id = StringProperty(name="消息ID", default="")
        role = EnumProperty(
            name="角色",
            items=[
                ("USER", "User", "用户消息"),
                ("ASSISTANT", "Assistant", "AI 消息"),
                ("SYSTEM", "System", "系统消息"),
            ],
            default="SYSTEM",
        )
        content = StringProperty(name="内容", default="")
        created_at = StringProperty(name="时间", default="")
        preview_path = StringProperty(name="截图路径", subtype="FILE_PATH", default="")
        action_id = StringProperty(name="动作ID", default="")
        can_undo = BoolProperty(name="可撤销", default=False)
        is_streaming = BoolProperty(name="流式中", default=False)
        undo_steps = IntProperty(name="撤销步数", default=0, min=0)

    class BLENDERAGENT_PG_pending_action(_bpy.types.PropertyGroup):
        """待确认执行的动作。"""

        action_id = StringProperty(name="动作ID", default="")
        summary = StringProperty(name="摘要", default="")
        payload = StringProperty(name="动作参数", default="")
        safety_level = EnumProperty(
            name="安全等级",
            items=[
                ("CONSERVATIVE", "保守", "仅低风险操作"),
                ("STANDARD", "标准", "平衡安全与效率"),
                ("ADVANCED", "高级", "允许更复杂的操作"),
            ],
            default="STANDARD",
        )
        status = EnumProperty(
            name="状态",
            items=[
                ("PENDING", "待确认", "等待用户确认"),
                ("APPROVED", "已确认", "已确认并执行"),
                ("REJECTED", "已拒绝", "已被用户拒绝"),
            ],
            default="PENDING",
        )

    class BLENDERAGENT_PG_undo_entry(_bpy.types.PropertyGroup):
        """AI 操作撤销映射。"""

        action_id = StringProperty(name="动作ID", default="")
        message_id = StringProperty(name="消息ID", default="")
        undo_steps = IntProperty(name="撤销步数", default=1, min=1)
        is_active = BoolProperty(name="是否有效", default=True)

    class BLENDERAGENT_AP_preferences(_bpy.types.AddonPreferences):
        """Addon 偏好配置。"""

        bl_idname = (__package__ or __name__).split(".")[0]

        api_key = StringProperty(
            name="API Key",
            description="云端模型 API Key（安全存储在 Blender 偏好中）",
            default="",
            subtype="PASSWORD",
        )
        default_model = StringProperty(
            name="默认模型",
            description="插件启动时默认使用的模型名",
            default="claude-sonnet-4.5",
        )
        auto_start_core = BoolProperty(
            name="启用时自动启动 Agent Core",
            description="在启用插件时自动拉起 Agent Core 子进程",
            default=True,
        )
        auto_restart_core = BoolProperty(
            name="异常退出自动重启",
            description="当 Agent Core 进程异常退出时自动重启",
            default=True,
        )
        max_restart_attempts = IntProperty(
            name="最大重启次数",
            description="自动重启的最大尝试次数，0 表示不限制",
            default=3,
            min=0,
            soft_max=10,
        )
        restart_backoff_seconds = FloatProperty(
            name="重启退避秒数",
            description="每次自动重启前等待秒数",
            default=1.0,
            min=0.0,
            max=30.0,
        )
        agent_command = StringProperty(
            name="Agent Core 启动命令",
            description="留空则使用默认命令或 BLENDERAGENT_CORE_CMD 环境变量",
            default="",
        )

        def draw(self, _context):
            layout = self.layout
            layout.label(text="BlenderAgent Frontend 偏好设置", icon="PREFERENCES")
            layout.prop(self, "api_key")
            layout.prop(self, "default_model")
            layout.prop(self, "agent_command")
            layout.prop(self, "auto_start_core")
            layout.prop(self, "auto_restart_core")
            layout.prop(self, "max_restart_attempts")
            layout.prop(self, "restart_backoff_seconds")

    CORE_CLASSES = (
        BLENDERAGENT_PG_message,
        BLENDERAGENT_PG_pending_action,
        BLENDERAGENT_PG_undo_entry,
        BLENDERAGENT_AP_preferences,
    )
    ALL_CLASSES = CORE_CLASSES + OPERATOR_CLASSES + PANEL_CLASSES

    _SCENE_PROPERTIES = [
        "blenderagent_messages",
        "blenderagent_message_index",
        "blenderagent_input_text",
        "blenderagent_is_generating",
        "blenderagent_last_command",
        "blenderagent_history_offset",
        "blenderagent_model_source",
        "blenderagent_model_name",
        "blenderagent_local_endpoint",
        "blenderagent_security_level",
        "blenderagent_persona_template",
        "blenderagent_bridge_status",
        "blenderagent_last_error",
        "blenderagent_pending_actions",
        "blenderagent_pending_action_index",
        "blenderagent_undo_stack",
        "blenderagent_undo_stack_index",
        "blenderagent_preview_progress",
        "blenderagent_action_edit_payload",
        "blenderagent_high_risk_confirm_id",
        "blenderagent_ai_undo_depth",
        "blenderagent_reference_image_path",
        "blenderagent_reference_image_name",
    ]

    def _addon_key() -> str:
        package_name = (__package__ or "").split(".")[0]
        return package_name or __name__.split(".")[0]

    def _resolve_preferences():
        context = getattr(_bpy, "context", None)
        if context is None:
            return None

        preferences = getattr(context, "preferences", None)
        if preferences is None:
            return None

        addon = preferences.addons.get(_addon_key())
        if addon is None:
            return None
        return addon.preferences

    def _register_scene_properties() -> None:
        scene = _bpy.types.Scene

        scene.blenderagent_messages = CollectionProperty(type=BLENDERAGENT_PG_message)
        scene.blenderagent_message_index = IntProperty(name="消息索引", default=-1, min=-1)
        scene.blenderagent_input_text = StringProperty(name="输入", default="")
        scene.blenderagent_is_generating = BoolProperty(name="生成中", default=False)
        scene.blenderagent_last_command = StringProperty(name="上一条指令", default="")
        scene.blenderagent_history_offset = IntProperty(name="历史偏移", default=0, min=0)

        scene.blenderagent_model_source = EnumProperty(
            name="模型来源",
            items=[
                ("CLOUD", "云端", "通过云端 API 调用"),
                ("LOCAL", "本地", "通过本地推理服务调用"),
            ],
            default="CLOUD",
        )
        scene.blenderagent_model_name = StringProperty(name="模型", default="claude-sonnet-4.5")
        scene.blenderagent_local_endpoint = StringProperty(
            name="本地端点",
            default="http://127.0.0.1:11434/v1",
        )

        scene.blenderagent_security_level = EnumProperty(
            name="安全等级",
            items=[
                ("CONSERVATIVE", "保守", "优先安全"),
                ("STANDARD", "标准", "默认策略"),
                ("ADVANCED", "高级", "允许更复杂操作"),
            ],
            default="STANDARD",
        )
        scene.blenderagent_persona_template = EnumProperty(
            name="角色模板",
            items=[
                ("architect", "Architect", "建筑可视化"),
                ("character", "Character", "角色建模"),
                ("game_assets", "Game Assets", "游戏资产"),
                ("beginner", "Beginner", "新手教学"),
            ],
            default="architect",
        )

        scene.blenderagent_bridge_status = StringProperty(name="Bridge 状态", default="DISCONNECTED")
        scene.blenderagent_last_error = StringProperty(name="最近错误", default="")

        scene.blenderagent_pending_actions = CollectionProperty(type=BLENDERAGENT_PG_pending_action)
        scene.blenderagent_pending_action_index = IntProperty(name="预览索引", default=-1, min=-1)
        scene.blenderagent_undo_stack = CollectionProperty(type=BLENDERAGENT_PG_undo_entry)
        scene.blenderagent_undo_stack_index = IntProperty(name="撤销栈索引", default=-1, min=-1)
        scene.blenderagent_preview_progress = FloatProperty(
            name="执行进度",
            default=0.0,
            min=0.0,
            max=100.0,
            subtype="PERCENTAGE",
        )
        scene.blenderagent_action_edit_payload = StringProperty(name="动作修改参数", default="")
        scene.blenderagent_high_risk_confirm_id = StringProperty(name="高风险确认动作ID", default="")
        scene.blenderagent_ai_undo_depth = IntProperty(name="AI 撤销深度", default=0, min=0)
        scene.blenderagent_reference_image_path = StringProperty(
            name="参考图",
            default="",
            subtype="FILE_PATH",
        )
        scene.blenderagent_reference_image_name = StringProperty(name="参考图名", default="")

    def _unregister_scene_properties() -> None:
        scene = _bpy.types.Scene
        for property_name in _SCENE_PROPERTIES:
            if hasattr(scene, property_name):
                delattr(scene, property_name)

    def _runtime_settings_from_preferences() -> tuple[RuntimeSettings, bool]:
        preferences = _resolve_preferences()

        command: str | None = None
        env_overrides: dict[str, str] = {}
        auto_start = True
        auto_restart = True
        max_restart_attempts = 3
        restart_backoff_seconds = 1.0

        if preferences is not None:
            raw_command = str(getattr(preferences, "agent_command", "")).strip()
            if raw_command:
                command = raw_command

            api_key = str(getattr(preferences, "api_key", "")).strip()
            if api_key:
                env_overrides["BLENDERAGENT_API_KEY"] = api_key

            # Handle Blender property deferred loading
            auto_start_val = getattr(preferences, "auto_start_core", True)
            auto_start = bool(auto_start_val) if not isinstance(auto_start_val, type(lambda: None)) else True

            auto_restart_val = getattr(preferences, "auto_restart_core", True)
            auto_restart = bool(auto_restart_val) if not isinstance(auto_restart_val, type(lambda: None)) else True

            max_restart_val = getattr(preferences, "max_restart_attempts", 3)
            try:
                max_restart_attempts = int(max_restart_val)
            except (TypeError, ValueError):
                max_restart_attempts = 3

            restart_backoff_val = getattr(preferences, "restart_backoff_seconds", 1.0)
            try:
                restart_backoff_seconds = float(restart_backoff_val)
            except (TypeError, ValueError):
                restart_backoff_seconds = 1.0

        return (
            RuntimeSettings(
                command=command,
                env_overrides=env_overrides,
                auto_restart=auto_restart,
                max_restart_attempts=max_restart_attempts,
                restart_backoff_seconds=restart_backoff_seconds,
            ),
            auto_start,
        )

    def _sync_bridge_status() -> None:
        status = get_runtime().status()
        data = getattr(_bpy, "data", None)
        scenes = getattr(data, "scenes", None)
        if scenes is None:
            return
        for scene in scenes:
            if hasattr(scene, "blenderagent_bridge_status"):
                scene.blenderagent_bridge_status = status

    def register() -> None:
        if _bpy.app.version < (4, 2, 0):
            raise RuntimeError("BlenderAgentBot Frontend 仅支持 Blender 4.2+。")

        for cls in ALL_CLASSES:
            _bpy.utils.register_class(cls)

        _register_scene_properties()

        settings, auto_start = _runtime_settings_from_preferences()
        if auto_start:
            try:
                get_runtime().start(settings)
            except Exception as exc:
                print(f"[BlenderAgent] Agent Core 自动启动失败: {exc}")
                context = getattr(_bpy, "context", None)
                scene = getattr(context, "scene", None)
                if scene is not None and hasattr(scene, "blenderagent_last_error"):
                    scene.blenderagent_last_error = str(exc)

        _sync_bridge_status()

    def unregister() -> None:
        stop_runtime()

        _unregister_scene_properties()

        for cls in reversed(ALL_CLASSES):
            _bpy.utils.unregister_class(cls)

else:

    def register() -> None:
        raise RuntimeError("当前环境缺少 bpy，仅可在 Blender 内启用 frontend-blender 插件。")

    def unregister() -> None:
        return None


__all__ = ["bl_info", "register", "unregister"]
