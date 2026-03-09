"""Test suite for LLM adapters.

Tests the base adapter interface, capabilities, and concrete implementations.
"""

import pytest

from blender_agent_core.llm import (
    ErrorAdapter,
    FallbackAdapter,
    LLMAdapter,
    LLMResponse,
    MockAdapter,
    ModelCapabilities,
    StreamChunk,
)


class TestModelCapabilities:
    """Test ModelCapabilities dataclass."""

    def test_default_capabilities(self):
        """Test default capability values."""
        caps = ModelCapabilities()

        assert caps.supports_tool_calling is False
        assert caps.supports_vision is False
        assert caps.supports_streaming is False
        assert caps.supports_parallel_tools is False
        assert caps.max_context_tokens == 4096
        assert caps.max_output_tokens == 2048
        assert caps.model_name == "unknown"
        assert caps.provider == "unknown"

    def test_custom_capabilities(self):
        """Test custom capability configuration."""
        caps = ModelCapabilities(
            supports_tool_calling=True,
            supports_vision=True,
            max_context_tokens=128000,
            model_name="gpt-4",
            provider="openai",
        )

        assert caps.supports_tool_calling is True
        assert caps.supports_vision is True
        assert caps.max_context_tokens == 128000
        assert caps.model_name == "gpt-4"
        assert caps.provider == "openai"


class TestLLMResponse:
    """Test LLMResponse class."""

    def test_basic_response(self):
        """Test basic response without tool calls."""
        response = LLMResponse(content="Hello, world!")

        assert response.content == "Hello, world!"
        assert response.tool_calls == []
        assert response.finish_reason == "stop"
        assert response.usage == {}

    def test_response_with_tool_calls(self):
        """Test response with tool calls."""
        tool_calls = [
            {"name": "get_weather", "arguments": {"location": "SF"}},
        ]
        response = LLMResponse(
            content="Let me check the weather.",
            tool_calls=tool_calls,
            finish_reason="tool_calls",
            usage={"prompt_tokens": 10, "completion_tokens": 5},
        )

        assert response.content == "Let me check the weather."
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0]["name"] == "get_weather"
        assert response.finish_reason == "tool_calls"
        assert response.usage["total_tokens"] == 15


class TestStreamChunk:
    """Test StreamChunk class."""

    def test_content_chunk(self):
        """Test content-only chunk."""
        chunk = StreamChunk(delta="Hello")

        assert chunk.delta == "Hello"
        assert chunk.tool_call_delta is None
        assert chunk.done is False

    def test_final_chunk(self):
        """Test final chunk with done flag."""
        chunk = StreamChunk(delta="", done=True)

        assert chunk.delta == ""
        assert chunk.done is True

    def test_tool_call_chunk(self):
        """Test chunk with tool call delta."""
        tool_delta = {"tool_calls": [{"name": "test"}]}
        chunk = StreamChunk(tool_call_delta=tool_delta, done=True)

        assert chunk.tool_call_delta == tool_delta
        assert chunk.done is True


class TestMockAdapter:
    """Test MockAdapter implementation."""

    @pytest.mark.asyncio
    async def test_basic_generation(self):
        """Test basic text generation."""
        adapter = MockAdapter(response_text="Test response")

        response = await adapter.generate(messages=[{"role": "user", "content": "Hello"}])

        assert response.content == "Test response"
        assert response.tool_calls is None
        assert response.finish_reason == "stop"

    @pytest.mark.asyncio
    async def test_tool_calling(self):
        """Test tool calling simulation."""
        adapter = MockAdapter(supports_tools=True)
        tools = [{"name": "test_tool", "description": "A test tool"}]

        response = await adapter.generate(
            messages=[{"role": "user", "content": "Use a tool"}],
            tools=tools,
        )

        assert response.tool_calls is not None
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0]["name"] == "test_tool"

    @pytest.mark.asyncio
    async def test_streaming(self):
        """Test streaming response."""
        adapter = MockAdapter(
            response_text="Hello world",
            stream_delay=0.01,
        )

        chunks = []
        async for chunk in adapter.stream(messages=[{"role": "user", "content": "Hi"}]):
            chunks.append(chunk)

        # Should have word chunks + final chunk
        assert len(chunks) > 2
        assert chunks[-1].done is True

        # Reconstruct content
        content = "".join(c.delta for c in chunks if not c.done)
        assert content == "Hello world"

    @pytest.mark.asyncio
    async def test_capabilities(self):
        """Test capability reporting."""
        adapter = MockAdapter(supports_tools=True, supports_streaming=True)
        caps = adapter.get_capabilities()

        assert caps.supports_tool_calling is True
        assert caps.supports_streaming is True
        assert caps.model_name == "mock-model"
        assert caps.provider == "mock"


