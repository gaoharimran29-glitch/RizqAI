from config import llm

from graph.state import GraphState

from prompts.prompts import PLANNER_PROMPT

from schemas.planner import PlannerOutput


planner_llm = llm.with_structured_output(PlannerOutput)


def planner_agent(state: GraphState) -> GraphState:
    """
    Planner Agent
    """

    query = state["user_query"]

    plan = planner_llm.invoke(
        PLANNER_PROMPT.format(
            query=query
        )
    )

    state["plan"] = plan.model_dump()

    return state