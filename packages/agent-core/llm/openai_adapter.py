from __future__ import annotations

import importlib
from collections.abc import Iterable, Mapping, Sequence
from typing import Any

from .base import LLMAdapter, LLMResponse, ModelCapabilities, StreamChunk, ToolCall, normalize_messages


class OpenAIAdapter(LLMAdapter):
    """OpenAI 兼容协议适配器。

    支持 GPT 系列以及 OpenAI-compatible 服务（Ollama/vLLM/LM Studio/LocalAI）。
    """

    def __init__(
        self,
        model: str,
        *,
        base_url: str | None = None,
        api_key: str | None = None,
        timeout: float = 60.0,
        allow_mock: bool = False,
    ) -> None:
        super().__init__(
            model,
            base_url=base_url,
            api_key=api_key,
            timeout=timeout,
            allow_mock=allow_mock,
        )
        self._client = None

    def get_capabilities(self) -> ModelCapabilities:
        name = self.model.lower()
        vision = any(token in name for token in ("gpt-4o", "vision", "omni", "llava"))
        parallel_tools = any(token in name for token in ("gpt-4.1", "gpt-4o", "o1", "o3"))
        max_context = 1_000_000 if "gpt-4.1" in name else 128_000
        return ModelCapabilities(
            tool_calling=True,
            vision=vision,
            parallel_tools=parallel_tools,
            max_context=max_context,
        )

    def _get_client(self) -> Any | None:
        if self._client is not None:
            return self._client
        try:
            openai_mod = importlib.import_module("openai")
        except Exception:  # pragma: no cover - optional dependency
            return None
        kwargs: dict[str, Any] = {
            "timeout": self.timeout,
        }
        if self.base_url:
            kwargs["base_url"] = self.base_url
        if self.api_key:
            kwargs["api_key"] = self.api_key
        elif self.base_url:
            kwargs["api_key"] = "not-required"
        else:
            return None
        self._client = openai_mod.OpenAI(**kwargs)
        return self._client

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
                raise RuntimeError(
                    "OpenAI client unavailable. 请安装 openai 并提供 api_key，"
                    "或配置 base_url (OpenAI-compatible) 后重试。"
                )
            return self._mock_generate(messages, tools=tools)

        payload: dict[str, Any] = {
            "model": self.model,
            "messages": normalize_messages(messages),
            "temperature": temperature,
        }
        if max_tokens is not None:
            payload["max_tokens"] = max_tokens
        if tools:
            payload["tools"] = list(tools)

        completion = client.chat.completions.create(**payload)
        choice = completion.choices[0]
        message = choice.message
        tool_calls: list[ToolCall] = []
        for call in getattr(message, "tool_calls", []) or []:
            function = getattr(call, "function", None)
            if function is None:
                continue
            arguments = function.arguments
            if isinstance(arguments, str):
                parsed_arguments: dict[str, Any] = {"raw": arguments}
            elif isinstance(arguments, dict):
                parsed_arguments = arguments
            else:
                parsed_arguments = {"raw": str(arguments)}
            tool_calls.append(ToolCall(name=function.name, arguments=parsed_arguments))

        usage = getattr(completion, "usage", None)
        usage_dict = {
            "prompt_tokens": getattr(usage, "prompt_tokens", 0) if usage else 0,
            "completion_tokens": getattr(usage, "completion_tokens", 0) if usage else 0,
            "total_tokens": getattr(usage, "total_tokens", 0) if usage else 0,
        }

        return LLMResponse(
            text=message.content or "",
            model=self.model,
            tool_calls=tool_calls,
            finish_reason=choice.finish_reason,
            usage=usage_dict,
            raw=completion,
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
                raise RuntimeError(
                    "OpenAI client unavailable. 请安装 openai 并提供 api_key，"
                    "或配置 base_url (OpenAI-compatible) 后重试。"
                )
            yield from self._mock_stream(messages, tools=tools)
            return

        payload: dict[str, Any] = {
            "model": self.model,
            "messages": normalize_messages(messages),
            "temperature": temperature,
            "stream": True,
        }
        if max_tokens is not None:
            payload["max_tokens"] = max_tokens
        if tools:
            payload["tools"] = list(tools)

        stream = client.chat.completions.create(**payload)
        for event in stream:
            choices = getattr(event, "choices", None) or []
            if not choices:
                continue
            delta = choices[0].delta
            text_delta = getattr(delta, "content", None) or ""
            if text_delta:
                yield StreamChunk(text_delta=text_delta, raw=event)

            delta_tool_calls = getattr(delta, "tool_calls", None) or []
            for call in delta_tool_calls:
                function = getattr(call, "function", None)
                if function is None:
                    continue
                yield StreamChunk(
                    tool_call_delta=ToolCall(
                        name=getattr(function, "name", ""),
                        arguments={"partial": getattr(function, "arguments", "")},
                    ),
                    raw=event,
                )

            if choices[0].finish_reason is not None:
                yield StreamChunk(done=True, raw=event)
                break

    def _mock_generate(
        self,
        messages: Sequence[Mapping[str, Any]],
        *,
        tools: Sequence[Mapping[str, Any]] | None = None,
    ) -> LLMResponse:
        latest = ""
        for message in reversed(messages):
            if str(message.get("role")) == "user":
                latest = str(message.get("content", ""))
                break
        text = f"[mock-openai:{self.model}] {latest}"
        tool_calls: list[ToolCall] = []
        if tools:
            first_tool = tools[0]
            function = first_tool.get("function", {}) if isinstance(first_tool, Mapping) else {}
            if isinstance(function, Mapping) and function.get("name"):
                tool_calls.append(ToolCall(name=str(function["name"]), arguments={}))

        return LLMResponse(
            text=text,
            model=self.model,
            tool_calls=tool_calls,
            finish_reason="stop",
            usage={"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
            raw=None,
        )

    def _mock_stream(
        self,
        messages: Sequence[Mapping[str, Any]],
        *,
        tools: Sequence[Mapping[str, Any]] | None = None,
    ) -> Iterable[StreamChunk]:
        text = self._mock_generate(messages, tools=tools).text
        for token in text.split(" "):
            if token:
                yield StreamChunk(text_delta=f"{token} ")
        yield StreamChunk(done=True)
