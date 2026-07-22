from openai import OpenAI

from app.core.config import settings
from app.llm.base import BaseLLM


class OpenRouterProvider(BaseLLM):
    """
    OpenRouter implementation of the BaseLLM interface.
    """

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.openrouter_api_key,
            base_url=settings.openrouter_base_url,
        )

    def generate(self, prompt: str) -> str:
        """
        Send a prompt to OpenRouter and return the response.
        """

        response = self.client.chat.completions.create(
            model=settings.llm_model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            max_tokens=settings.llm_max_tokens,
            temperature=settings.llm_temperature,
        )
        print(response)
        return response.choices[0].message.content
    