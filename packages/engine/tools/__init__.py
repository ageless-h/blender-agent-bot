from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable

from ..protocol import ToolResult
from .declarative import get_tool_definitions as get_declarative_tools
from .fallback import get_tool_definitions as get_fallback_tools
from .imperative import get_tool_definitions as get_imperative_tools
from .perception import get_tool_definitions as get_perception_tools
from .spec import ToolDefinition


@dataclass(slots=True)
class ToolRegistry:
    _items: dict[str, ToolDefinition] = field(default_factory=dict)

    def register(self, definition: ToolDefinition) -> None:
        self._items[definition.name] = definition

    def register_many(self, definitions: Iterable[ToolDefinition]) -> None:
        for definition in definitions:
            self.register(definition)

    def has(self, tool_name: str) -> bool:
        return tool_name in self._items

    def get(self, tool_name: str) -> ToolDefinition:
        if tool_name not in self._items:
            raise KeyError(f"unknown tool: {tool_name}")
        return self._items[tool_name]

    def list_tools(self) -> list[ToolDefinition]:
        return list(self._items.values())

    def execute(self, tool_name: str, arguments: dict[str, object]) -> ToolResult:
        try:
            definition = self.get(tool_name)
        except KeyError as exc:
            return ToolResult(tool_name=tool_name, success=False, error=str(exc))

        try:
            return definition.handler(arguments)
        except Exception as exc:
            return ToolResult(tool_name=tool_name, success=False, error=str(exc))


def build_default_registry() -> ToolRegistry:
    registry = ToolRegistry()
    registry.register_many(get_perception_tools())
    registry.register_many(get_declarative_tools())
    registry.register_many(get_imperative_tools())
    registry.register_many(get_fallback_tools())
    return registry


__all__ = ["ToolDefinition", "ToolRegistry", "build_default_registry"]
