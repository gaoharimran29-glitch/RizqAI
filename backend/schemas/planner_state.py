from typing import List

from pydantic import BaseModel, Field


class PlannerOutput(BaseModel):
    """
    Structured output returned by the Planner Agent.
    """

    intent: str = Field(
        description="The user's investment intent."
    )

    company: str | None = Field(
        default=None,
        description="The company or stock symbol if present."
    )

    tasks: List[str] = Field(
        description="List of agent names to execute."
    )