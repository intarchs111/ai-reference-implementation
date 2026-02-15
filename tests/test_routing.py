from app.routing import select_provider
from app.schemas.request import AIRequest

def test_low_complexity_routes_to_mock():
    request = AIRequest(
        prompt="Hello",
        complexity="low",
        estimated_cost=0.01
    )

    provider = select_provider(request)

    assert provider.name == "mock-model"