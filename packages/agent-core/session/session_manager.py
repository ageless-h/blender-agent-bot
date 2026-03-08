from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any
from uuid import uuid4

from .message_store import MessageStore, StoredMessage


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


@dataclass(slots=True)
class SessionInfo:
    session_id: str
    user_id: str
    created_at: datetime = field(default_factory=_utcnow)
    last_active_at: datetime = field(default_factory=_utcnow)
    config: dict[str, Any] = field(default_factory=dict)


class SessionManager:
    """多用户会话管理器。"""

    def __init__(
        self,
        *,
        timeout_seconds: int = 3_600,
        message_store: MessageStore | None = None,
    ) -> None:
        self.timeout_seconds = timeout_seconds
        self.message_store = message_store or MessageStore()
        self._sessions: dict[str, SessionInfo] = {}

    def create_session(
        self,
        *,
        user_id: str,
        config: dict[str, Any] | None = None,
        session_id: str | None = None,
    ) -> SessionInfo:
        self.cleanup_expired_sessions()
        sid = session_id or uuid4().hex
        session = SessionInfo(session_id=sid, user_id=user_id, config=config or {})
        self._sessions[sid] = session
        return session

    def get_session(self, session_id: str) -> SessionInfo | None:
        session = self._sessions.get(session_id)
        if session is None:
            return None
        if self._is_expired(session):
            self.destroy_session(session_id)
            return None
        session.last_active_at = _utcnow()
        return session

    def list_sessions(self, *, user_id: str | None = None) -> list[SessionInfo]:
        self.cleanup_expired_sessions()
        sessions = list(self._sessions.values())
        if user_id is None:
            return sessions
        return [session for session in sessions if session.user_id == user_id]

    def destroy_session(self, session_id: str) -> None:
        self._sessions.pop(session_id, None)
        self.message_store.clear_session(session_id)

    def cleanup_expired_sessions(self) -> int:
        now = _utcnow()
        expired = [
            session_id
            for session_id, session in self._sessions.items()
            if now - session.last_active_at > timedelta(seconds=self.timeout_seconds)
        ]
        for session_id in expired:
            self.destroy_session(session_id)
        return len(expired)

    def update_config(self, session_id: str, updates: dict[str, Any]) -> dict[str, Any] | None:
        session = self.get_session(session_id)
        if session is None:
            return None
        session.config.update(updates)
        return dict(session.config)

    def add_message(
        self,
        *,
        session_id: str,
        role: str,
        content: str,
        metadata: dict[str, Any] | None = None,
    ) -> StoredMessage:
        session = self.get_session(session_id)
        if session is None:
            raise KeyError(f"session not found or expired: {session_id}")
        return self.message_store.add_message(
            session_id=session_id,
            role=role,
            content=content,
            metadata=metadata,
        )

    def list_messages(self, session_id: str, *, limit: int | None = None) -> list[StoredMessage]:
        session = self.get_session(session_id)
        if session is None:
            return []
        return self.message_store.list_messages(session_id, limit=limit)

    def _is_expired(self, session: SessionInfo) -> bool:
        return _utcnow() - session.last_active_at > timedelta(seconds=self.timeout_seconds)
