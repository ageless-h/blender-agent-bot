"""Azure OpenAI adapter with simplified configuration.

Provides Azure-specific configuration helpers on top of OpenAIAdapter.
"""

from __future__ import annotations

import os

from .openai_adapter import OpenAIAdapter


class AzureOpenAIAdapter(OpenAIAdapter):
    """Adapter specifically for Azure OpenAI Service.

    Simplifies Azure OpenAI configuration by handling endpoint construction
    and API version management.
    """

    def __init__(
        self,
        azure_endpoint: str | None = None,
        api_key: str | None = None,
        api_version: str = "2024-02-15-preview",
        deployment_name: str | None = None,
        timeout: float = 60.0,
        max_retries: int = 2,
    ):
        """Initialize Azure OpenAI adapter.

        Args:
            azure_endpoint: Azure OpenAI endpoint URL
                (e.g., "https://your-resource.openai.azure.com")
                Defaults to AZURE_OPENAI_ENDPOINT env var
            api_key: Azure OpenAI API key
                Defaults to AZURE_OPENAI_API_KEY env var
            api_version: Azure API version
            deployment_name: Azure deployment name (model name)
                Defaults to AZURE_OPENAI_DEPLOYMENT env var
            timeout: Request timeout in seconds
            max_retries: Number of retries on failure

        Raises:
            ValueError: If required Azure configuration is missing
        """
        # Get configuration from environment if not provided
        azure_endpoint = azure_endpoint or os.getenv("AZURE_OPENAI_ENDPOINT")
        api_key = api_key or os.getenv("AZURE_OPENAI_API_KEY")
        deployment_name = deployment_name or os.getenv("AZURE_OPENAI_DEPLOYMENT")

        if not azure_endpoint:
            raise ValueError(
                "Azure endpoint required. "
                "Provide azure_endpoint or set AZURE_OPENAI_ENDPOINT env var."
            )

        if not api_key:
            raise ValueError(
                "Azure API key required. Provide api_key or set AZURE_OPENAI_API_KEY env var."
            )

        if not deployment_name:
            raise ValueError(
                "Azure deployment name required. "
                "Provide deployment_name or set AZURE_OPENAI_DEPLOYMENT env var."
            )

        # Construct Azure base URL
        # Azure uses: {endpoint}/openai/deployments/{deployment}/chat/completions?api-version={version}
        base_url = f"{azure_endpoint.rstrip('/')}/openai/deployments/{deployment_name}"

        # Initialize parent OpenAI adapter with Azure configuration
        super().__init__(
            api_key=api_key,
            base_url=base_url,
            model=deployment_name,  # Azure uses deployment name as model
            timeout=timeout,
            max_retries=max_retries,
        )

        self.azure_endpoint = azure_endpoint
        self.api_version = api_version
        self.deployment_name = deployment_name


__all__ = ["AzureOpenAIAdapter"]
