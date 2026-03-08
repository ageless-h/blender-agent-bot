from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class UndoEvent:
    step_index: int
    reason: str
    created_at: datetime = field(default_factory=datetime.utcnow)


class UndoAwareTracker:
    """追踪用户撤销行为，作为隐式负反馈信号。"""

    def __init__(self) -> None:
        self._events: list[UndoEvent] = []
        self._manual_corrections: dict[int, list[dict[str, Any]]] = {}

    def record_undo(self, *, step_index: int, reason: str = "") -> None:
        self._events.append(UndoEvent(step_index=step_index, reason=reason))

    def record_manual_correction(self, *, step_index: int, correction: dict[str, Any]) -> None:
        self._manual_corrections.setdefault(step_index, []).append(dict(correction))

    def undo_rate(self, *, total_steps: int) -> float:
        if total_steps <= 0:
            return 0.0
        return round(len(self._events) / total_steps, 4)

    def partial_undo_stats(self) -> dict[int, int]:
        stats: dict[int, int] = {}
        for event in self._events:
            stats[event.step_index] = stats.get(event.step_index, 0) + 1
        return stats

    def get_corrections(self, step_index: int) -> list[dict[str, Any]]:
        return list(self._manual_corrections.get(step_index, []))

    def export(self) -> dict[str, Any]:
        return {
            "events": [
                {
                    "step_index": event.step_index,
                    "reason": event.reason,
                    "created_at": event.created_at.isoformat(),
                }
                for event in self._events
            ],
            "manual_corrections": self._manual_corrections,
        }
