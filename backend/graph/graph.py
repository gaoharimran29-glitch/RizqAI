from langgraph.graph import START, END, StateGraph

from graph.state import GraphState

from agents.planner_agent import planner_agent


def build_graph():

    graph_builder = StateGraph(GraphState)

    # Register Nodes
    graph_builder.add_node("planner", planner_agent)

    # Entry Point
    graph_builder.add_edge(START, "planner")

    # Temporary End
    graph_builder.add_edge("planner", END)

    return graph_builder.compile()


graph = build_graph()