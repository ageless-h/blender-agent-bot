"""Protocol definitions for BlenderAgentBot."""

from .engine_protocol import (
    CapabilityInfo,
    EngineRequest,
    EngineRequestType,
    EngineResponse,
    EngineResponseStatus,
)
from .messages import BaseMessage, MessageType

# Import agent protocol types with fallback
try:
    from .agent_request import (
        AgentRequest,
        AttachmentRef,
        ConfirmResponse,
        RequestContext,
        RequestOptions,
        ToolCallRequest,
    )
    from .agent_response import (
        AgentResponse,
        ConfirmRequest,
        ResponseStatus,
        ScreenshotRef,
        StreamChunk,
    )
except ImportError:
    # Fallback: define minimal types if agent_types not available
    AgentRequest = None
    AgentResponse = None
    ResponseStatus = None

__all__ = [
    # Engine protocol
    "EngineRequest",
    "EngineResponse",
    "EngineRequestType",
    "EngineResponseStatus",
    "CapabilityInfo",
    # Messages
    "MessageType",
    "BaseMessage",
    # Agent protocol (if available)
    "AgentRequest",
    "AgentResponse",
    "ResponseStatus",
    "StreamChunk",
    "ConfirmRequest",
    "ToolCallRequest",
    "ConfirmResponse",
    "AttachmentRef",
    "RequestContext",
    "RequestOptions",
    "ScreenshotRef",
]
