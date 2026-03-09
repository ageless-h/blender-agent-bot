"""Anthropic Claude LLM adapter.

Supports Claude models via the Anthropic API.
"""

from __future__ import annotations

import json
import os
from collections.abc import AsyncIterator
from typing import Any

try:
    from anthropic import AsyncAnthropic
    from anthropic.types import Message, MessageStreamEvent

    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False
    AsyncAnthropic = None  # type: ignore
    Message = None  # type: ignore
    MessageStreamEvent = None  # type: ignore

from .base import LLMAdapter, LLMResponse, StreamChunk
from .capabilities import ModelCapabilities


class AnthropicAdapter(LLMAdapter):
    """Adapter for Anthropic Claude models.

    Supports Claude 3 family (Opus, Sonnet, Haiku) with tool calling and vision.
    """

    def __init__(
        self,
        api_key: str | None = None,
        model: str = "claude-3-5-sonnet-20241022",
        timeout: float = 600.0,
        max_retries: int = 2,
    ):
        """Initialize Anthropic adapter.

        Args:
            api_key: Anthropic API key (defaults to ANTHROPIC_API_KEY env var)
            model: Claude model name
            timeout: Request timeout in seconds
            max_retries: Number of retries on failure

        Raises:
            ImportError: If anthropic package is not installed
        """
        if not ANTHROPIC_AVAILABLE:
            raise ImportError(
                "Anthropic package not installed. Install with: pip install anthropic"
            )

        self.model = model
        self.client = AsyncAnthropic(
            api_key=api_key or os.getenv("ANTHROPIC_API_KEY"),
            timeout=timeout,
            max_retries=max_retries,
        )

        self._capabilities = self._detect_capabilities()

    def _detect_capabilities(self) -> ModelCapabilities:
        """Detect model capabilities based on model name.

        Returns:
            ModelCapabilities for this model
        """
        model_lower = self.model.lower()

        # Claude 3 Opus
        if "opus" in model_lower:
            return ModelCapabilities(
                supports_tool_calling=True,
                supports_vision=True,
                supports_streaming=True,
                supports_parallel_tools=True,
                max_context_tokens=200000,
                max_output_tokens=4096,
                model_name=self.model,
                provider="anthropic",
            )

        # Claude 3 Sonnet
        if "sonnet" in model_lower:
            return ModelCapabilities(
                supports_tool_calling=True,
                supports_vision=True,
                supports_streaming=True,
                supports_parallel_tools=True,
                max_context_tokens=200000,
                max_output_tokens=4096,
                model_name=self.model,
                provider="anthropic",
            )

        # Claude 3 Haiku
        if "haiku" in model_lower:
            return ModelCapabilities(
                supports_tool_calling=True,
                supports_vision=True,
                supports_streaming=True,
                supports_parallel_tools=True,
                max_context_tokens=200000,
                max_output_tokens=4096,
                model_name=self.model,
                provider="anthropic",
            )

        # Default for unknown Claude models
        return ModelCapabilities(
            supports_tool_calling=True,
            supports_vision=False,
            supports_streaming=True,
            supports_parallel_tools=False,
            max_context_tokens=100000,
            max_output_tokens=4096,
            model_name=self.model,
            provider="anthropic",
        )

    def get_capabilities(self) -> ModelCapabilities:
        """Get model capabilities."""
        return self._capabilities

    def _convert_messages_to_anthropic(
        self,
        messages: list[dict[str, Any]],
    ) -> tuple[str, list[dict[str, Any]]]:
        """Convert OpenAI-style messages to Anthropic format.

        Args:
            messages: OpenAI-format messages

        Returns:
            Tuple of (system_prompt, anthropic_messages)
        """
        system_prompt = ""
        anthropic_messages = []

        for msg in messages:
            role = msg.get("role")
            content = msg.get("content", "")

            if role == "system":
                # Anthropic uses separate system parameter
                system_prompt = content
            elif role in ["user", "assistant"]:
                anthropic_messages.append(
                    {
                        "role": role,
                        "content": content,
                    }
                )

        return system_prompt, anthropic_messages

    def _convert_tools_to_anthropic(
        self,
        tools: list[dict[str, Any]] | None,
    ) -> list[dict[str, Any]] | None:
        """Convert generic tool format to Anthropic format.

        Args:
            tools: Generic tool definitions

        Returns:
            Anthropic-formatted tools or None
        """
        if not tools:
            return None

        anthropic_tools = []
        for tool in tools:
            anthropic_tools.append(
                {
                    "name": tool.get("name"),
                    "description": tool.get("description", ""),
                    "input_schema": tool.get("parameters", {}),
                }
            )

        return anthropic_tools

    def _extract_tool_calls(
        self,
        message: Message,
    ) -> list[dict[str, Any]] | None:
        """Extract tool calls from Anthropic response.

        Args:
            message: Anthropic message

        Returns:
            List of tool calls or None
        """
        if not hasattr(message, "content") or not message.content:
            return None

        tool_calls = []
        for block in message.content:
            if block.type == "tool_use":
                tool_calls.append(
                    {
                        "name": block.name,
                        "arguments": json.dumps(block.input)
                        if isinstance(block.input, dict)
                        else block.input,
                    }
                )

        return tool_calls if tool_calls else None

    def _extract_text_content(self, message: Message) -> str:
        """Extract text content from Anthropic message.

        Args:
            message: Anthropic message

        Returns:
            Extracted text content
        """
        if not hasattr(message, "content") or not message.content:
            return ""

        text_parts = []
        for block in message.content:
            if block.type == "text":
                text_parts.append(block.text)

        return "".join(text_parts)

    async def generate(
        self,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> LLMResponse:
        """Generate a response from Claude.

        Args:
            messages: Conversation history in OpenAI format
            tools: Available tools for function calling
            **kwargs: Additional Anthropic parameters

        Returns:
            LLMResponse with content and optional tool calls
        """
        # Convert messages to Anthropic format
        system_prompt, anthropic_messages = self._convert_messages_to_anthropic(messages)

        # Convert tools to Anthropic format
        anthropic_tools = self._convert_tools_to_anthropic(tools)

        # Build request parameters
        params: dict[str, Any] = {
            "model": self.model,
            "messages": anthropic_messages,
            "max_tokens": kwargs.pop("max_tokens", 4096),
            **kwargs,
        }

        if system_prompt:
            params["system"] = system_prompt

        if anthropic_tools:
            params["tools"] = anthropic_tools

        # Make API call
        message = await self.client.messages.create(**params)

        # Extract response
        content = self._extract_text_content(message)
        tool_calls = self._extract_tool_calls(message)

        return LLMResponse(
            content=content,
            tool_calls=tool_calls,
            finish_reason=message.stop_reason or "stop",
            usage={
                "prompt_tokens": message.usage.input_tokens if message.usage else 0,
                "completion_tokens": message.usage.output_tokens if message.usage else 0,
                "total_tokens": (
                    (message.usage.input_tokens + message.usage.output_tokens)
                    if message.usage
                    else 0
                ),
            },
        )

    async def stream(
        self,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> AsyncIterator[StreamChunk]:
        """Stream a response from Claude.

        Args:
            messages: Conversation history
            tools: Available tools
            **kwargs: Additional parameters

        Yields:
            StreamChunk objects with incremental content
        """
        # Convert messages to Anthropic format
        system_prompt, anthropic_messages = self._convert_messages_to_anthropic(messages)

        # Convert tools to Anthropic format
        anthropic_tools = self._convert_tools_to_anthropic(tools)

        # Build request parameters
        params: dict[str, Any] = {
            "model": self.model,
            "messages": anthropic_messages,
            "max_tokens": kwargs.pop("max_tokens", 4096),
            "stream": True,
            **kwargs,
        }

        if system_prompt:
            params["system"] = system_prompt

        if anthropic_tools:
            params["tools"] = anthropic_tools

        # Stream response
        tool_calls_accumulator: list[dict[str, Any]] = []

        async with self.client.messages.stream(**params) as stream:
            async for event in stream:
                # Handle content deltas
                if event.type == "content_block_delta":
                    if hasattr(event.delta, "text"):
                        yield StreamChunk(
                            delta=event.delta.text,
                            tool_call_delta=None,
                            done=False,
                        )

                # Handle tool use blocks
                elif event.type == "content_block_start":
                    if (
                        hasattr(event.content_block, "type")
                        and event.content_block.type == "tool_use"
                    ):
                        tool_calls_accumulator.append(
                            {
                                "name": event.content_block.name,
                                "arguments": "",
                            }
                        )

                elif event.type == "content_block_delta":
                    if hasattr(event.delta, "partial_json"):
                        # Accumulate tool arguments
                        if tool_calls_accumulator:
                            tool_calls_accumulator[-1]["arguments"] += event.delta.partial_json

                # Handle stream end
                elif event.type == "message_stop":
                    # Finalize tool calls
                    tool_calls = None
                    if tool_calls_accumulator:
                        tool_calls = tool_calls_accumulator

                    yield StreamChunk(
                        delta="",
                        tool_call_delta={"tool_calls": tool_calls} if tool_calls else None,
                        done=True,
                    )

    async def close(self) -> None:
        """Clean up Anthropic client resources."""
        await self.client.close()


__all__ = ["AnthropicAdapter"]
