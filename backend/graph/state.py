from typing import TypedDict, Any
from schemas.planner_state import PlannerState

class GraphState(TypedDict):

    user_query: str
    plan: PlannerState | None
    research: dict[str, Any]
    risk: dict[str, Any]
    debate: dict[str, Any]
    thesis: dict[str, Any]
    memories: list[dict[str, Any]]
    approval: bool