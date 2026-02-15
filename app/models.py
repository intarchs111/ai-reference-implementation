from dataclasses import dataclass

@dataclass
class ProviderConfig:
    name: str
    cost_per_token: float
    max_tokens: int