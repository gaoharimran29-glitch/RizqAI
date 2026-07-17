```
backend/

│
├── agents/
│ ├── planner_agent.py # Creates a plan of action based on the user's query.
│ │ # Example: "Should I buy NVIDIA?" -> Fetch stock data,
│ │ # check portfolio, analyze risk, etc.
│ │
│ ├── research_agent.py # Performs stock research using APIs.
│ │ # Fetches stock price, fundamentals, company information,
│ │ # latest news and market data.
│ │
│ ├── risk_agent.py # Calculates portfolio and stock risk.
│ │ # Checks diversification, volatility, sector exposure,
│ │ # and assigns a risk score.
│ │
│ ├── debate_agent.py # Generates Bull vs Bear analysis.
│ │ # Gives both positive and negative investment arguments.
│ │
│ └── thesis_agent.py # Generates the final investment thesis.
│ # Provides recommendation, confidence score,
│ # allocation suggestions and reasoning.
│
├── graph/
│ ├── graph.py # Main LangGraph workflow.
│ │ # Connects all agents and defines the execution flow.
│ │
│ └── state.py # Stores the shared LangGraph state.
│ # Contains query, memories, portfolio data,
│ # research results and user feedback.
│
├── memory/
│ ├── memory_manager.py # Handles long-term memory.
│ │ # Stores investment preferences, portfolio behaviour,
│ │ # previous decisions and user corrections.
│ │
│ └── memory_utils.py # Helper functions for saving, retrieving,
│ # updating and summarizing memories.
│
├── tools/
│ ├── stock_tools.py # Wrapper around stock APIs (Yahoo Finance).
│ │ # Used to fetch prices, company details,
│ │ # historical data and financial statements.
│ │
│ └── news_tools.py # Fetches stock and market related news.
│ # Used by the Research Agent.
│
├── api/
│ └── routes.py # FastAPI routes for frontend communication.
│ # Example:
│ # /ask
│ # /portfolio
│ # /memory
│ # /paper-trade
│
├── prompts/
│ └── prompts.py # Stores all LLM prompts in one place.
│ # Includes prompts for planner, research,
│ # debate, risk analysis and thesis generation.
│
├── database/
│ └── db.py # SQLite database setup.
│ # Stores memories, trade history,
│ # portfolio data and investment journal entries.
│
├── main.py # FastAPI application entry point.
│ # Initializes LangGraph and API routes.
│
├── config.py # Stores API keys, environment variables
│ # and application configurations.
│
└── requirements.txt # Python dependencies for the backend.
```