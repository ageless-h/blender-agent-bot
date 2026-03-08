from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


@dataclass(slots=True)
class HistoryMessage:
    role: str
    content: str
    created_at: datetime = field(default_factory=_utcnow)
    metadata: dict[str, Any] = field(default_factory=dict)


class HistoryManager:
    """对话历史管理（滑动窗口 + 摘要压缩）。"""

    def __init__(self, *, window_size: int = 24, summary_trigger: int = 36) -> None:
        self.window_size = window_size
        self.summary_trigger = summary_trigger
        self._messages: list[HistoryMessage] = []
        self._summary: str = ""

    def append(self, role: str, content: str, metadata: dict[str, Any] | None = None) -> None:
        self._messages.append(HistoryMessage(role=role, content=content, metadata=metadata or {}))
        if len(self._messages) > self.summary_trigger:
            self._compress_history()

    def get_recent_messages(self, *, limit: int | None = None) -> list[HistoryMessage]:
        size = limit or self.window_size
        return self._messages[-size:]

    def get_context(self) -> list[dict[str, str]]:
        context: list[dict[str, str]] = []
        if self._summary:
            context.append({"role": "system", "content": f"历史摘要:\n{self._summary}"})
        context.extend(
            {"role": msg.role, "content": msg.content} for msg in self.get_recent_messages(limit=self.window_size)
        )
        return context

    def clear(self) -> None:
        self._messages.clear()
        self._summary = ""

    def export_state(self) -> dict[str, Any]:
        return {
            "summary": self._summary,
            "messages": [
                {
                    "role": msg.role,
                    "content": msg.content,
                    "created_at": msg.created_at.isoformat(),
                    "metadata": msg.metadata,
                }
                for msg in self._messages
            ],
        }

    def restore_state(self, state: dict[str, Any]) -> None:
        self._summary = str(state.get("summary", ""))
        restored: list[HistoryMessage] = []
        for item in state.get("messages", []):
            created_at = item.get("created_at")
            try:
                parsed_time = datetime.fromisoformat(created_at) if isinstance(created_at, str) else _utcnow()
            except ValueError:
                parsed_time = _utcnow()
            restored.append(
                HistoryMessage(
                    role=str(item.get("role", "user")),
                    content=str(item.get("content", "")),
                    created_at=parsed_time,
                    metadata=dict(item.get("metadata", {})),
                )
            )
        self._messages = restored

    def _compress_history(self) -> None:
        overflow = len(self._messages) - self.window_size
        if overflow <= 0:
            return

        old_messages = self._messages[:overflow]
        self._messages = self._messages[overflow:]

        snippets = []
        for msg in old_messages:
            compact = msg.content.strip().replace("\n", " ")
            if len(compact) > 80:
                compact = f"{compact[:77]}..."
            snippets.append(f"[{msg.role}] {compact}")

        merged = "\n".join(snippets)
        self._summary = f"{self._summary}\n{merged}".strip() if self._summary else merged
