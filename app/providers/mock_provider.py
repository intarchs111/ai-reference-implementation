from app.providers.base import BaseProvider

class MockProvider(BaseProvider):
    name = "mock-model"

    async def generate(self, prompt: str) -> str:
        return f"[Mock response] {prompt}"