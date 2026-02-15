from pydantic import BaseModel

class AIRequest(BaseModel):
    prompt: str
    complexity: str  # low / high
    estimated_cost: float