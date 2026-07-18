from backend.config import llm
from backend.graph.state import GraphState
from backend.prompts.prompts import PLANNER_PROMPT
from backend.schemas.planner_state import PlannerState
from langchain_core.prompts import ChatPromptTemplate
from langsmith import traceable

@traceable(name="planner_agent")
async def planner_agent(state: GraphState) -> GraphState:
    """Planner Agent classify the user intent and plan the agents to run"""

    print("Planner agent Working....")

    try:
        planner_llm = llm.with_structured_output(PlannerState)
        prompt = ChatPromptTemplate.from_messages([("system", PLANNER_PROMPT) , ("human" , "{user_query}")])
        messages = await prompt.ainvoke({"user_query": state["user_query"]})
        plan = await planner_llm.ainvoke(messages)

    except Exception as e:
        return {
            "success": False ,
            "error" : str(e)
        }

    return {
        "success": True ,
        "plan" : plan
    }