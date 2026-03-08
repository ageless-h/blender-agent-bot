from __future__ import annotations

import importlib
from collections.abc import Iterable, Mapping, Sequence
from typing import Any

from .base import LLMAdapter, LLMResponse, ModelCapabilities, StreamChunk, ToolCall


class AnthropicAdapter(LLMAdapter):
    """Anthropic Claude 适配器。"""

    def __init__(
        self,
        model: str,
        *,
        api_key: str | None = None,
        base_url: str | None = None,
        timeout: float = 60.0,
        allow_mock: bool = False,
    ) -> None:
        super().__init__(
            model,
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            allow_mock=allow_mock,
        )
        self._client = None

    def get_capabilities(self) -> ModelCapabilities:
        model = self.model.lower()
        max_context = 200_000 if "claude" in model else 64_000
        vision = any(token in model for token in ("3-5", "3.5", "sonnet", "opus", "haiku"))
        return ModelCapabilities(
            tool_calling=True,
            vision=vision,
            parallel_tools=True,
            max_context=max_context,
        )

    def _get_client(self) -> Any | None:
        if self._client is not None:
            return self._client
        if not self.api_key:
            return None
        try:
            anthropic_mod = importlib.import_module("anthropic")
        except Exception:  # pragma: no cover - optional dependency
            return None
        kwargs: dict[str, Any] = {"api_key": self.api_key, "timeout": self.timeout}
        if self.base_url:
            kwargs["base_url"] = self.base_url
        self._client = anthropic_mod.Anthropic(**kwargs)
        return self._client

    def _convert_messages(self, messages: Sequence[Mapping[str, Any]]) -> tuple[str | None, list[dict[str, Any]]]:
        system_parts: list[str] = []
        anthropic_messages: list[dict[str, Any]] = []
        for message in messages:
            role = str(message.get("role", "user"))
            content = message.get("content", "")
            if role == "system":
                system_parts.append(str(content))
                continue
            anthropic_messages.append({"role": role, "content": str(content)})
        system_prompt = "\n\n".join(system_parts) if system_parts else None
        return system_prompt, anthropic_messages

    def generate(
        self,
        messages: Sequence[Mapping[str, Any]],
        *,
        tools: Sequence[Mapping[str, Any]] | None = None,
        temperature: float = 0.2,
        max_tokens: int | None = None,
    ) -> LLMResponse:
        client = self._get_client()
        if client is None:
            if not self.allow_mock:
                raise RuntimeError("Anthropic client unavailable. 请安装 anthropic 并配置 api_key 后重试。")
            return self._mock_generate(messages)

        system_prompt, anthropic_messages = self._convert_messages(messages)
        payload: dict[str, Any] = {
            "model": self.model,
            "messages": anthropic_messages,
            "temperature": temperature,
            "max_tokens": max_tokens or 1024,
        }
        if system_prompt:
            payload["system"] = system_prompt
        if tools:
            payload["tools"] = list(tools)

        response = client.messages.create(**payload)
        text_parts: list[str] = []
        tool_calls: list[ToolCall] = []
        for block in getattr(response, "content", []) or []:
            block_type = getattr(block, "type", "")
            if block_type == "text":
                text_parts.append(getattr(block, "text", ""))
            if block_type == "tool_use":
                tool_calls.append(
                    ToolCall(
                        name=str(getattr(block, "name", "")),
                        arguments=dict(getattr(block, "input", {}) or {}),
                    )
                )

        usage = getattr(response, "usage", None)
        usage_dict = {
            "prompt_tokens": getattr(usage, "input_tokens", 0) if usage else 0,
            "completion_tokens": getattr(usage, "output_tokens", 0) if usage else 0,
            "total_tokens": ((getattr(usage, "input_tokens", 0) + getattr(usage, "output_tokens", 0)) if usage else 0),
        }
        return LLMResponse(
            text="".join(text_parts),
            model=self.model,
            tool_calls=tool_calls,
            finish_reason=getattr(response, "stop_reason", None),
            usage=usage_dict,
            raw=response,
        )

    def stream(
        self,
        messages: Sequence[Mapping[str, Any]],
        *,
        tools: Sequence[Mapping[str, Any]] | None = None,
        temperature: float = 0.2,
        max_tokens: int | None = None,
    ) -> Iterable[StreamChunk]:
        client = self._get_client()
        if client is None:
            if not self.allow_mock:
                raise RuntimeError("Anthropic client unavailable. 请安装 anthropic 并配置 api_key 后重试。")
            yield from self._mock_stream(messages)
            return

        system_prompt, anthropic_messages = self._convert_messages(messages)
        payload: dict[str, Any] = {
            "model": self.model,
            "messages": anthropic_messages,
            "temperature": temperature,
            "max_tokens": max_tokens or 1024,
            "stream": True,
        }
        if system_prompt:
            payload["system"] = system_prompt
        if tools:
            payload["tools"] = list(tools)

        stream = client.messages.create(**payload)
        for event in stream:
            event_type = getattr(event, "type", "")
            if event_type in {"content_block_delta", "content_block_start"}:
                delta = getattr(event, "delta", None)
                if delta is not None:
                    text = getattr(delta, "text", "")
                    if text:
                        yield StreamChunk(text_delta=text, raw=event)

                block = getattr(event, "content_block", None)
                if block is not None and getattr(block, "type", "") == "tool_use":
                    yield StreamChunk(
                        tool_call_delta=ToolCall(
                            name=str(getattr(block, "name", "")),
                            arguments=dict(getattr(block, "input", {}) or {}),
                        ),
                        raw=event,
                    )

            if event_type == "message_stop":
                yield StreamChunk(done=True, raw=event)
                break

    def _mock_generate(self, messages: Sequence[Mapping[str, Any]]) -> LLMResponse:
        latest = ""
        for message in reversed(messages):
            if str(message.get("role")) == "user":
                latest = str(message.get("content", ""))
                break
        return LLMResponse(
            text=f"[mock-anthropic:{self.model}] {latest}",
            model=self.model,
            finish_reason="stop",
        )

    def _mock_stream(self, messages: Sequence[Mapping[str, Any]]) -> Iterable[StreamChunk]:
        text = self._mock_generate(messages).text
        for token in text.split(" "):
            if token:
                yield StreamChunk(text_delta=f"{token} ")
        yield StreamChunk(done=True)
