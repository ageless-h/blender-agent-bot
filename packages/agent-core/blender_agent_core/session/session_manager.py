from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping


@dataclass(slots=True)
class Session:
    """In-memory session state used by Agent Core."""

    session_id: str
    history: list[dict[str, Any]] = field(default_factory=list)
    context: dict[str, Any] = field(default_factory=dict)

    def add_history(self, entry: Mapping[str, Any]) -> None:
        self.history.append(dict(entry))


class SessionManager:
    """Create, fetch, and delete isolated in-memory sessions."""

    def __init__(self) -> None:
        self._sessions: dict[str, Session] = {}

    def create_session(self, session_id: str, context: Mapping[str, Any] | None = None) -> Session:
        """Create a new session for the given session ID."""

        if session_id in self._sessions:
            raise ValueError(f"session already exists: {session_id}")

        session = Session(session_id=session_id, context=dict(context or {}))
        self._sessions[session_id] = session
        return session

    def get_session(self, session_id: str) -> Session | None:
        """Return the session for ``session_id`` when it exists."""

        return self._sessions.get(session_id)

    def delete_session(self, session_id: str) -> bool:
        """Delete a session and report whether one was removed."""

        return self._sessions.pop(session_id, None) is not None
