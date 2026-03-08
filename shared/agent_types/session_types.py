from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field

from .tool_types import ToolCall


class MessageRole(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"
    TOOL = "tool"


class ChatMessage(BaseModel):
    role: MessageRole
    content: str
    tool_calls: list[ToolCall] = Field(default_factory=list)
    screenshots: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    model_config = ConfigDict(extra="forbid")


class Session(BaseModel):
    id: str
    user_id: str | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    messages: list[ChatMessage] = Field(default_factory=list)

    model_config = ConfigDict(extra="forbid")

    def add_message(self, message: ChatMessage) -> None:
        self.messages.append(message)
        self.updated_at = datetime.now(timezone.utc)


__all__ = [
    "Session",
    "ChatMessage",
    "MessageRole",
]
