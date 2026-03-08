from __future__ import annotations

from dataclasses import dataclass, field


BASE_RULES = [
    "优先保证操作安全与可撤销性",
    "优先复用已有技能，再考虑从零规划",
    "输出结构化步骤，明确工具名与参数",
    "发生错误时先解释原因，再给出恢复动作",
]


@dataclass(slots=True)
class BasePrompt:
    system_role: str = "你是 BlenderAgentBot 的核心执行代理。"
    rules: list[str] = field(default_factory=lambda: list(BASE_RULES))

    def render(
        self,
        *,
        scene_summary: str = "",
        history_summary: str = "",
        capabilities_summary: str = "",
    ) -> str:
        sections = [self.system_role, "", "[工作规则]"]
        sections.extend(f"- {rule}" for rule in self.rules)
        if capabilities_summary:
            sections.extend(["", "[模型能力]", capabilities_summary])
        if scene_summary:
            sections.extend(["", "[场景上下文]", scene_summary])
        if history_summary:
            sections.extend(["", "[历史摘要]", history_summary])
        return "\n".join(sections).strip()
