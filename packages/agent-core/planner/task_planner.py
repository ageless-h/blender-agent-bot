from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class ToolInvocation:
    name: str
    arguments: dict[str, Any] = field(default_factory=dict)
    risk: str = "low"
    retry: int = 0


@dataclass(slots=True)
class PlanStep:
    index: int
    description: str
    calls: list[ToolInvocation] = field(default_factory=list)
    fallback: str | None = None


@dataclass(slots=True)
class PlannedTask:
    user_intent: str
    steps: list[PlanStep]
    metadata: dict[str, Any] = field(default_factory=dict)


class TaskPlanner:
    """将自然语言指令拆解为可执行工具调用序列。"""

    def __init__(self, *, max_retry: int = 2) -> None:
        self.max_retry = max_retry

    def plan(self, user_intent: str) -> PlannedTask:
        normalized_intent = user_intent.strip()
        if not normalized_intent:
            return PlannedTask(user_intent=user_intent, steps=[])

        pieces = self._split_intent(normalized_intent)
        steps: list[PlanStep] = []
        for index, piece in enumerate(pieces, start=1):
            calls = self._plan_piece(piece)
            steps.append(
                PlanStep(
                    index=index,
                    description=piece,
                    calls=calls,
                    fallback="回退到最近一次场景快照",
                )
            )

        return PlannedTask(
            user_intent=user_intent,
            steps=steps,
            metadata={"step_count": len(steps), "planner": "heuristic-v1"},
        )

    def rebuild_after_failure(
        self,
        task: PlannedTask,
        *,
        failed_step_index: int,
        error: str,
    ) -> PlannedTask:
        rebuilt_steps: list[PlanStep] = []
        for step in task.steps:
            if step.index != failed_step_index:
                rebuilt_steps.append(step)
                continue

            retried_calls = [
                ToolInvocation(
                    name=call.name,
                    arguments={**call.arguments, "_retry_reason": error},
                    risk=call.risk,
                    retry=min(call.retry + 1, self.max_retry),
                )
                for call in step.calls
            ]
            rebuilt_steps.append(
                PlanStep(
                    index=step.index,
                    description=f"{step.description}（失败重试）",
                    calls=retried_calls,
                    fallback=step.fallback,
                )
            )

        metadata = dict(task.metadata)
        metadata["last_error"] = error
        metadata["replanned_step"] = failed_step_index
        return PlannedTask(user_intent=task.user_intent, steps=rebuilt_steps, metadata=metadata)

    def _split_intent(self, user_intent: str) -> list[str]:
        separators = ["然后", "并且", "并", "，", ",", " and then ", " then "]
        parts = [user_intent]
        for separator in separators:
            next_parts: list[str] = []
            for part in parts:
                if separator in part:
                    next_parts.extend([item.strip() for item in part.split(separator) if item.strip()])
                else:
                    next_parts.append(part.strip())
            parts = next_parts
        return [part for part in parts if part]

    def _plan_piece(self, piece: str) -> list[ToolInvocation]:
        text = piece.lower()

        if "小屋" in piece or "house" in text:
            return [
                ToolInvocation(
                    name="create_primitive",
                    arguments={"type": "cube", "name": "house_body", "size": 2.0},
                    risk="medium",
                ),
                ToolInvocation(
                    name="create_primitive",
                    arguments={"type": "cone", "name": "house_roof", "radius": 1.6, "depth": 1.2},
                    risk="medium",
                ),
                ToolInvocation(
                    name="align_objects",
                    arguments={"base": "house_body", "target": "house_roof", "mode": "stack_top"},
                    risk="low",
                ),
            ]

        if "材质" in piece or "material" in text:
            return [
                ToolInvocation(
                    name="set_material",
                    arguments={"target": "selected", "preset": "default_pbr"},
                    risk="low",
                )
            ]

        if "删除" in piece or "delete" in text:
            return [
                ToolInvocation(
                    name="delete_object",
                    arguments={"target": "selected"},
                    risk="high",
                )
            ]

        return [
            ToolInvocation(
                name="run_nl_action",
                arguments={"instruction": piece},
                risk="low",
            )
        ]
