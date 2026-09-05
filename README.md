<div align="center">
  <picture>
    <img alt="RizqAI Logo" src="assets/banner.svg" width="100%">
  </picture>
</div>

<p align="center">
  <b>An autonomous, multi-agent financial intelligence and investment research engine orchestrated via LangGraph, powered by structured LLM reasoning, real-time market data ingestion, and adversarial Bull-Bear debate synthesis.</b>
</p>

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/LangGraph-v1.1.10-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain-ai.github.io/langgraph/)
[![LangChain](https://img.shields.io/badge/LangChain-v1.2.17-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://www.langchain.com/)
[![LangSmith](https://img.shields.io/badge/LangSmith-Traceable-FF8800?style=for-the-badge&logo=langchain&logoColor=white)](https://smith.langchain.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.141.1-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Next.js-16.2.10-000000?style=for-the-badge&logo=next.js&logoColor=white)](https://nextjs.org/)
[![React](https://img.shields.io/badge/React-19.2.4-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-v4.0-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)
[![SQLite](https://img.shields.io/badge/SQLite-AsyncCheckpointer-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

</div>

---

## 📚 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Prerequisites](#-prerequisites)
- [Installation](#️-installation)
- [Usage](#-usage)
- [LLM Client Behavior & Security Considerations](#-llm-client-behavior--security-considerations)
- [Known Limitations](#-known-limitations)
- [Project Structure](#️-project-structure)
- [License](#-license)
- [Author](#-author)

---

<a id="-overview"></a>
## 🔍 Overview

**RizqAI** (derived from the Arabic *Rizq* — provision, sustenance) is an enterprise-grade, agentic equity research system designed to emulate an institutional investment committee. Rather than relying on monolithic LLM prompts that suffer from hallucinations, cognitive bias, and stale training data, RizqAI decomposes the financial research workflow into a deterministic, stateful multi-agent DAG (Directed Acyclic Graph) powered by **LangGraph**.

When a user submits a market query, RizqAI routes the request through a specialized hierarchy of autonomous agents:

```
                                  ┌────────────────────────┐
                                  │       User Query       │
                                  └───────────┬────────────┘
                                              │
                                              ▼
                                 ┌──────────────────────────┐
                                 │     Guardrail Agent      │
                                 │   (Groq / GPT-OSS-20B)   │
                                 └──────┬────────────┬──────┘
                                        │            │
                  ┌─────────────────────┘            └──────────────────────┐
                  │ [company_analysis]                                      │ [general_finance]
                  ▼                                                         ▼
      ┌──────────────────────┐                                 ┌─────────────────────────┐
      │    Planner Agent     │                                 │  General Finance Agent  │
      │(Gemini 3.7 + Fallbacks)                                │  (Concept / Note Q&A)   │
      └──────────┬───────────┘                                 └────────────┬────────────┘
                 │                                                          │
                 ▼                                                          │
     ┌────────────────────────┐                                             │
     │     Research Agent     │ ◄── [yfinance API + NewsAPI Tools]          │
     └───────────┬────────────┘                                             │
                 │                                                          │
                 ▼                                                          │
     ┌────────────────────────┐                                             │
     │       Risk Agent       │ ◄── [Downside / Volatility / Scoring]       │
     └───────────┬────────────┘                                             │
                 │                                                          │
                 ▼                                                          │
     ┌────────────────────────┐                                             │
     │      Debate Agent      │ ◄── [Bull Case vs. Bear Case Clash]         │
     └───────────┬────────────┘                                             │
                 │                                                          │
                 ▼                                                          │
     ┌────────────────────────┐                                             │
     │      Thesis Agent      │ ◄── [Recommendation / Confidence / Memo]    │
     └───────────┬────────────┘                                             │
                 │                                                          │
                 └──────────────────────┐    ┌──────────────────────────────┘
                                        ▼    ▼
                                 ┌───────────────┐
                                 │  Final Output │
                                 │ (SSE Stream)  │
                                 └───────────────┘
```

The system is engineered as an asynchronous decoupled architecture:
1. **The Backend**: A high-performance **FastAPI** service coordinating the **LangGraph StateGraph**, streaming real-time agent state mutations via **Server-Sent Events (SSE)**, and persisting threads and checkpoints in **SQLite** via SQLAlchemy 2.0 and `AsyncSqliteSaver`.
2. **The Frontend**: A responsive, modern financial terminal built on **Next.js 16 (App Router)**, **React 19**, and **Tailwind CSS v4**, delivering sub-second live execution timeline tracking, expandable telemetry logs, and structured financial memos.

---

<a id="-features"></a>
## ✨ Features

- **Autonomous Multi-Agent DAG Execution**: Orchestrated via LangGraph state graphs with conditional edge transitions, cyclical evaluation loops, and centralized `GraphState` shared memory.
- **Dynamic Runtime Query Planning**: The `PlannerAgent` decomposes complex natural language prompts, automatically resolves company names into validated stock ticker symbols (e.g. *"Apple"* $\rightarrow$ `AAPL`), and schedules only the necessary downstream agents.
- **Real-Time Fundamental & Technical Data Ingestion**: The `ResearchAgent` operates as a ReAct tool-calling agent equipped with Yahoo Finance (`yfinance`) integration for live bid/ask prices, day range, 52-week high/lows, market cap, P/E multiples, forward P/E, EPS, dividend yields, and beta metrics.
- **Catalyst & Market News Aggregation**: Integrated `NewsApiClient` querying real-time, sentiment-driving headlines and macro events over active coverage tickers.
- **Multidimensional Risk Scoring Engine**: The `RiskAgent` computes an algorithmic risk score scaled strictly from `1` (lowest risk) to `10` (highest risk), categorizes risk severity (`LOW`, `MEDIUM`, `HIGH`), and structures opposing risk factors against mitigation variables.
- **Adversarial Bull vs. Bear Debate Synthesis**: The `DebateAgent` pits an unconstrained bull thesis against an adversarial bear case, surfacing the primary structural contradictions, margin pressures, and valuation tensions between market participants.
- **Institutional Investment Verdict**: The `ThesisAgent` synthesizes all upstream telemetry into an actionable investment memo with a definitive stance (`BUY`, `HOLD`, `SELL`, `WATCH`), numerical confidence rating (`0-10`), macroeconomic rationale, and mandatory compliance disclaimers.
- **Intelligent Semantic Guardrails**: Dedicated `GuardrailAgent` screening queries into `company_analysis`, `general_finance`, or `irrelevant`. Out-of-domain requests or prompt injection vectors are terminated early with explanatory feedback.
- **Real-Time Token & Event Streaming**: Native SSE (`text/event-stream`) streaming pipeline pushing agent execution deltas directly to the web client with microsecond latency.
- **Fault-Tolerant Tri-Tier LLM Fallbacks**: Resilience architecture chaining Google Gemini 3.7 Flash $\rightarrow$ Mistral Large $\rightarrow$ Groq LPU (GPT-OSS-20B), eliminating downtime caused by provider outages or rate limits.
- **Full-Stack Observability with LangSmith**: End-to-end `@traceable` instrumentation tracking agent run latencies, token consumption, tool input/output observations, and state checkpoints.

---

<a id="-demo"></a>
## 🎬 Demo

### Multi-Agent State Machine Topology

RizqAI's compiled execution graph maps state transitions dynamically across conditional decision boundaries:

<div align="center">
  <img src="assets/image.png" alt="RizqAI LangGraph Architecture" width="850">
</div>

### Execution Lifecycle Example

When prompting:
> *"Should I invest in NVIDIA for a 3-year horizon given current AI infrastructure spending?"*

1. **Guardrail Agent** evaluates intent $\rightarrow$ classified as `company_analysis`.
2. **Planner Agent** parses context $\rightarrow$ identifies ticker `NVDA`, schedules `[research_agent, risk_agent, debate_agent, thesis_agent]`.
3. **Research Agent** executes tool calls:
   - `get_stock_price(symbol="NVDA")` $\rightarrow$ retrieves near-real-time price, market cap, 52w range.
   - `get_company_info(symbol="NVDA")` $\rightarrow$ extracts P/E ratio, Forward P/E, sector, beta, margins.
   - `get_company_news(company="NVIDIA")` $\rightarrow$ gathers latest headlines regarding hyperscaler capex and export controls.
4. **Risk Agent** analyzes valuation multiples against macroeconomic risks $\rightarrow$ returns a Risk Score of `7/10 (HIGH)` highlighting customer concentration and chip cycle cyclicality.
5. **Debate Agent** constructs adversarial cases:
   - **Bull**: Unmatched CUDA moat, data center hyperscaler capex growth, sovereign AI tailwinds.
   - **Bear**: Margin compression from custom silicon (ASICs), cyclical slowdown, geopolitical export curbs.
   - **Clash**: Sustainability of 75%+ gross margins vs. client capex ROI constraints.
6. **Thesis Agent** outputs verdict:
   - **Recommendation**: `BUY` (Confidence: `8/10`).
   - **Thesis**: Near-term data center revenue lock-in offsets valuation multiples, recommended with phased accumulation.

---

<a id="-prerequisites"></a>
## 📋 Prerequisites

Ensure the following runtimes and toolchains are installed on your host system:

- **Python**: Version `3.12+` or `3.14` (with `pip` and virtual environment support).
- **Node.js**: Version `20.x` or `22.x LTS` (with `npm` package manager).
- **Docker & Docker Compose** (Optional, for containerized deployments).
- **API Credentials**:
  - [Google AI Studio API Key](https://aistudio.google.com/) (`GOOGLE_API_KEY`) for Gemini 3.7 Flash.
  - [Mistral AI API Key](https://console.mistral.ai/) (`MISTRAL_API_KEY`) for Mistral Large.
  - [Groq Cloud API Key](https://console.groq.com/) (`GROQ_API_KEY`) for LPU-accelerated inference.
  - [NewsAPI Developer Key](https://newsapi.org/) (`NEWS_API_KEY`) for real-time news retrieval.
  - [LangSmith API Key](https://smith.langchain.com/) (`LANGCHAIN_API_KEY`) for telemetry and trace logging.

---

<a id="️-installation"></a>
<a id="-installation"></a>
## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/gaoharimran29-glitch/RizqAI.git
cd RizqAI
```

### 2. Configure Environment Variables

Create a root `.env` file by copying the provided example template:

```bash
cp .env.example .env
```

Populate the `.env` file with your credentials:

```ini
# LLM Providers
GOOGLE_API_KEY=your_gemini_api_key_here
MISTRAL_API_KEY=your_mistral_api_key_here
GROQ_API_KEY=your_groq_api_key_here

# External Tools
NEWS_API_KEY=your_newsapi_key_here

# Observability & Tracing (LangSmith)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT='https://api.smith.langchain.com'
LANGCHAIN_API_KEY=your_langsmith_api_key_here
LANGCHAIN_PROJECT=RizqAI

# CORS Configuration
FRONTEND_ORIGIN=http://localhost:3000
```

---

### Option A: Running with Docker Compose (Recommended)

Run both the FastAPI backend and Next.js frontend in isolated multi-stage containers with built-in health checking:

```bash
docker compose up --build
```

The services will initialize at:
- **Frontend**: `http://localhost:3000`
- **Backend API**: `http://localhost:8000`
- **Backend Healthcheck**: `http://localhost:8000/conversations/health`

---

### Option B: Manual Local Development Setup

#### 1. Backend Service Setup

```bash
# Navigate to the backend directory
cd backend

# Create and activate a Python virtual environment
# On Linux / macOS:
python3 -m venv venv
source venv/bin/activate

# On Windows (PowerShell):
python -m venv venv
.\venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Start the FastAPI ASGI server with auto-reload
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The backend automatically creates the SQLite databases (`rizqai.db` and `rizqai_checkpoints.db`) upon startup.

#### 2. Frontend Service Setup

Open a separate terminal shell:

```bash
# Navigate to the frontend directory
cd frontend

# Install dependencies via npm
npm install

# Launch the Next.js development server
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

---

<a id="-usage"></a>
## 💻 Usage

### Web Interface

1. Open `http://localhost:3000`.
2. Inspect the **Desk Status** indicator in the sidebar (`SYSTEM OPEN` confirms backend health).
3. Type an equity ticker, company name, or macroeconomic question in the query terminal.
4. Watch the live **Timeline Stepper** cycle through:
   $$\text{Screen} \longrightarrow \text{Plan} \longrightarrow \text{Research} \longrightarrow \text{Risk} \longrightarrow \text{Debate} \longrightarrow \text{Verdict}$$
5. Expand **"Show the flow"** to inspect raw, timestamped SSE node events.
6. Revisit historical analyses at any time from the left sidebar thread drawer.

### REST & Streaming API Endpoints

The backend exposes endpoints under the `/conversations` prefix:

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/conversations/health` | Healthcheck verification endpoint returning `{"status": "ok"}`. |
| `GET` | `/conversations` | Fetches all persisted conversations sorted by `updated_at DESC`. |
| `GET` | `/conversations/{id}/messages` | Fetches complete message history and serialized states for thread `{id}`. |
| `POST` | `/conversations/messages/stream` | Dispatches query to LangGraph and streams execution updates via SSE. |

#### Streaming Query with cURL

```bash
curl -N -X POST http://localhost:8000/conversations/messages/stream \
  -H "Content-Type: application/json" \
  -d '{"query": "Evaluate Microsoft MSFT cloud growth and risk profile", "conversation_id": null}'
```

### Example Prompts

- **Single-Stock Deep Dive**:
  ```text
  "Provide a complete investment analysis of TSLA including recent robotaxi developments."
  ```
- **Fundamental & Valuation Screen**:
  ```text
  "Is Apple AAPL overvalued at current multiples? Check P/E, EPS, and recent news."
  ```
- **General Finance & Methodology**:
  ```text
  "What is the difference between trailing P/E and forward P/E, and how does beta impact volatility?"
  ```

---

<a id="-llm-client-behavior--security-considerations"></a>
## 🛡️ LLM Client Behavior & Security Considerations

### 1. Tri-Tier Model Fallback & High-Availability Architecture

Production agentic systems cannot afford single-point-of-failure vulnerabilities when downstream providers experience rate-limiting (`HTTP 429`), server degradation (`HTTP 500/503`), or network latency spikes.

RizqAI implements an automatic cascading fallback hierarchy using LangChain's `.with_fallbacks()` paradigm:

```python
primary_llm = ChatGoogleGenerativeAI(
    model="gemini-3.7-flash",
    temperature=0.2,
    api_key=GOOGLE_API_KEY,
    timeout=30,
)

fallback_llm_1 = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0.2,
    timeout=30,
    api_key=MISTRAL_API_KEY,
)

fallback_llm_2 = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.2,
    timeout=30,
    api_key=GROQ_API_KEY,
)

# Unified fault-tolerant LLM pipeline
llm = primary_llm.with_fallbacks([fallback_llm_1, fallback_llm_2])
```

- **Primary**: Google Gemini 3.7 Flash handles complex long-context reasoning with near-zero latency.
- **Secondary**: Mistral Large acts as the first resilience layer if Gemini hits quota limits.
- **Tertiary**: Groq Cloud running open-weights models (`openai/gpt-oss-20b`) on LPU hardware provides sub-second emergency failover.
- **Guaranteed Timeouts**: Every model invocation strictly enforces an explicit 30-second timeout to prevent blocked graph execution.

### 2. Dedicated Low-Latency Guardrail Screening

To preserve primary model quotas and ensure instantaneous boundary screening, the `GuardrailAgent` is isolated onto Groq LPUs (`guardrail_llm`). It parses queries before any tools or plans are initialized, protecting the system against malicious prompt injections, non-financial prompt drift, and resource exhaustion.

### 3. Reasoning Block Deconstruction (`extract_output_text`)

Next-generation reasoning models (such as Gemini 3.x) return complex conversational payloads containing distinct metadata and reasoning tokens. Within the `ResearchAgent`'s ReAct loop, raw block structures can corrupt downstream Pydantic validation:

```python
def extract_output_text(output) -> str:
    """Extracts sanitized visible text from reasoning model content blocks,
    filtering out internal signature/thought metadata blocks."""
    if isinstance(output, str):
        return output
    if isinstance(output, list):
        parts = [
            block.get("text", "") for block in output
            if isinstance(block, dict) and block.get("type") == "text"
        ]
        return "".join(parts)
    return str(output)
```

### 4. Deterministic Schema Enforcement

Freeform generation is strictly disabled across operational nodes. Every agent enforces Pydantic v2 schemas using `.with_structured_output(...)`:
- `GuardrailDecision`
- `PlannerState`
- `ResearchData`
- `RiskState`
- `DebateAgent`
- `ThesisAgent`
- `GeneralFinanceAnswer`

This guarantees that data transmitted over the wire matches the TypeScript interface definitions in `frontend/lib/types.ts` field-for-field.

### 5. Financial Advisory Disclaimer & Regulatory Compliance

RizqAI is an automated research assistant for informational and educational purposes only. Every thesis generation automatically appends an SEC/FINRA-compliant regulatory notice clarifying that outputs do not constitute formal investment advice or individualized fiduciary recommendations.

---

<a id="-known-limitations"></a>
## ⚠️ Known Limitations

- **Free-Tier NewsAPI Rate Limits**: The developer tier of NewsAPI limits requests to 100 queries/day and restricts lookback windows to articles published within the last 30 days.
- **Yahoo Finance Scraper Throttling**: The `yfinance` library relies on Yahoo Finance's public API and scraping endpoints. High-frequency automated requests from a single IP address may encounter transient HTTP 429 throttling.
- **Market Quote Delays**: Depending on global exchange licensing, quote snapshots provided by Yahoo Finance's `fast_info` may reflect standard 15-minute delays during open market hours.
- **SQLite Concurrency in Production**: The default checkpointing layer uses `aiosqlite` and local file locks (`rizqai.db` / `rizqai_checkpoints.db`). For distributed enterprise clusters with concurrent multi-tenant writes, replace `AsyncSqliteSaver` with `PostgresSaver`.

---

<a id="️-project-structure"></a>
<a id="-project-structure"></a>
## 🏗️ Project Structure

```
RizqAI/
├── .env.example                 # Environment configuration template
├── docker-compose.yml           # Multi-container orchestration (FastAPI + Next.js)
├── LICENSE                      # MIT Open Source License
├── README.md                    # Project documentation
├── assets/
│   ├── banner.svg               # RizqAI vector wordmark banner
│   └── image.png                # Compiled LangGraph architecture state diagram
│
├── backend/
│   ├── main.py                  # FastAPI entry point & ASGI lifespan management
│   ├── config.py                # LLM client initialization & tri-tier fallbacks
│   ├── requirements.txt         # Python backend dependencies
│   ├── dockerfile               # Python 3.12 multi-stage container build
│   │
│   ├── agents/                  # Autonomous LangGraph execution nodes
│   │   ├── guardrail_agent.py   # Intent classification & perimeter security
│   │   ├── planner_agent.py     # Ticker resolution & task graph planner
│   │   ├── research_agent.py    # ReAct tool-calling market analyst
│   │   ├── risk_agent.py        # Volatility & quantitative risk scoring
│   │   ├── debate_agent.py      # Polarized Bull vs. Bear debate synthesis
│   │   ├── thesis_agent.py      # Final actionable recommendation & memo
│   │   ├── general_finance_agent.py # Conceptual personal finance advisor
│   │   └── node_routing.py      # Dynamic conditional routing predicates
│   │
│   ├── graph/                   # LangGraph orchestration engine
│   │   ├── graph.py             # StateGraph definition & edge topology
│   │   └── state.py             # Centralized GraphState schema
│   │
│   ├── tools/                   # Agent tool wrappers & utility helpers
│   │   ├── stock_price_tool.py  # Near-real-time ticker price snapshot
│   │   ├── company_info_tool.py # Company fundamentals, valuation & ratios
│   │   ├── company_news_tool.py # Recent headlines from NewsAPI
│   │   └── helpers.py           # Fuzzy ticker resolution via Yahoo Search
│   │
│   ├── schemas/                 # Pydantic v2 structured output contracts
│   │   ├── conversation.py      # REST & thread validation schemas
│   │   ├── guardrail_state.py   # Guardrail taxonomy classifications
│   │   ├── planner_state.py     # Agent task sequence definitions
│   │   ├── research_state.py    # Tool observation & research payload
│   │   ├── risk_state.py        # Risk score & factor models
│   │   ├── debate_state.py      # Adversarial case models
│   │   ├── thesis_state.py      # Recommendation & verdict contracts
│   │   └── general_finance_state.py # Educational finance schemas
│   │
│   ├── prompts/                 # Specialized system prompts per agent
│   │   ├── guardrail_prompt.py
│   │   ├── planner_prompt.py
│   │   ├── research_prompt.py
│   │   ├── risk_prompt.py
│   │   ├── debate_prompt.py
│   │   ├── thesis_prompt.py
│   │   └── general_finance_prompt.py
│   │
│   ├── database/                # Persistence & ORM models
│   │   ├── db.py                # SQLAlchemy engine & session factory
│   │   └── models.py            # Conversation & Message relational entities
│   │
│   └── api/                     # Web layer & routing
│       ├── routes.py            # REST endpoints & SSE streaming handler
│       └── helpers.py           # Node serialization & stream chunk formatting
│
└── frontend/                    # Next.js 16 App Router interface
    ├── package.json             # Frontend dependencies (React 19, Tailwind v4)
    ├── tsconfig.json            # TypeScript configuration
    ├── dockerfile               # Node 22 Alpine standalone runner
    │
    ├── app/
    │   ├── layout.tsx           # Global HTML shell & typography
    │   ├── page.tsx             # Interactive research terminal & state orchestrator
    │   └── globals.css          # Tailwind CSS v4 styling & color tokens
    │
    ├── components/              # Modular UI components
    │   ├── ChatTurn.tsx         # Analysis turn card & phase distributor
    │   ├── Timeline.tsx         # Real-time multi-agent progression stepper
    │   ├── StreamLog.tsx        # Live SSE telemetry & node event logger
    │   ├── Sidebar.tsx          # Thread drawer & system status monitor
    │   ├── QueryInput.tsx       # Search query terminal with examples
    │   ├── Markdown.tsx         # Markdown syntax & LaTeX renderer
    │   └── sections/            # Specialized agent visual cards
    │       ├── PlanSection.tsx
    │       ├── ResearchSection.tsx
    │       ├── RiskSection.tsx
    │       ├── DebateSection.tsx
    │       ├── ThesisSection.tsx
    │       ├── GeneralFinanceSection.tsx
    │       ├── ScopeNoteSection.tsx
    │       └── EmptyNoteSection.tsx
    │
    └── lib/                     # Client libraries & typing
        ├── api.ts               # ReadableStream SSE reader & REST fetchers
        ├── types.ts             # TypeScript mirrors of backend Pydantic models
        ├── format.ts            # Currency & compact number formatters
        ├── parseHistory.ts      # Relational message rehydration parser
        └── streamLog.ts         # Event stream log summarization
```

---

<a id="-license"></a>
## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

<a id="-author"></a>
## 👤 Authors & Contributors

This project was conceptualized, architected, and built in close technical collaboration:

### 🌟 Core Developers

#### **Gaohar Imran**
- **GitHub**: [@gaoharimran29-glitch](https://github.com/gaoharimran29-glitch)
- **Email**: [gaoharimran29@gmail.com](mailto:gaoharimran29@gmail.com)

#### **Mohd Ali**
- **GitHub**: [@BeingMohdAli](https://github.com/BeingMohdAli)
- **Email**: [mohdalisaad868@gmail.com](mailto:mohdalisaad868@gmail.com)

### 🤝 Core Contributions & Collaborative Engineering

Both authors actively collaborated across the entire stack, sharing equal ownership of the product's design and execution:

- **Joint Ideation & Architectural Design**: Collaboratively brainstormed the core concept of RizqAI, designed the LangGraph multi-agent DAG topology, defined state transition boundaries, and formulated prompt engineering strategies.
- **Full-Stack Coordination (Backend & Frontend)**: Both developers actively contributed to and reviewed both sides of the application:
  - **Backend Engineering**: Coordinated on FastAPI API development, LangGraph state orchestration (`GraphState`), autonomous agent nodes (`Guardrail`, `Planner`, `Research`, `Risk`, `Debate`, `Thesis`, and `General Finance`), tool integrations (Yahoo Finance, NewsAPI), SQLite checkpointing, and tri-tier LLM fallback resilience.
  - **Frontend Engineering**: Coordinated on building the responsive Next.js 16 terminal interface, real-time Server-Sent Events (SSE) consumption, interactive multi-agent timeline tracking (`Timeline.tsx`), live execution flow telemetry (`StreamLog.tsx`), and styling with Tailwind CSS v4.
- **Continuous Peer Review & Iteration**: Actively suggested structural changes, optimized agent memory and debate pipelines, conducted mutual code reviews, and resolved cross-cutting state and UI integration challenges.



---

<div align="center">
  <sub>Engineered with precision for autonomous financial intelligence. Built with LangGraph, FastAPI, and Next.js.</sub>
</div>
