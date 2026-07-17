from typing import Any, TypedDict


class GraphState(TypedDict):
    user_query: str

    plan: dict[str, Any]

    research: dict[str, Any]

    risk: dict[str, Any]

    debate: dict[str, Any]

    thesis: dict[str, Any]

    memories: list

    approval: bool