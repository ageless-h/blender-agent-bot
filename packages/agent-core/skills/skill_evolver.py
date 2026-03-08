from __future__ import annotations

from dataclasses import dataclass

from .skill_store import SkillRecord
from .undo_tracker import UndoAwareTracker


@dataclass(slots=True)
class EvolverSuggestion:
    step_index: int
    action: str
    reason: str


class SkillEvolver:
    """根据执行反馈自动生成优化建议。"""

    def __init__(self, *, undo_threshold: float = 0.3) -> None:
        self.undo_threshold = undo_threshold

    def suggest(self, skill: SkillRecord, tracker: UndoAwareTracker) -> list[EvolverSuggestion]:
        total_steps = max(len(skill.capsule), 1)
        overall_undo_rate = tracker.undo_rate(total_steps=total_steps)
        step_stats = tracker.partial_undo_stats()

        suggestions: list[EvolverSuggestion] = []
        for step_index, undo_count in step_stats.items():
            per_step_rate = undo_count / total_steps
            if per_step_rate >= self.undo_threshold:
                suggestions.append(
                    EvolverSuggestion(
                        step_index=step_index,
                        action="re_optimize_step",
                        reason=f"step undo_rate={per_step_rate:.2f} 超过阈值 {self.undo_threshold:.2f}",
                    )
                )

        if overall_undo_rate >= self.undo_threshold and not suggestions:
            suggestions.append(
                EvolverSuggestion(
                    step_index=0,
                    action="review_whole_skill",
                    reason=f"整体 undo_rate={overall_undo_rate:.2f} 超过阈值",
                )
            )

        return suggestions

    def apply(self, skill: SkillRecord, suggestions: list[EvolverSuggestion]) -> SkillRecord:
        if not suggestions:
            return skill
        gene = dict(skill.gene)
        gene.setdefault("evolution", [])
        gene["evolution"].extend(
            {
                "step_index": suggestion.step_index,
                "action": suggestion.action,
                "reason": suggestion.reason,
            }
            for suggestion in suggestions
        )
        skill.gene = gene
        return skill
