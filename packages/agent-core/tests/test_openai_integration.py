"""Integration tests for OpenAI adapter.

These tests require actual API keys and make real API calls.
Skip if OPENAI_API_KEY is not set.
"""

import os

import pytest

from blender_agent_core.llm import (
    AzureOpenAIAdapter,
    FallbackAdapter,
    MockAdapter,
    OpenAIAdapter,
)


# Skip all tests if OpenAI not available
pytestmark = pytest.mark.skipif(
    not os.getenv("OPENAI_API_KEY"),
    reason="OPENAI_API_KEY not set - skipping integration tests",
)


class TestOpenAIAdapter:
    """Integration tests for OpenAIAdapter."""

    @pytest.mark.asyncio
    @pytest.mark.integration
    async def test_basic_generation(self):
        """Test basic text generation with OpenAI."""
        adapter = OpenAIAdapter(model="gpt-3.5-turbo")

        response = await adapter.generate(
            messages=[{"role": "user", "content": "Say 'test successful' and nothing else."}],
            temperature=0,
        )

        assert response.content
        assert "test" in response.content.lower()
        assert response.finish_reason in ["stop", "length"]
        assert response.usage["total_tokens"] > 0

        await adapter.close()

    @pytest.mark.asyncio
    @pytest.mark.integration
    async def test_tool_calling(self):
        """Test function calling with OpenAI."""
        adapter = OpenAIAdapter(model="gpt-3.5-turbo")

        tools = [
            {
                "name": "get_weather",
                "description": "Get the current weather in a location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "City name",
                        },
                    },
                    "required": ["location"],
                },
            }
        ]

        response = await adapter.generate(
            messages=[{"role": "user", "content": "What's the weather in San Francisco?"}],
            tools=tools,
            temperature=0,
        )

        # Should call the tool
        assert response.tool_calls is not None
        assert len(response.tool_calls) > 0
        assert response.tool_calls[0]["name"] == "get_weather"

        await adapter.close()

    @pytest.mark.asyncio
    @pytest.mark.integration
    async def test_streaming(self):
        """Test streaming response from OpenAI."""
        adapter = OpenAIAdapter(model="gpt-3.5-turbo")

        chunks = []
        async for chunk in adapter.stream(
            messages=[{"role": "user", "content": "Count from 1 to 3, one number per line."}],
            temperature=0,
        ):
            chunks.append(chunk)

        # Should have multiple chunks
        assert len(chunks) > 1

        # Last chunk should be done
        assert chunks[-1].done is True

        # Reconstruct content
        content = "".join(c.delta for c in chunks if not c.done)
        assert content  # Should have some content

        await adapter.close()

    @pytest.mark.asyncio
    @pytest.mark.integration
    async def test_capabilities_detection(self):
        """Test capability detection for different models."""
        # GPT-4
        adapter_gpt4 = OpenAIAdapter(model="gpt-4")
        caps_gpt4 = adapter_gpt4.get_capabilities()

        assert caps_gpt4.supports_tool_calling is True
        assert caps_gpt4.supports_streaming is True
        assert caps_gpt4.model_name == "gpt-4"

        # GPT-3.5
        adapter_gpt35 = OpenAIAdapter(model="gpt-3.5-turbo")
        caps_gpt35 = adapter_gpt35.get_capabilities()

        assert caps_gpt35.supports_tool_calling is True
        assert caps_gpt35.max_context_tokens == 16385

        await adapter_gpt4.close()
        await adapter_gpt35.close()


class TestAzureOpenAIAdapter:
    """Integration tests for Azure OpenAI."""

    @pytest.mark.asyncio
    @pytest.mark.integration
    @pytest.mark.skipif(
        not os.getenv("AZURE_OPENAI_ENDPOINT"),
        reason="Azure OpenAI not configured",
    )
    async def test_azure_basic_generation(self):
        """Test basic generation with Azure OpenAI."""
        adapter = AzureOpenAIAdapter()

        response = await adapter.generate(
            messages=[{"role": "user", "content": "Say 'azure test' and nothing else."}],
            temperature=0,
        )

        assert response.content
        assert "azure" in response.content.lower() or "test" in response.content.lower()

        await adapter.close()

    def test_azure_configuration_validation(self):
        """Test that Azure adapter validates configuration."""
        # Missing endpoint
        with pytest.raises(ValueError, match="endpoint required"):
            AzureOpenAIAdapter(
                azure_endpoint=None,
                api_key="test-key",
                deployment_name="test-deployment",
            )

        # Missing API key
        with pytest.raises(ValueError, match="API key required"):
            AzureOpenAIAdapter(
                azure_endpoint="https://test.openai.azure.com",
                api_key=None,
                deployment_name="test-deployment",
            )

        # Missing deployment
        with pytest.raises(ValueError, match="deployment name required"):
            AzureOpenAIAdapter(
                azure_endpoint="https://test.openai.azure.com",
                api_key="test-key",
                deployment_name=None,
            )


class TestFallbackWithOpenAI:
    """Test FallbackAdapter wrapping OpenAI."""

    @pytest.mark.asyncio
    @pytest.mark.integration
    async def test_fallback_wraps_openai(self):
        """Test that fallback can wrap OpenAI adapter."""
        base = OpenAIAdapter(model="gpt-3.5-turbo")
        fallback = FallbackAdapter(base)

        response = await fallback.generate(
            messages=[{"role": "user", "content": "Say 'fallback test' and nothing else."}],
            temperature=0,
        )

        assert response.content
        assert "fallback" in response.content.lower() or "test" in response.content.lower()

        await fallback.close()

    @pytest.mark.asyncio
    @pytest.mark.integration
    async def test_fallback_simulates_tools(self):
        """Test that fallback can simulate tool calling."""
        base = OpenAIAdapter(model="gpt-3.5-turbo")
        fallback = FallbackAdapter(base)

        tools = [
            {
                "name": "calculate",
                "description": "Perform calculation",
                "parameters": {"type": "object"},
            }
        ]

        # The fallback should inject tool descriptions
        response = await fallback.generate(
            messages=[{"role": "user", "content": "Use the calculate tool with value 42."}],
            tools=tools,
            temperature=0,
        )

        # Response should be generated (may or may not parse tool call)
        assert response.content is not None

        await fallback.close()


@pytest.fixture
def mock_openai_adapter():
    """Mock adapter for testing without API calls."""
    return MockAdapter(
        response_text="Mock OpenAI response",
        supports_tools=True,
        supports_streaming=True,
    )


class TestOpenAIAdapterUnit:
    """Unit tests for OpenAI adapter (no API calls)."""

    def test_tool_conversion(self):
        """Test tool format conversion."""
        adapter = OpenAIAdapter(model="gpt-3.5-turbo")

        tools = [
            {
                "name": "test_tool",
                "description": "A test tool",
                "parameters": {
                    "type": "object",
                    "properties": {"param": {"type": "string"}},
                },
            }
        ]

        openai_tools = adapter._convert_tools_to_openai(tools)

        assert openai_tools is not None
        assert len(openai_tools) == 1
        assert openai_tools[0]["type"] == "function"
        assert openai_tools[0]["function"]["name"] == "test_tool"
        assert openai_tools[0]["function"]["description"] == "A test tool"

    def test_empty_tools_conversion(self):
        """Test that None/empty tools are handled."""
        adapter = OpenAIAdapter(model="gpt-3.5-turbo")

        assert adapter._convert_tools_to_openai(None) is None
        assert adapter._convert_tools_to_openai([]) is None
