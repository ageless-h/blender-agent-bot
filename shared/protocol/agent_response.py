from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from ..agent_types.tool_types import SafetyLevel, ToolCall
from .messages import BaseMessage, MessageType


class ResponseStatus(str, Enum):
    SUCCESS = "success"
    FAILED = "failed"
    NEEDS_CONFIRM = "needs_confirm"


class ScreenshotRef(BaseModel):
    data_base64: str
    mime_type: str = "image/png"

    model_config = ConfigDict(extra="forbid")


class AgentResponse(BaseMessage):
    type: MessageType = MessageType.CHAT
    session_id: str
    message: str
    tool_calls: list[ToolCall] = Field(default_factory=list)
    screenshots: list[ScreenshotRef] = Field(default_factory=list)
    status: ResponseStatus = ResponseStatus.SUCCESS
    error: str | None = None


class StreamChunk(BaseMessage):
    type: MessageType = MessageType.STREAM_CHUNK
    session_id: str
    delta: str = ""
    tool_call_delta: ToolCall | None = None
    done: bool = False


class ConfirmRequest(BaseMessage):
    type: MessageType = MessageType.CONFIRM_REQUEST
    session_id: str
    request_id: str
    message: str
    safety_level: SafetyLevel = SafetyLevel.LEVEL_2
    operation: dict[str, Any] = Field(default_factory=dict)
    expires_in_seconds: int | None = None


__all__ = [
    "AgentResponse",
    "StreamChunk",
    "ConfirmRequest",
    "ResponseStatus",
    "ScreenshotRef",
]
