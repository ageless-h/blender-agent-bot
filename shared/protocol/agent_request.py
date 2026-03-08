from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from ..agent_types.tool_types import SafetyLevel, ToolCall
from .messages import BaseMessage, MessageType


class AttachmentRef(BaseModel):
    name: str
    mime_type: str = "application/octet-stream"
    uri: str | None = None
    data_base64: str | None = None

    model_config = ConfigDict(extra="forbid")


class RequestContext(BaseModel):
    selected_objects: list[str] = Field(default_factory=list)
    active_object: str | None = None
    scene_excerpt: dict[str, Any] = Field(default_factory=dict)

    model_config = ConfigDict(extra="allow")


class RequestOptions(BaseModel):
    model: str | None = None
    provider: str | None = None
    role: str | None = None
    safety_level: SafetyLevel | None = None
    stream: bool = True
    max_steps: int | None = None

    model_config = ConfigDict(extra="forbid")


class AgentRequest(BaseMessage):
    type: MessageType = MessageType.CHAT
    session_id: str
    message: str
    attachments: list[AttachmentRef] = Field(default_factory=list)
    context: RequestContext = Field(default_factory=RequestContext)
    options: RequestOptions = Field(default_factory=RequestOptions)


class ToolCallRequest(BaseMessage):
    type: MessageType = MessageType.TOOL_CALL
    session_id: str
    tool_call: ToolCall
    require_confirmation: bool = False


class ConfirmResponse(BaseMessage):
    type: MessageType = MessageType.CONFIRM_RESPONSE
    session_id: str
    request_id: str
    approved: bool
    reason: str | None = None


__all__ = [
    "AgentRequest",
    "ToolCallRequest",
    "ConfirmResponse",
    "AttachmentRef",
    "RequestContext",
    "RequestOptions",
]
