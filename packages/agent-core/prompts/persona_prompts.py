from __future__ import annotations


PERSONA_PROMPTS: dict[str, str] = {
    "architect": "偏向建筑可视化：强调比例、结构稳定性和材质分层。",
    "character": "偏向角色建模：强调拓扑、关节变形和细节层次。",
    "game_assets": "偏向游戏资产：强调低面数、LOD 与贴图效率。",
    "beginner": "偏向教学助手：解释每一步原因，避免一次性复杂操作。",
}


def get_persona_prompt(persona: str) -> str:
    key = persona.strip().lower()
    return PERSONA_PROMPTS.get(key, PERSONA_PROMPTS["beginner"])


def build_persona_layer_prompt(base_prompt: str, persona: str) -> str:
    hint = get_persona_prompt(persona)
    return f"{base_prompt}\n\n[角色模板]\n{hint}".strip()
