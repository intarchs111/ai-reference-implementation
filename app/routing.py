from app.providers.mock_provider import MockProvider
from app.providers.openai_provider import OpenAIProvider

def select_provider(request):
    if request.complexity == "low":
        return MockProvider()
    else:
        return OpenAIProvider()