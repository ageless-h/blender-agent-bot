from __future__ import annotations

import json
import re
from collections.abc import Iterable, Mapping, Sequence
from typing import Any

from .base import LLMAdapter, LLMResponse, ModelCapabilities, StreamChunk, ToolCall


class FallbackAdapter(LLMAdapter):
    """无原生 tool-calling 的降级适配器。"""

    TOOL_JSON_PATTERN = re.compile(
        r'\{\s*"tool"\s*:\s*"(?P<name>[^"]+)"\s*,\s*"arguments"\s*:\s*(?P<args>\{.*\})\s*\}',
        re.DOTALL,
    )

    def get_capabilities(self) -> ModelCapabilities:
        return ModelCapabilities(
            tool_calling=False,
            vision=False,
            parallel_tools=False,
            max_context=32_768,
        )

    def generate(
        self,
        messages: Sequence[Mapping[str, Any]],
        *,
        tools: Sequence[Mapping[str, Any]] | None = None,
        temperature: float = 0.2,
        max_tokens: int | None = None,
    ) -> LLMResponse:
        latest = ""
        for message in reversed(messages):
            if str(message.get("role")) == "user":
                latest = str(message.get("content", ""))
                break

        tool_call = self._extract_tool_call(latest)
        if tool_call is not None:
            text = f"检测到工具调用意图: {tool_call.name}"
            return LLMResponse(
                text=text,
                model=self.model,
                tool_calls=[tool_call],
                finish_reason="stop",
            )

        tool_hint = "\n可用工具: " + ", ".join(self._tool_names(tools)) if tools else ""
        text = f"[fallback:{self.model}] {latest}{tool_hint}".strip()
        return LLMResponse(text=text, model=self.model, finish_reason="stop")

    def stream(
        self,
        messages: Sequence[Mapping[str, Any]],
        *,
        tools: Sequence[Mapping[str, Any]] | None = None,
        temperature: float = 0.2,
        max_tokens: int | None = None,
    ) -> Iterable[StreamChunk]:
        response = self.generate(
            messages,
            tools=tools,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        for token in response.text.split(" "):
            if token:
                yield StreamChunk(text_delta=f"{token} ")
        for tool_call in response.tool_calls:
            yield StreamChunk(tool_call_delta=tool_call)
        yield StreamChunk(done=True)

    def _extract_tool_call(self, text: str) -> ToolCall | None:
        match = self.TOOL_JSON_PATTERN.search(text)
        if not match:
            return None
        name = match.group("name").strip()
        args_raw = match.group("args").strip()
        try:
            arguments = json.loads(args_raw)
            if not isinstance(arguments, dict):
                return None
        except json.JSONDecodeError:
            return None
        return ToolCall(name=name, arguments=arguments)

    def _tool_names(self, tools: Sequence[Mapping[str, Any]] | None) -> list[str]:
        if not tools:
            return []
        names: list[str] = []
        for tool in tools:
            function = tool.get("function")
            if isinstance(function, Mapping) and isinstance(function.get("name"), str):
                names.append(function["name"])
        return names
