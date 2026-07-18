from langgraph.graph import START, END, StateGraph
from .state import GraphState
from backend.agents.planner_agent import planner_agent

graph_builder = StateGraph(GraphState)

graph_builder.add_node("planner_agent", planner_agent)

graph_builder.add_edge(START, "planner_agent")
graph_builder.add_edge("planner_agent", END)

final_graph = graph_builder.compile()