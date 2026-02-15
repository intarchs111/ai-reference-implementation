from fastapi import FastAPI, HTTPException
from app.schemas.request import AIRequest
from app.schemas.response import AIResponse
from app.routing import select_provider
from app.cost_control import enforce_budget
from app.governance import validate_request

app = FastAPI(title="Enterprise AI Platform")

@app.post("/generate", response_model=AIResponse)
async def generate(request: AIRequest):

    # Governance validation
    validate_request(request)

    # Cost guardrail
    enforce_budget(request.estimated_cost)

    # Model routing
    provider = select_provider(request)

    result = await provider.generate(request.prompt)

    return AIResponse(
        output=result,
        model=provider.name
    )