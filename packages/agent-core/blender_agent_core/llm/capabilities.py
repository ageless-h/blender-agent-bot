"""Model capabilities detection."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ModelCapabilities:
    """Describes what a specific LLM model can do.
    
    Used by Agent Core to adapt behavior based on model capabilities.
    """
    
    # Core capabilities
    supports_tool_calling: bool = False
    supports_vision: bool = False
    supports_streaming: bool = False
    supports_parallel_tools: bool = False
    
    # Context and limits
    max_context_tokens: int = 4096
    max_output_tokens: int = 2048
    
    # Model identification
    model_name: str = "unknown"
    provider: str = "unknown"
    
    def __str__(self) -> str:
        caps = []
        if self.supports_tool_calling:
            caps.append("tool_calling")
        if self.supports_vision:
            caps.append("vision")
        if self.supports_streaming:
            caps.append("streaming")
        if self.supports_parallel_tools:
            caps.append("parallel_tools")
        
        return f"{self.model_name} ({self.provider}): {', '.join(caps) if caps else 'basic'}"


# Predefined capabilities for common models
GPT4_CAPABILITIES = ModelCapabilities(
    supports_tool_calling=True,
    supports_vision=True,
    supports_streaming=True,
    supports_parallel_tools=True,
    max_context_tokens=128000,
    max_output_tokens=4096,
    model_name="gpt-4",
    provider="openai",
)

GPT4O_CAPABILITIES = ModelCapabilities(
    supports_tool_calling=True,
    supports_vision=True,
    supports_streaming=True,
    supports_parallel_tools=True,
    max_context_tokens=128000,
    max_output_tokens=16384,
    model_name="gpt-4o",
    provider="openai",
)

CLAUDE_OPUS_CAPABILITIES = ModelCapabilities(
    supports_tool_calling=True,
    supports_vision=True,
    supports_streaming=True,
    supports_parallel_tools=False,
    max_context_tokens=200000,
    max_output_tokens=4096,
    model_name="claude-opus-4",
    provider="anthropic",
)

CLAUDE_SONNET_CAPABILITIES = ModelCapabilities(
    supports_tool_calling=True,
    supports_vision=True,
    supports_streaming=True,
    supports_parallel_tools=False,
    max_context_tokens=200000,
    max_output_tokens=8192,
    model_name="claude-sonnet-4",
    provider="anthropic",
)


__all__ = [
    "ModelCapabilities",
    "GPT4_CAPABILITIES",
    "GPT4O_CAPABILITIES",
    "CLAUDE_OPUS_CAPABILITIES",
    "CLAUDE_SONNET_CAPABILITIES",
]
