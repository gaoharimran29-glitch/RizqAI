from langgraph.graph import START, END, StateGraph
from graph.state import GraphState
from agents.planner_agent import planner_agent

graph_builder = StateGraph(GraphState)

graph_builder.add_node("planner_agent", planner_agent)

graph_builder.add_edge(START, "planner_agent")
graph_builder.add_edge("planner_agent", END)

graph_builder.compile()