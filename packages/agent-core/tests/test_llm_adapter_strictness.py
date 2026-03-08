import pytest

from llm import AnthropicAdapter, GoogleAdapter, OpenAIAdapter


MESSAGES = [{"role": "user", "content": "hello"}]


def test_openai_adapter_raises_when_mock_disabled() -> None:
    adapter = OpenAIAdapter(model="gpt-4o", api_key=None, base_url=None)
    with pytest.raises(RuntimeError, match="OpenAI client unavailable"):
        adapter.generate(MESSAGES)


def test_openai_adapter_can_use_mock_when_enabled() -> None:
    adapter = OpenAIAdapter(model="gpt-4o", api_key=None, base_url=None, allow_mock=True)
    response = adapter.generate(MESSAGES)
    assert response.text.startswith("[mock-openai")


def test_anthropic_adapter_raises_when_mock_disabled() -> None:
    adapter = AnthropicAdapter(model="claude-3-5-sonnet", api_key=None)
    with pytest.raises(RuntimeError, match="Anthropic client unavailable"):
        adapter.generate(MESSAGES)


def test_google_adapter_raises_when_mock_disabled() -> None:
    adapter = GoogleAdapter(model="gemini-1.5-pro", api_key=None)
    with pytest.raises(RuntimeError, match="Google client unavailable"):
        adapter.generate(MESSAGES)
