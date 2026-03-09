"""Mock LLM adapter for testing and demonstration.

This adapter simulates LLM behavior without making real API calls.
Useful for:
- Unit testing
- Development without API keys
- Demonstrating streaming behavior
"""

from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator
from typing import Any

from .base import LLMAdapter, LLMResponse, StreamChunk
from .capabilities import ModelCapabilities


class MockAdapter(LLMAdapter):
    """Mock adapter that simulates LLM responses.

    Provides configurable responses for testing without real API calls.
    """

    def __init__(
        self,
        response_text: str = "Mock response",
        supports_tools: bool = True,
        supports_streaming: bool = True,
        stream_delay: float = 0.05,
    ):
        """Initialize mock adapter.

        Args:
            response_text: Default response text
            supports_tools: Whether to simulate tool calling support
            supports_streaming: Whether to support streaming
            stream_delay: Delay between stream chunks (seconds)
        """
        self.response_text = response_text
        self.stream_delay = stream_delay
        self._capabilities = ModelCapabilities(
            supports_tool_calling=supports_tools,
            supports_vision=False,
            supports_streaming=supports_streaming,
            supports_parallel_tools=supports_tools,
            max_context_tokens=8192,
            max_output_tokens=4096,
            model_name="mock-model",
            provider="mock",
        )

    def get_capabilities(self) -> ModelCapabilities:
        """Get mock capabilities."""
        return self._capabilities

    async def generate(
        self,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> LLMResponse:
        """Generate a mock response.

        Args:
            messages: Conversation history
            tools: Available tools
            **kwargs: Additional parameters

        Returns:
            Mock LLMResponse
        """
        # Simulate API delay
        await asyncio.sleep(0.1)

        # Check if last message asks for tool use
        tool_calls = None
        if tools and messages:
            last_msg = messages[-1].get("content", "")
            if "tool" in last_msg.lower() or "function" in last_msg.lower():
                # Simulate a tool call
                tool_calls = [
                    {
                        "name": tools[0]["name"],
                        "arguments": {"param": "mock_value"},
                    }
                ]

        return LLMResponse(
            content=self.response_text,
            tool_calls=tool_calls,
            finish_reason="stop",
            usage={"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15},
        )

    async def stream(
        self,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> AsyncIterator[StreamChunk]:
        """Stream a mock response.

        Demonstrates proper streaming behavior by yielding chunks incrementally.

        Args:
            messages: Conversation history
            tools: Available tools
            **kwargs: Additional parameters

        Yields:
            StreamChunk objects with incremental content
        """
        if not self._capabilities.supports_streaming:
            raise NotImplementedError("Streaming not supported by this mock adapter")

        # Split response into words for streaming
        words = self.response_text.split()

        for i, word in enumerate(words):
            # Add space before word (except first)
            delta = f" {word}" if i > 0 else word

            yield StreamChunk(
                delta=delta,
                tool_call_delta=None,
                done=False,
            )

            # Simulate network delay
            await asyncio.sleep(self.stream_delay)

        # Check if we should simulate a tool call
        tool_call_delta = None
        if tools and messages:
            last_msg = messages[-1].get("content", "")
            if "tool" in last_msg.lower():
                tool_call_delta = {
                    "tool_calls": [
                        {
                            "name": tools[0]["name"],
                            "arguments": {"param": "mock_value"},
                        }
                    ]
                }

        # Final chunk marks completion
        yield StreamChunk(
            delta="",
            tool_call_delta=tool_call_delta,
            done=True,
        )


class ErrorAdapter(LLMAdapter):
    """Mock adapter that simulates errors.

    Useful for testing error handling paths.
    """

    def __init__(self, error_message: str = "Mock error"):
        """Initialize error adapter.

        Args:
            error_message: Error message to raise
        """
        self.error_message = error_message
        self._capabilities = ModelCapabilities(
            supports_tool_calling=False,
            supports_vision=False,
            supports_streaming=False,
            max_context_tokens=0,
            max_output_tokens=0,
            model_name="error-model",
            provider="mock",
        )

    def get_capabilities(self) -> ModelCapabilities:
        """Get error adapter capabilities."""
        return self._capabilities

    async def generate(
        self,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> LLMResponse:
        """Raise an error."""
        raise RuntimeError(self.error_message)

    async def stream(
        self,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> AsyncIterator[StreamChunk]:
        """Raise an error."""
        raise RuntimeError(self.error_message)
        # Make this a generator
        yield  # type: ignore


__all__ = ["MockAdapter", "ErrorAdapter"]
