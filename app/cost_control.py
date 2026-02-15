from app.config import DAILY_BUDGET

current_spend = 0.0

def enforce_budget(estimated_cost: float):
    global current_spend

    if current_spend + estimated_cost > DAILY_BUDGET:
        raise Exception("Daily budget exceeded")

    current_spend += estimated_cost