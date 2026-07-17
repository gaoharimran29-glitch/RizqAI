from graph.graph import graph

initial_state = {
    "user_query": "Should I invest in NVIDIA?",

    "plan": None,

    "research": {},

    "risk": {},

    "debate": {},

    "thesis": {},

    "memories": [],

    "approval": False
}

result = graph.invoke(initial_state)

print(result["plan"])