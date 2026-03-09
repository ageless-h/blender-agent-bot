"""Fallback adapter for models without native tool calling support.

This adapter wraps any LLM and simulates tool calling by:
1. Injecting tool descriptions into the system prompt
2. Parsing structured output (JSON) from the model's response
3. Converting parsed tool calls into standard LLMResponse format

Use this for:
- Local models without function calling
- Legacy API endpoints
- Custom/experimental models
"""

from __future__ import annotations

import json
import re
from collections.abc import AsyncIterator
from typing import Any

from .base import LLMAdapter, LLMResponse, StreamChunk
from .capabilities import ModelCapabilities


class FallbackAdapter(LLMAdapter):
    """Adapter that adds tool calling to models without native support.

    Wraps any base LLM adapter and simulates tool calling through prompt engineering.
    """

    def __init__(self, base_adapter: LLMAdapter):
        """Initialize fallback adapter.

        Args:
            base_adapter: The underlying LLM adapter to wrap
        """
        self.base_adapter = base_adapter
        self._capabilities = self._build_capabilities()

    def _build_capabilities(self) -> ModelCapabilities:
        """Build capabilities based on base adapter."""
        base_caps = self.base_adapter.get_capabilities()

        # Inherit most capabilities, but disable tool calling
        return ModelCapabilities(
            supports_tool_calling=False,  # We simulate it, not native
            supports_vision=base_caps.supports_vision,
            supports_streaming=base_caps.supports_streaming,
            supports_parallel_tools=False,  # Fallback doesn't support parallel
            max_context_tokens=base_caps.max_context_tokens,
            max_output_tokens=base_caps.max_output_tokens,
            model_name=f"{base_caps.model_name} (fallback)",
            provider=base_caps.provider,
        )

    def get_capabilities(self) -> ModelCapabilities:
        """Get capabilities of this adapter."""
        return self._capabilities

    def _build_tool_prompt(self, tools: list[dict[str, Any]]) -> str:
        """Build tool description prompt.

        Args:
            tools: List of tool definitions

        Returns:
            Formatted prompt describing available tools
        """
        if not tools:
            return ""

        tool_descriptions = []
        for tool in tools:
            name = tool.get("name", "unknown")
            description = tool.get("description", "")
            parameters = tool.get("parameters", {})

            tool_descriptions.append(
                f"- {name}: {description}\n  Parameters: {json.dumps(parameters, indent=2)}"
            )

        prompt = (
            "\n\nYou have access to the following tools:\n"
            + "\n".join(tool_descriptions)
            + "\n\nTo use a tool, respond with JSON in this format:\n"
            '{"tool": "tool_name", "arguments": {...}}\n\n'
            "If you don't need to use a tool, respond normally."
        )

        return prompt

    def _inject_tools_into_messages(
        self,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]] | None,
    ) -> list[dict[str, Any]]:
        """Inject tool descriptions into system message.

        Args:
            messages: Original message list
            tools: Tool definitions

        Returns:
            Modified message list with tool prompt
        """
        if not tools:
            return messages

        tool_prompt = self._build_tool_prompt(tools)
        modified_messages = messages.copy()

        # Find or create system message
        system_idx = None
        for i, msg in enumerate(modified_messages):
            if msg.get("role") == "system":
                system_idx = i
                break

        if system_idx is not None:
            # Append to existing system message
            modified_messages[system_idx] = {
                "role": "system",
                "content": modified_messages[system_idx]["content"] + tool_prompt,
            }
        else:
            # Insert new system message at the beginning
            modified_messages.insert(
                0,
                {
                    "role": "system",
                    "content": tool_prompt,
                },
            )

        return modified_messages

    def _parse_tool_call(self, content: str) -> tuple[str, list[dict[str, Any]] | None]:
        """Parse tool call from model response.

        Args:
            content: Raw model output

        Returns:
            Tuple of (cleaned_content, tool_calls)
            - cleaned_content: Text with tool JSON removed
            - tool_calls: Parsed tool calls or None
        """
        # Look for JSON blocks in the response
        json_pattern = r'```json\s*(\{.*?\})\s*```|(\{[^{}]*"tool"[^{}]*\})'
        matches = re.finditer(json_pattern, content, re.DOTALL)

        tool_calls = []
        cleaned_content = content

        for match in matches:
            json_str = match.group(1) or match.group(2)
            try:
                data = json.loads(json_str)
                if "tool" in data and "arguments" in data:
                    tool_calls.append(
                        {
                            "name": data["tool"],
                            "arguments": data["arguments"],
                        }
                    )
                    # Remove the JSON block from content
                    cleaned_content = cleaned_content.replace(match.group(0), "").strip()
            except json.JSONDecodeError:
                # Not valid JSON, skip
                continue

        return cleaned_content, tool_calls if tool_calls else None

    async def generate(
        self,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> LLMResponse:
        """Generate response with simulated tool calling.

        Args:
            messages: Conversation history
            tools: Available tools
            **kwargs: Additional parameters

        Returns:
            LLMResponse with parsed tool calls
        """
        # Inject tool descriptions into messages
        modified_messages = self._inject_tools_into_messages(messages, tools)

        # Call base adapter
        response = await self.base_adapter.generate(
            modified_messages,
            tools=None,  # Don't pass tools to base adapter
            **kwargs,
        )

        # Parse tool calls from response
        cleaned_content, tool_calls = self._parse_tool_call(response.content)

        return LLMResponse(
            content=cleaned_content,
            tool_calls=tool_calls,
            finish_reason=response.finish_reason,
            usage=response.usage,
        )

    async def stream(
        self,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> AsyncIterator[StreamChunk]:
        """Stream response with simulated tool calling.

        Note: Tool calls are only detected at the end of streaming.

        Args:
            messages: Conversation history
            tools: Available tools
            **kwargs: Additional parameters

        Yields:
            StreamChunk objects
        """
        # Inject tool descriptions
        modified_messages = self._inject_tools_into_messages(messages, tools)

        # Accumulate full response for tool parsing
        accumulated_content = ""

        async for chunk in self.base_adapter.stream(modified_messages, tools=None, **kwargs):
            accumulated_content += chunk.delta

            if chunk.done:
                # Parse tool calls from complete response
                cleaned_content, tool_calls = self._parse_tool_call(accumulated_content)

                # Yield final chunk with tool calls
                yield StreamChunk(
                    delta="",
                    tool_call_delta={"tool_calls": tool_calls} if tool_calls else None,
                    done=True,
                )
            else:
                # Yield content chunks as-is
                yield chunk

    async def close(self) -> None:
        """Clean up base adapter resources."""
        await self.base_adapter.close()


__all__ = ["FallbackAdapter"]
