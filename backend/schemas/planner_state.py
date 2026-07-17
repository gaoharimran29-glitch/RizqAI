from typing import List

from pydantic import BaseModel, Field
from enum import Enum


class Intent(str, Enum):
    STOCK_ANALYSIS = "stock_analysis"
    STOCK_PRICE = "stock_price"
    COMPANY_RESEARCH = "company_research"
    MARKET_NEWS = "market_news"
    PORTFOLIO_ANALYSIS = "portfolio_analysis"
    PORTFOLIO_RISK = "portfolio_risk"
    STOCK_COMPARISON = "stock_comparison"
    GENERAL_QUESTION = "general_question"
    UNRELATED = "unrelated"

class PlannerState(BaseModel):
    """
    Structured output returned by the Planner Agent.
    """

    intent: Intent = Field(
        description="Classified intent of the user's query."
    )

    company: str | None = Field(
        default=None,
        description="The company or stock symbol if present."
    )

    tasks: List[str] = Field(
        description="List of agent names to execute."
    )