class TestErrorAdapter:
    """Test ErrorAdapter for error handling."""

    @pytest.mark.asyncio
    async def test_generate_raises_error(self):
        """Test that generate raises configured error."""
        adapter = ErrorAdapter(error_message="Test error")

        with pytest.raises(RuntimeError, match="Test error"):
            await adapter.generate(messages=[])

    @pytest.mark.asyncio
    async def test_stream_raises_error(self):
        """Test that stream raises configured error."""
        adapter = ErrorAdapter(error_message="Stream error")

        with pytest.raises(RuntimeError, match="Stream error"):
            async for _ in adapter.stream(messages=[]):
                pass

    def test_capabilities(self):
        """Test error adapter capabilities."""
        adapter = ErrorAdapter()
        caps = adapter.get_capabilities()

        assert caps.supports_tool_calling is False
        assert caps.supports_streaming is False
        assert caps.model_name == "error-model"


class TestFallbackAdapter:
    """Test FallbackAdapter for tool calling simulation."""

    @pytest.mark.asyncio
    async def test_wraps_base_adapter(self):
        """Test that fallback wraps base adapter."""
        base = MockAdapter(response_text="Base response")
        fallback = FallbackAdapter(base)

        response = await fallback.generate(messages=[{"role": "user", "content": "Hello"}])

        assert "Base response" in response.content or response.content == "Base response"

    @pytest.mark.asyncio
    async def test_injects_tool_prompt(self):
        """Test that tools are injected into system message."""
        base = MockAdapter()
        fallback = FallbackAdapter(base)

        tools = [
            {
                "name": "test_tool",
                "description": "A test tool",
                "parameters": {"type": "object"},
            }
        ]

        # The fallback should inject tool descriptions
        response = await fallback.generate(
            messages=[{"role": "user", "content": "Hello"}],
            tools=tools,
        )

        # Response should be generated (no errors)
        assert response.content is not None

    @pytest.mark.asyncio
    async def test_parses_tool_calls(self):
        """Test parsing tool calls from JSON response."""
        # Create a mock that returns JSON tool call
        base = MockAdapter(
            response_text='```json\n{"tool": "get_weather", "arguments": {"location": "SF"}}\n```'
        )
        fallback = FallbackAdapter(base)

        tools = [{"name": "get_weather", "description": "Get weather"}]
        response = await fallback.generate(
            messages=[{"role": "user", "content": "Weather?"}],
            tools=tools,
        )

        # Should parse the tool call
        assert response.tool_calls is not None
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0]["name"] == "get_weather"
        assert response.tool_calls[0]["arguments"]["location"] == "SF"

    @pytest.mark.asyncio
    async def test_streaming_with_fallback(self):
        """Test streaming through fallback adapter."""
        base = MockAdapter(response_text="Test response", stream_delay=0.01)
        fallback = FallbackAdapter(base)

        chunks = []
        async for chunk in fallback.stream(messages=[{"role": "user", "content": "Hi"}]):
            chunks.append(chunk)

        assert len(chunks) > 0
        assert chunks[-1].done is True

    def test_capabilities_inheritance(self):
        """Test that capabilities are inherited from base."""
        base = MockAdapter(supports_tools=True)
        fallback = FallbackAdapter(base)

        caps = fallback.get_capabilities()

        # Tool calling should be False (we simulate it)
        assert caps.supports_tool_calling is False
        # Other capabilities inherited
        assert caps.model_name == "mock-model (fallback)"


@pytest.fixture
def sample_messages():
    """Sample message history for testing."""
    return [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"},
    ]


@pytest.fixture
def sample_tools():
    """Sample tool definitions for testing."""
    return [
        {
            "name": "get_weather",
            "description": "Get current weather",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"},
                },
                "required": ["location"],
            },
        },
    ]


class TestAdapterInterface:
    """Test the LLMAdapter interface contract."""

    @pytest.mark.asyncio
    async def test_adapter_must_implement_generate(self):
        """Test that adapters must implement generate."""

        class IncompleteAdapter(LLMAdapter):
            def get_capabilities(self):
                return ModelCapabilities()

            async def stream(self, messages, tools=None, **kwargs):
                yield StreamChunk(done=True)

        adapter = IncompleteAdapter()

        # Should raise NotImplementedError or similar
        with pytest.raises((NotImplementedError, TypeError)):
            await adapter.generate(messages=[])

    @pytest.mark.asyncio
    async def test_adapter_must_implement_stream(self):
        """Test that adapters must implement stream."""

        class IncompleteAdapter(LLMAdapter):
            def get_capabilities(self):
                return ModelCapabilities()

            async def generate(self, messages, tools=None, **kwargs):
                return LLMResponse(content="test")

        adapter = IncompleteAdapter()

        # Should raise NotImplementedError or similar
        with pytest.raises((NotImplementedError, TypeError)):
            async for _ in adapter.stream(messages=[]):
                pass
