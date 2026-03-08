from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

from ..protocol import SafetyLevel, ToolResult

ToolHandler = Callable[[dict[str, Any]], ToolResult]


@dataclass(frozen=True, slots=True)
class ToolDefinition:
    name: str
    description: str
    safety_level: SafetyLevel
    layer: str
    handler: ToolHandler
