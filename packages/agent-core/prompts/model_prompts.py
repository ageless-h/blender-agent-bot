from __future__ import annotations


MODEL_PROMPTS: dict[str, str] = {
    "claude": "强调长上下文推理，优先输出可验证步骤和风险提示。",
    "gpt": "强调工具调用参数完整性，尽量并行工具执行。",
    "gemini": "强调多模态与长上下文，优先给出结构化 JSON。",
    "local": "上下文有限，优先简洁计划并减少无关历史。",
}


def resolve_model_prompt(model_name: str) -> str:
    lowered = model_name.lower()
    if "claude" in lowered:
        return MODEL_PROMPTS["claude"]
    if "gpt" in lowered or "o1" in lowered or "o3" in lowered:
        return MODEL_PROMPTS["gpt"]
    if "gemini" in lowered:
        return MODEL_PROMPTS["gemini"]
    return MODEL_PROMPTS["local"]


def build_model_layer_prompt(model_name: str, base_prompt: str) -> str:
    model_hint = resolve_model_prompt(model_name)
    return f"{base_prompt}\n\n[模型特化策略]\n{model_hint}".strip()
