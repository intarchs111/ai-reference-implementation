from app.providers.base import BaseProvider

class OpenAIProvider(BaseProvider):
    name = "openai-model"

    async def generate(self, prompt: str) -> str:
        # Placeholder for real API call
        return f"[OpenAI simulated response] {prompt}"