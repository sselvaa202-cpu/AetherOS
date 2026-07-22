from app.core.config import settings
from app.llm.base import BaseLLM
from app.llm.openrouter import OpenRouterProvider


def get_llm() -> BaseLLM:
    """
    Return the configured LLM provider.
    """

    if settings.llm_provider.lower() == "openrouter":
        return OpenRouterProvider()

    raise ValueError(
        f"Unsupported LLM provider: {settings.llm_provider}"
    )