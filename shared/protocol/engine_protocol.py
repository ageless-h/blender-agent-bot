"""Engine-level protocol for Blender operations.

This protocol is frontend-agnostic and defines the core interface
between any frontend (MCP, Web, CLI, Blender UI) and the Engine layer.
"""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class EngineRequestType(str, Enum):
    """Type of engine request."""

    EXECUTE_CAPABILITY = "execute_capability"
    LIST_CAPABILITIES = "list_capabilities"
    GET_CAPABILITY_INFO = "get_capability_info"


class EngineResponseStatus(str, Enum):
    """Status of engine response."""

    SUCCESS = "success"
    ERROR = "error"
    BLOCKED = "blocked"  # Security/allowlist blocked


class EngineRequest(BaseModel):
    """Request to the Engine layer.

    This is the unified interface that all frontends use to communicate
    with the Engine. It's completely independent of MCP, HTTP, or any
    other transport protocol.
    """

    request_type: EngineRequestType
    capability: str | None = None
    payload: dict[str, Any] = Field(default_factory=dict)
    request_id: str | None = None

    model_config = ConfigDict(extra="forbid")


class EngineResponse(BaseModel):
    """Response from the Engine layer.

    Contains the result of executing a capability, along with metadata
    about execution time, errors, and any security blocks.
    """

    status: EngineResponseStatus
    request_id: str | None = None

    # Success case
    result: dict[str, Any] | None = None

    # Error case
    error: str | None = None
    error_type: str | None = None  # e.g., "capability_not_found", "validation_error"

    # Metadata
    capability: str | None = None
    execution_time_ms: float | None = None

    model_config = ConfigDict(extra="forbid")


class CapabilityInfo(BaseModel):
    """Information about a single capability."""

    name: str
    description: str
    scopes: list[str] = Field(default_factory=list)
    min_version: str | None = None
    max_version: str | None = None
    available: bool = True
    unavailable_reason: str | None = None

    model_config = ConfigDict(extra="forbid")


__all__ = [
    "EngineRequest",
    "EngineResponse",
    "EngineRequestType",
    "EngineResponseStatus",
    "CapabilityInfo",
]
