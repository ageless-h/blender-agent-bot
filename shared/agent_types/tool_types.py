from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class SafetyLevel(str, Enum):
    LEVEL_0 = "level_0"
    LEVEL_1 = "level_1"
    LEVEL_2 = "level_2"
    LEVEL_3 = "level_3"
    FORBIDDEN = "forbidden"


class ToolDefinition(BaseModel):
    name: str
    description: str
    parameters: dict[str, Any] = Field(default_factory=dict)
    safety_level: SafetyLevel = SafetyLevel.LEVEL_1

    model_config = ConfigDict(extra="forbid")


class ToolCall(BaseModel):
    tool_name: str
    arguments: dict[str, Any] = Field(default_factory=dict)

    model_config = ConfigDict(extra="forbid")


class ToolResult(BaseModel):
    success: bool
    data: Any | None = None
    error: str | None = None

    model_config = ConfigDict(extra="forbid")


__all__ = [
    "SafetyLevel",
    "ToolDefinition",
    "ToolCall",
    "ToolResult",
]
