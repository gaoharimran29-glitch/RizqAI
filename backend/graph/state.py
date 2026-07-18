from typing import TypedDict, Any
from backend.schemas.planner_state import PlannerState

class GraphState(TypedDict):
    success: bool
    error: str
    user_query: str
    plan: PlannerState | None
    research: dict[str, Any]
    risk: dict[str, Any]
    debate: dict[str, Any]
    thesis: dict[str, Any]
    memories: list[dict[str, Any]]
    approval: bool