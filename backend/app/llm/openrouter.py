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

        print("Model:", settings.llm_model)

    def generate(
        self,
        prompt: str,
        max_tokens: int = 400,
    ) -> str:
        """
        Send a prompt to OpenRouter and return the response.
        """

        try:
            response = self.client.chat.completions.create(
                model=settings.llm_model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                max_tokens=max_tokens,
                temperature=settings.llm_temperature,
            )

        except Exception as e:

            print("=" * 80)
            print("OPENROUTER ERROR")
            print(type(e).__name__)
            print(str(e))
            print("=" * 80)

            return f"LLM Error: {e}"

        print("=" * 80)
        print("RAW RESPONSE")
        print(response)
        print("=" * 80)

        # Safety checks
        if response is None:
            print("ERROR: response is None")
            return "No response received."

        if response.choices is None:
            print("ERROR: response.choices is None")
            return "No choices returned."

        if len(response.choices) == 0:
            print("ERROR: response.choices is empty")
            return "Empty choices."

        message = response.choices[0].message

        print("CONTENT:", message.content)
        print("REASONING:", getattr(message, "reasoning", None))
        print("FINISH:", response.choices[0].finish_reason)

        finish_reason = response.choices[0].finish_reason

        if finish_reason == "length":
            print("WARNING: Response truncated (max_tokens reached).")

        content = (message.content or "").strip()
        reasoning = (getattr(message, "reasoning", "") or "").strip()

        if content:
            return content

        if reasoning:
            print("WARNING: Returning reasoning because content is empty.")
            return reasoning

        return "Model returned no content."