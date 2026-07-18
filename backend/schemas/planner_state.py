from enum import Enum
from typing import List
from pydantic import BaseModel, Field
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
class Agent(str, Enum):
    RESEARCH = "research_agent"
    RISK = "risk_agent"
    DEBATE = "debate_agent"
    THESIS = "thesis_agent"

class PlannerState(BaseModel):
    intent: Intent = Field(description="Classified intent of the user's query.")
    companies: List[str] = Field(default_factory=list, description="Companies or stock symbols mentioned by the user.")
    tasks: List[Agent] = Field(description="Agents that should be executed.")