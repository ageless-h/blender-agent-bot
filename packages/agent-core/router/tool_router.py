from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Mapping


ToolHandler = Callable[[dict[str, Any]], Any]
ToolValidator = Callable[[dict[str, Any]], bool]


@dataclass(slots=True)
class ToolSpec:
    name: str
    handler: ToolHandler
    required_args: tuple[str, ...] = ()
    retry_count: int = 1
    validator: ToolValidator | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


class ToolRouter:
    """Agent 决策 -> 工具调用映射器。"""

    def __init__(self) -> None:
        self._registry: dict[str, ToolSpec] = {}

    def register_tool(
        self,
        name: str,
        handler: ToolHandler,
        *,
        required_args: tuple[str, ...] = (),
        retry_count: int = 1,
        validator: ToolValidator | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        self._registry[name] = ToolSpec(
            name=name,
            handler=handler,
            required_args=required_args,
            retry_count=max(1, retry_count),
            validator=validator,
            metadata=metadata or {},
        )

    def has_tool(self, name: str) -> bool:
        return name in self._registry

    def list_tools(self) -> list[str]:
        return sorted(self._registry.keys())

    def dispatch(self, tool_name: str, arguments: Mapping[str, Any] | None = None) -> Any:
        if tool_name not in self._registry:
            raise KeyError(f"tool not found: {tool_name}")

        spec = self._registry[tool_name]
        payload = dict(arguments or {})
        self._validate_required(spec, payload)
        if spec.validator and not spec.validator(payload):
            raise ValueError(f"tool args validation failed: {tool_name}")

        last_error: Exception | None = None
        for _ in range(spec.retry_count):
            try:
                return spec.handler(payload)
            except Exception as error:
                last_error = error

        raise RuntimeError(f"tool execution failed after retries: {tool_name}") from last_error

    def register_from_mapping(
        self,
        mapping: Mapping[str, ToolHandler],
        *,
        retry_count: int = 1,
    ) -> None:
        for name, handler in mapping.items():
            self.register_tool(name=name, handler=handler, retry_count=retry_count)

    def _validate_required(self, spec: ToolSpec, arguments: dict[str, Any]) -> None:
        missing = [key for key in spec.required_args if key not in arguments]
        if missing:
            missing_args = ", ".join(missing)
            raise ValueError(f"missing required args for {spec.name}: {missing_args}")
