from config import llm
from graph.state import GraphState
from prompts.prompts import PLANNER_PROMPT
from schemas.planner_state import PlannerState

planner_llm = llm.with_structured_output(PlannerState)

def planner_agent(state: GraphState) -> GraphState:
    """Planner Agent"""

    query = state["user_query"]

    plan = planner_llm.invoke(
        PLANNER_PROMPT.format(
            query=query
        )
    )

    state["plan"] = plan

    return state