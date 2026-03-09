"""LLM adapter module.

Provides unified interface for different LLM providers.
"""

from .anthropic_adapter import AnthropicAdapter
from .azure_adapter import AzureOpenAIAdapter
from .base import LLMAdapter, LLMResponse, StreamChunk
from .capabilities import ModelCapabilities
from .fallback_adapter import FallbackAdapter
from .mock_adapter import ErrorAdapter, MockAdapter
from .openai_adapter import OpenAIAdapter

__all__ = [
    "LLMAdapter",
    "LLMResponse",
    "StreamChunk",
    "ModelCapabilities",
    "FallbackAdapter",
    "MockAdapter",
    "ErrorAdapter",
    "OpenAIAdapter",
    "AzureOpenAIAdapter",
    "AnthropicAdapter",
]
