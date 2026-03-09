"""OpenAI-compatible LLM adapter.

Supports:
- OpenAI API (GPT-4, GPT-3.5, etc.)
- Azure OpenAI
- Any OpenAI-compatible endpoint (LocalAI, vLLM, etc.)
"""

from __future__ import annotations

import os
from collections.abc import AsyncIterator
from typing import Any

try:
    from openai import AsyncOpenAI
    from openai.types.chat import ChatCompletion, ChatCompletionChunk

    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    AsyncOpenAI = None  # type: ignore
    ChatCompletion = None  # type: ignore
    ChatCompletionChunk = None  # type: ignore

from .base import LLMAdapter, LLMResponse, StreamChunk
from .capabilities import ModelCapabilities


class OpenAIAdapter(LLMAdapter):
    """Adapter for OpenAI and OpenAI-compatible APIs.

    Supports:
    - Official OpenAI API
    - Azure OpenAI
    - LocalAI, vLLM, and other compatible endpoints
    """

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        model: str = "gpt-4",
        organization: str | None = None,
        timeout: float = 60.0,
        max_retries: int = 2,
    ):
        """Initialize OpenAI adapter.

        Args:
            api_key: OpenAI API key (defaults to OPENAI_API_KEY env var)
            base_url: Custom base URL for compatible endpoints
            model: Model name to use
            organization: OpenAI organization ID
            timeout: Request timeout in seconds
            max_retries: Number of retries on failure

        Raises:
            ImportError: If openai package is not installed
        """
        if not OPENAI_AVAILABLE:
            raise ImportError("OpenAI package not installed. Install with: pip install openai")

        self.model = model
        self.client = AsyncOpenAI(
            api_key=api_key or os.getenv("OPENAI_API_KEY"),
            base_url=base_url,
            organization=organization,
            timeout=timeout,
            max_retries=max_retries,
        )

        # Detect capabilities based on model name
        self._capabilities = self._detect_capabilities()

    def _detect_capabilities(self) -> ModelCapabilities:
        """Detect model capabilities based on model name.

        Returns:
            ModelCapabilities for this model
        """
        model_lower = self.model.lower()

        # GPT-4 family
        if "gpt-4" in model_lower:
            supports_vision = "vision" in model_lower or "turbo" in model_lower
            max_context = 128000 if "turbo" in model_lower else 8192

            return ModelCapabilities(
                supports_tool_calling=True,
                supports_vision=supports_vision,
                supports_streaming=True,
                supports_parallel_tools=True,
                max_context_tokens=max_context,
                max_output_tokens=4096,
                model_name=self.model,
                provider="openai",
            )

        # GPT-3.5 family
        if "gpt-3.5" in model_lower:
            return ModelCapabilities(
                supports_tool_calling=True,
                supports_vision=False,
                supports_streaming=True,
                supports_parallel_tools=True,
                max_context_tokens=16385,
                max_output_tokens=4096,
                model_name=self.model,
                provider="openai",
            )

        # Default for unknown models
        return ModelCapabilities(
            supports_tool_calling=True,
            supports_vision=False,
            supports_streaming=True,
            supports_parallel_tools=False,
            max_context_tokens=4096,
            max_output_tokens=2048,
            model_name=self.model,
            provider="openai-compatible",
        )

    def get_capabilities(self) -> ModelCapabilities:
        """Get model capabilities."""
        return self._capabilities

    def _convert_tools_to_openai(
        self,
        tools: list[dict[str, Any]] | None,
    ) -> list[dict[str, Any]] | None:
        """Convert generic tool format to OpenAI format.

        Args:
            tools: Generic tool definitions

        Returns:
            OpenAI-formatted tools or None
        """
        if not tools:
            return None

        openai_tools = []
        for tool in tools:
            openai_tools.append(
                {
                    "type": "function",
                    "function": {
                        "name": tool.get("name"),
                        "description": tool.get("description", ""),
                        "parameters": tool.get("parameters", {}),
                    },
                }
            )

        return openai_tools

    def _extract_tool_calls(
        self,
        completion: ChatCompletion,
    ) -> list[dict[str, Any]] | None:
        """Extract tool calls from OpenAI response.

        Args:
            completion: OpenAI chat completion

        Returns:
            List of tool calls or None
        """
        message = completion.choices[0].message

        if not message.tool_calls:
            return None

        tool_calls = []
        for tc in message.tool_calls:
            tool_calls.append(
                {
                    "name": tc.function.name,
                    "arguments": tc.function.arguments,
                }
            )

        return tool_calls

    async def generate(
        self,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> LLMResponse:
        """Generate a response from OpenAI.

        Args:
            messages: Conversation history in OpenAI format
            tools: Available tools for function calling
            **kwargs: Additional OpenAI parameters (temperature, etc.)

        Returns:
            LLMResponse with content and optional tool calls
        """
        # Convert tools to OpenAI format
        openai_tools = self._convert_tools_to_openai(tools)

        # Build request parameters
        params: dict[str, Any] = {
            "model": self.model,
            "messages": messages,
            **kwargs,
        }

        if openai_tools:
            params["tools"] = openai_tools

        # Make API call
        completion = await self.client.chat.completions.create(**params)

        # Extract response
        message = completion.choices[0].message
        content = message.content or ""
        tool_calls = self._extract_tool_calls(completion)

        return LLMResponse(
            content=content,
            tool_calls=tool_calls,
            finish_reason=completion.choices[0].finish_reason,
            usage={
                "prompt_tokens": completion.usage.prompt_tokens if completion.usage else 0,
                "completion_tokens": completion.usage.completion_tokens if completion.usage else 0,
                "total_tokens": completion.usage.total_tokens if completion.usage else 0,
            },
        )

    async def stream(
        self,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> AsyncIterator[StreamChunk]:
        """Stream a response from OpenAI.

        Args:
            messages: Conversation history
            tools: Available tools
            **kwargs: Additional parameters

        Yields:
            StreamChunk objects with incremental content
        """
        # Convert tools to OpenAI format
        openai_tools = self._convert_tools_to_openai(tools)

        # Build request parameters
        params: dict[str, Any] = {
            "model": self.model,
            "messages": messages,
            "stream": True,
            **kwargs,
        }

        if openai_tools:
            params["tools"] = openai_tools

        # Stream response
        stream = await self.client.chat.completions.create(**params)

        # Accumulate tool calls
        tool_calls_accumulator: dict[int, dict[str, Any]] = {}

        async for chunk in stream:
            if not chunk.choices:
                continue

            choice = chunk.choices[0]
            delta = choice.delta

            # Handle content delta
            if delta.content:
                yield StreamChunk(
                    delta=delta.content,
                    tool_call_delta=None,
                    done=False,
                )

            # Handle tool call deltas
            if delta.tool_calls:
                for tc_delta in delta.tool_calls:
                    idx = tc_delta.index

                    if idx not in tool_calls_accumulator:
                        tool_calls_accumulator[idx] = {
                            "name": "",
                            "arguments": "",
                        }

                    if tc_delta.function:
                        if tc_delta.function.name:
                            tool_calls_accumulator[idx]["name"] = tc_delta.function.name
                        if tc_delta.function.arguments:
                            tool_calls_accumulator[idx]["arguments"] += tc_delta.function.arguments

            # Check if done
            if choice.finish_reason:
                # Convert accumulated tool calls
                tool_calls = None
                if tool_calls_accumulator:
                    tool_calls = list(tool_calls_accumulator.values())

                yield StreamChunk(
                    delta="",
                    tool_call_delta={"tool_calls": tool_calls} if tool_calls else None,
                    done=True,
                )
                break

    async def close(self) -> None:
        """Clean up OpenAI client resources."""
        await self.client.close()


__all__ = ["OpenAIAdapter"]
