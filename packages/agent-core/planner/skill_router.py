from __future__ import annotations

from dataclasses import dataclass

from .task_planner import PlannedTask, TaskPlanner
from skills.skill_matcher import SkillMatcher
from skills.skill_store import SkillRecord


@dataclass(slots=True)
class RouteDecision:
    route_type: str
    reason: str
    skill: SkillRecord | None = None
    planned_task: PlannedTask | None = None


class SkillRouter:
    """Skill 优先路由，未命中时回退到 TaskPlanner。"""

    def __init__(
        self,
        *,
        matcher: SkillMatcher | None = None,
        planner: TaskPlanner | None = None,
        min_match_score: float = 0.35,
    ) -> None:
        self.matcher = matcher or SkillMatcher()
        self.planner = planner or TaskPlanner()
        self.min_match_score = min_match_score

    def route(self, user_intent: str, skills: list[SkillRecord]) -> RouteDecision:
        best_match = self.matcher.best_match(
            user_intent,
            skills,
            min_score=self.min_match_score,
        )
        if best_match is not None:
            return RouteDecision(
                route_type="skill",
                reason=f"命中技能: {best_match.skill.skill_id} (score={best_match.score:.2f})",
                skill=best_match.skill,
            )

        planned_task = self.planner.plan(user_intent)
        return RouteDecision(
            route_type="planner",
            reason="未命中技能，使用任务规划器生成执行步骤",
            planned_task=planned_task,
        )
