from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Any, Mapping, TypeVar
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field

MessageModelT = TypeVar("MessageModelT", bound="BaseMessage")


class MessageType(str, Enum):
    CHAT = "chat"
    TOOL_CALL = "tool_call"
    TOOL_RESULT = "tool_result"
    ERROR = "error"
    STREAM_CHUNK = "stream_chunk"
    CONFIRM_REQUEST = "confirm_request"
    CONFIRM_RESPONSE = "confirm_response"


class BaseMessage(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    type: MessageType
    metadata: dict[str, Any] = Field(default_factory=dict)

    model_config = ConfigDict(extra="forbid")

    def to_dict(self) -> dict[str, Any]:
        if hasattr(self, "model_dump"):
            return self.model_dump(mode="json")
        return self.dict()

    def to_json(self) -> str:
        if hasattr(self, "model_dump_json"):
            return self.model_dump_json()
        return self.json()

    @classmethod
    def from_dict(cls: type[MessageModelT], payload: Mapping[str, Any]) -> MessageModelT:
        if hasattr(cls, "model_validate"):
            return cls.model_validate(payload)
        return cls.parse_obj(payload)

    @classmethod
    def from_json(cls: type[MessageModelT], payload: str) -> MessageModelT:
        if hasattr(cls, "model_validate_json"):
            return cls.model_validate_json(payload)
        return cls.parse_raw(payload)


__all__ = [
    "MessageType",
    "BaseMessage",
]
