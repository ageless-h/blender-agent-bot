from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import uuid4


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


@dataclass(slots=True)
class StoredMessage:
    message_id: str
    session_id: str
    role: str
    content: str
    created_at: datetime = field(default_factory=_utcnow)
    metadata: dict[str, Any] = field(default_factory=dict)


class MessageStore:
    """对话消息存储：默认内存，支持 JSONL 持久化。"""

    def __init__(self, *, persist_file: str | Path | None = None) -> None:
        self.persist_file = Path(persist_file) if persist_file else None
        self._session_messages: dict[str, list[StoredMessage]] = {}
        if self.persist_file and self.persist_file.exists():
            self._load_from_disk()

    def add_message(
        self,
        *,
        session_id: str,
        role: str,
        content: str,
        metadata: dict[str, Any] | None = None,
    ) -> StoredMessage:
        message = StoredMessage(
            message_id=uuid4().hex,
            session_id=session_id,
            role=role,
            content=content,
            metadata=metadata or {},
        )
        self._session_messages.setdefault(session_id, []).append(message)
        if self.persist_file:
            self._append_to_disk(message)
        return message

    def list_messages(self, session_id: str, *, limit: int | None = None) -> list[StoredMessage]:
        messages = self._session_messages.get(session_id, [])
        if limit is None:
            return list(messages)
        return list(messages[-limit:])

    def clear_session(self, session_id: str) -> None:
        self._session_messages.pop(session_id, None)
        if self.persist_file:
            self._rewrite_disk()

    def dump(self) -> dict[str, Any]:
        return {
            session_id: [self._to_jsonable(msg) for msg in messages]
            for session_id, messages in self._session_messages.items()
        }

    def _append_to_disk(self, message: StoredMessage) -> None:
        if self.persist_file is None:
            return
        self.persist_file.parent.mkdir(parents=True, exist_ok=True)
        with self.persist_file.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(self._to_jsonable(message), ensure_ascii=False) + "\n")

    def _rewrite_disk(self) -> None:
        if self.persist_file is None:
            return
        self.persist_file.parent.mkdir(parents=True, exist_ok=True)
        with self.persist_file.open("w", encoding="utf-8") as handle:
            for messages in self._session_messages.values():
                for message in messages:
                    handle.write(json.dumps(self._to_jsonable(message), ensure_ascii=False) + "\n")

    def _load_from_disk(self) -> None:
        if self.persist_file is None or not self.persist_file.exists():
            return
        with self.persist_file.open("r", encoding="utf-8") as handle:
            for line in handle:
                payload = line.strip()
                if not payload:
                    continue
                try:
                    data = json.loads(payload)
                except json.JSONDecodeError:
                    continue
                session_id = str(data.get("session_id", ""))
                if not session_id:
                    continue
                created_at_raw = data.get("created_at")
                try:
                    created_at = (
                        datetime.fromisoformat(created_at_raw) if isinstance(created_at_raw, str) else _utcnow()
                    )
                except ValueError:
                    created_at = _utcnow()
                message = StoredMessage(
                    message_id=str(data.get("message_id", uuid4().hex)),
                    session_id=session_id,
                    role=str(data.get("role", "user")),
                    content=str(data.get("content", "")),
                    created_at=created_at,
                    metadata=dict(data.get("metadata", {})),
                )
                self._session_messages.setdefault(session_id, []).append(message)

    def _to_jsonable(self, message: StoredMessage) -> dict[str, Any]:
        return {
            "message_id": message.message_id,
            "session_id": message.session_id,
            "role": message.role,
            "content": message.content,
            "created_at": message.created_at.isoformat(),
            "metadata": message.metadata,
        }
