from __future__ import annotations

import importlib
from collections.abc import Iterable, Mapping, Sequence
from typing import Any

from .base import LLMAdapter, LLMResponse, ModelCapabilities, StreamChunk, ToolCall


class GoogleAdapter(LLMAdapter):
    """Gemini 适配器（google-generativeai）。"""

    def __init__(
        self,
        model: str,
        *,
        api_key: str | None = None,
        timeout: float = 60.0,
        allow_mock: bool = False,
    ) -> None:
        super().__init__(
            model,
            api_key=api_key,
            timeout=timeout,
            allow_mock=allow_mock,
        )
        self._genai = None

    def get_capabilities(self) -> ModelCapabilities:
        model = self.model.lower()
        return ModelCapabilities(
            tool_calling=True,
            vision=True,
            parallel_tools="flash" not in model,
            max_context=2_000_000,
        )

    def _get_genai(self) -> Any | None:
        if self._genai is not None:
            return self._genai
        if not self.api_key:
            return None
        try:
            genai = importlib.import_module("google.generativeai")
        except Exception:  # pragma: no cover - optional dependency
            return None
        genai.configure(api_key=self.api_key)
        self._genai = genai
        return genai

    def _messages_to_prompt(self, messages: Sequence[Mapping[str, Any]]) -> str:
        rows: list[str] = []
        for message in messages:
            role = str(message.get("role", "user"))
            content = str(message.get("content", ""))
            rows.append(f"[{role}] {content}")
        return "\n".join(rows)

    def generate(
        self,
        messages: Sequence[Mapping[str, Any]],
        *,
        tools: Sequence[Mapping[str, Any]] | None = None,
        temperature: float = 0.2,
        max_tokens: int | None = None,
    ) -> LLMResponse:
        genai = self._get_genai()
        if genai is None:
            if not self.allow_mock:
                raise RuntimeError("Google client unavailable. 请安装 google-generativeai 并配置 api_key 后重试。")
            return self._mock_generate(messages)

        prompt = self._messages_to_prompt(messages)
        model = genai.GenerativeModel(model_name=self.model)
        generation_config: dict[str, Any] = {"temperature": temperature}
        if max_tokens is not None:
            generation_config["max_output_tokens"] = max_tokens

        response = model.generate_content(
            prompt,
            generation_config=generation_config,
        )

        text = str(getattr(response, "text", "") or "")
        tool_calls: list[ToolCall] = []
        for candidate in getattr(response, "candidates", []) or []:
            content = getattr(candidate, "content", None)
            for part in getattr(content, "parts", []) or []:
                function_call = getattr(part, "function_call", None)
                if function_call is not None:
                    tool_calls.append(
                        ToolCall(
                            name=str(getattr(function_call, "name", "")),
                            arguments=dict(getattr(function_call, "args", {}) or {}),
                        )
                    )

        return LLMResponse(
            text=text,
            model=self.model,
            tool_calls=tool_calls,
            finish_reason="stop",
            usage={},
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
        genai = self._get_genai()
        if genai is None:
            if not self.allow_mock:
                raise RuntimeError("Google client unavailable. 请安装 google-generativeai 并配置 api_key 后重试。")
            yield from self._mock_stream(messages)
            return

        prompt = self._messages_to_prompt(messages)
        model = genai.GenerativeModel(model_name=self.model)
        generation_config: dict[str, Any] = {"temperature": temperature}
        if max_tokens is not None:
            generation_config["max_output_tokens"] = max_tokens

        stream = model.generate_content(
            prompt,
            generation_config=generation_config,
            stream=True,
        )
        for chunk in stream:
            text = str(getattr(chunk, "text", "") or "")
            if text:
                yield StreamChunk(text_delta=text, raw=chunk)
        yield StreamChunk(done=True)

    def _mock_generate(self, messages: Sequence[Mapping[str, Any]]) -> LLMResponse:
        latest = ""
        for message in reversed(messages):
            if str(message.get("role")) == "user":
                latest = str(message.get("content", ""))
                break
        return LLMResponse(
            text=f"[mock-google:{self.model}] {latest}",
            model=self.model,
            finish_reason="stop",
        )

    def _mock_stream(self, messages: Sequence[Mapping[str, Any]]) -> Iterable[StreamChunk]:
        text = self._mock_generate(messages).text
        for token in text.split(" "):
            if token:
                yield StreamChunk(text_delta=f"{token} ")
        yield StreamChunk(done=True)
