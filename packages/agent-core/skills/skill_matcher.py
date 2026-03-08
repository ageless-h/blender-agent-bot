from __future__ import annotations

import re
from dataclasses import dataclass

from .skill_store import SkillRecord


@dataclass(slots=True)
class SkillMatch:
    skill: SkillRecord
    score: float
    reason: str


class SkillMatcher:
    """根据意图语义和历史成功率进行技能匹配。"""

    def __init__(
        self,
        *,
        keyword_weight: float = 0.6,
        tag_weight: float = 0.2,
        success_weight: float = 0.2,
    ) -> None:
        total = keyword_weight + tag_weight + success_weight
        self.keyword_weight = keyword_weight / total
        self.tag_weight = tag_weight / total
        self.success_weight = success_weight / total

    def match(self, user_intent: str, skills: list[SkillRecord], *, top_k: int = 5) -> list[SkillMatch]:
        intent_tokens = self._tokenize(user_intent)
        intent_token_set = set(intent_tokens)
        matches: list[SkillMatch] = []

        for skill in skills:
            skill_keywords = self._tokenize(
                " ".join([skill.metadata.name, skill.metadata.description, *skill.metadata.tags])
            )
            keyword_score = self._overlap_ratio(intent_token_set, set(skill_keywords))
            tag_score = self._overlap_ratio(intent_token_set, {tag.lower() for tag in skill.metadata.tags})
            success_score = max(0.0, min(skill.metadata.success_rate, 1.0))

            score = (
                keyword_score * self.keyword_weight + tag_score * self.tag_weight + success_score * self.success_weight
            )
            reason = f"keyword={keyword_score:.2f}, tag={tag_score:.2f}, " f"success={success_score:.2f}"
            matches.append(SkillMatch(skill=skill, score=score, reason=reason))

        matches.sort(key=lambda item: item.score, reverse=True)
        return matches[:top_k]

    def best_match(
        self,
        user_intent: str,
        skills: list[SkillRecord],
        *,
        min_score: float = 0.35,
    ) -> SkillMatch | None:
        matches = self.match(user_intent, skills, top_k=1)
        if not matches:
            return None
        if matches[0].score < min_score:
            return None
        return matches[0]

    def _tokenize(self, text: str) -> list[str]:
        normalized = text.lower()
        latin_tokens = re.findall(r"[a-z0-9_]{2,}", normalized)
        cjk_tokens = [token for token in re.findall(r"[\u4e00-\u9fff]{1,}", normalized) if len(token) >= 1]
        return latin_tokens + cjk_tokens

    def _overlap_ratio(self, left: set[str], right: set[str]) -> float:
        if not left or not right:
            return 0.0
        return len(left & right) / len(left)
