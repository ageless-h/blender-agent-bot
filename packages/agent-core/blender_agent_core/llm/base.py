"""Base LLM adapter interface."""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import AsyncIterator
from typing import Any

from .capabilities import ModelCapabilities


class LLMResponse:
    """Response from LLM."""

    def __init__(
        self,
        content: str,
        tool_calls: list[dict[str, Any]] | None = None,
        finish_reason: str = "stop",
        usage: dict[str, int] | None = None,
    ):
        self.content = content
        self.tool_calls = tool_calls or []
        self.finish_reason = finish_reason
        self.usage = usage or {}


class StreamChunk:
    """Chunk of streaming response."""

    def __init__(
        self,
        delta: str = "",
        tool_call_delta: dict[str, Any] | None = None,
        done: bool = False,
    ):
        self.delta = delta
        self.tool_call_delta = tool_call_delta
        self.done = done


class LLMAdapter(ABC):
    """Abstract base class for LLM adapters.

    All LLM adapters (OpenAI, Anthropic, etc.) must implement this interface.
    """

    @abstractmethod
    def get_capabilities(self) -> ModelCapabilities:
        """Get model capabilities.

        Returns:
            ModelCapabilities describing what this model can do
        """
        pass

    @abstractmethod
    async def generate(
        self,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> LLMResponse:
        """Generate a response from the LLM.

        Args:
            messages: Conversation history in OpenAI format
            tools: Available tools for function calling
            **kwargs: Additional model-specific parameters

        Returns:
            LLMResponse with content and optional tool calls
        """
        pass

    @abstractmethod
    async def stream(
        self,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> AsyncIterator[StreamChunk]:
        """Stream a response from the LLM.

        Args:
            messages: Conversation history
            tools: Available tools
            **kwargs: Additional parameters

        Yields:
            StreamChunk objects with incremental content
        """
        pass

    async def close(self) -> None:
        """Clean up resources (optional)."""
        pass


__all__ = [
    "LLMAdapter",
    "LLMResponse",
    "StreamChunk",
    "ModelCapabilities",
]
