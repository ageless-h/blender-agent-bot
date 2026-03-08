from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Iterable, Mapping, Sequence


@dataclass(slots=True, frozen=True)
class ModelCapabilities:
    tool_calling: bool
    vision: bool
    parallel_tools: bool
    max_context: int


@dataclass(slots=True)
class ToolCall:
    name: str
    arguments: dict[str, Any]


@dataclass(slots=True)
class LLMResponse:
    text: str
    model: str
    tool_calls: list[ToolCall] = field(default_factory=list)
    finish_reason: str | None = None
    usage: dict[str, int] = field(default_factory=dict)
    raw: Any | None = None


@dataclass(slots=True)
class StreamChunk:
    text_delta: str = ""
    done: bool = False
    tool_call_delta: ToolCall | None = None
    raw: Any | None = None


def normalize_messages(messages: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    normalized: list[dict[str, Any]] = []
    for message in messages:
        role = str(message.get("role", "user"))
        content = message.get("content", "")
        normalized.append(
            {
                "role": role,
                "content": content,
                **{k: v for k, v in message.items() if k not in {"role", "content"}},
            }
        )
    return normalized


class LLMAdapter(ABC):
    def __init__(
        self,
        model: str,
        *,
        base_url: str | None = None,
        api_key: str | None = None,
        timeout: float = 60.0,
        allow_mock: bool = False,
    ) -> None:
        self.model = model
        self.base_url = base_url
        self.api_key = api_key
        self.timeout = timeout
        self.allow_mock = allow_mock

    @abstractmethod
    def get_capabilities(self) -> ModelCapabilities:
        raise NotImplementedError

    @abstractmethod
    def generate(
        self,
        messages: Sequence[Mapping[str, Any]],
        *,
        tools: Sequence[Mapping[str, Any]] | None = None,
        temperature: float = 0.2,
        max_tokens: int | None = None,
    ) -> LLMResponse:
        raise NotImplementedError

    @abstractmethod
    def stream(
        self,
        messages: Sequence[Mapping[str, Any]],
        *,
        tools: Sequence[Mapping[str, Any]] | None = None,
        temperature: float = 0.2,
        max_tokens: int | None = None,
    ) -> Iterable[StreamChunk]:
        raise NotImplementedError
