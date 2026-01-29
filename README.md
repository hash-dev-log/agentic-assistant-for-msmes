# agentic-assistant-for-msmes
This project demonstrates an agentic AI automation system built using LangGraph, Retrieval-Augmented Generation (RAG), and LangSmith to automate core business operations such as reminders, reporting, and data-driven insights that mirrors real consulting use cases.

# AI Business Operations Assistant

## Problem Statement

Small and medium consulting firms face operational inefficiencies in:
- Manual follow-up tracking leading to missed deadlines
- Time-consuming weekly report compilation
- Inability to extract actionable insights from internal documentation

This system automates three critical workflows:
1. **Task & Follow-up Reminders**: Identifies overdue/upcoming tasks using business rules
2. **Weekly Operational Reporting**: Aggregates KPIs and metrics automatically
3. **Business Insights**: Provides data-grounded answers using RAG over internal SOPs

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    LANGGRAPH ORCHESTRATOR                    │
│                                                               │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐ │
│  │  LOAD    │──▶│ VALIDATE │──▶│ REMINDER │──▶│  REPORT  │ │
│  │  DATA    │   │  DATA    │   │  AGENT   │   │  AGENT   │ │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘ │
│                                       │                       │
│                                       ▼                       │
│                                 ┌──────────┐                 │
│                                 │ INSIGHT  │                 │
│                                 │  AGENT   │                 │
│                                 └──────────┘                 │
│                                       │                       │
│                                       ▼                       │
│                                  ┌────────┐                  │
│                                  │  RAG   │                  │
│                                  │ ENGINE │                  │
│                                  └────────┘                  │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
                    ┌────────────┐
                    │  LANGSMITH │
                    │  TRACING   │
                    └────────────┘
```

---

## Key Design Decisions

### 1. **Determinism Over Creativity**
- Business rules (date checks, status filters) are deterministic
- LLMs only used for natural language generation, not decision-making
- All logic is auditable and explainable

### 2. **Clear Agent Boundaries**
- **Reminder Agent**: Pure business logic + message formatting
- **Report Agent**: Aggregation + KPI calculation
- **Insight Agent**: RAG-based question answering

### 3. **Data Quality First**
- Explicit validation layer before processing
- Graceful degradation for missing/malformed data
- Error states captured in outputs

### 4. **Production-Ready Outputs**
- Structured JSON compatible with Excel, Power BI
- Timestamps for audit trails
- Metadata for debugging

---

## Technology Stack

| Component | Technology | Rationale |
|-----------|-----------|-----------|
| Orchestration | LangGraph | Explicit state management, visual debugging |
| LLM Framework | LangChain | Industry standard, integrates with LangSmith |
| Embeddings | OpenAI `text-embedding-3-small` | Cost-effective, sufficient for small docs |
| Vector Store | FAISS | In-memory, no infrastructure needed |
| Observability | LangSmith | Native LangChain integration |

---

## Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install langchain langgraph langsmith openai faiss-cpu pandas python-dotenv

# Set environment variables
export OPENAI_API_KEY="your-key-here"
export LANGCHAIN_API_KEY="your-langsmith-key"
export LANGCHAIN_TRACING_V2="true"
export LANGCHAIN_PROJECT="ai-business-ops"
```

---

## Usage

```bash
# Run the complete workflow
python main.py

# Outputs will be generated in outputs/
# - reminders.json
# - weekly_report.json
```

---

## Assumptions

1. **Data Freshness**: CSV files are updated daily by operations team
2. **Date Format**: ISO 8601 (YYYY-MM-DD) in all date columns
3. **LLM Access**: OpenAI API key available (GPT-4 for insights, GPT-3.5 for formatting)
4. **Single-tenant**: System processes one client's data at a time

---

## Limitations

1. **No Incremental Updates**: Full reprocessing on each run
2. **In-Memory RAG**: Documents must fit in memory (suitable for <100 pages)
3. **No Authentication**: Assumes secure execution environment
4. **English Only**: NLP components not tested for multilingual content

---

## Future Improvements

### Phase 2 (Near-term)
- [ ] Email integration for automated reminder delivery
- [ ] Dashboard UI for insights exploration
- [ ] PostgreSQL backend for historical tracking

### Phase 3 (Long-term)
- [ ] Multi-tenant support with access controls
- [ ] Advanced RAG with reranking
- [ ] Integration with CRM systems (Salesforce, HubSpot)
- [ ] Predictive analytics for sales pipeline

---

## Monitoring & Debugging

### LangSmith Tracing
1. Navigate to [LangSmith Dashboard](https://smith.langchain.com)
2. Filter by project: `ai-business-ops`
3. Each agent run is tagged (`reminder_agent`, `report_agent`, `insight_agent`)

### Common Issues

| Error | Cause | Solution |
|-------|-------|----------|
| `KeyError: 'due_date'` | Missing column in CSV | Check data/tasks.csv structure |
| `401 Unauthorized` | Invalid API key | Verify OPENAI_API_KEY |
| Empty reminders.json | No overdue tasks | Expected behavior if all tasks current |

---

## File Structure

```
ai_business_ops/
│
├── data/                    # Input data
│   ├── tasks.csv
│   ├── sales.csv
│   └── docs/
│       └── sop.md
│
├── agents/                  # Business logic agents
│   ├── reminder_agent.py
│   ├── report_agent.py
│   └── insight_agent.py
│
├── workflows/               # LangGraph orchestration
│   └── business_graph.py
│
├── rag/                     # Retrieval-augmented generation
│   ├── loader.py
│   ├── retriever.py
│
├── utils/                   # Shared utilities
│   ├── data_loader.py
│   └── validators.py
│
├── outputs/                 # Generated artifacts
│   ├── reminders.json
│   └── weekly_report.json
│
├── main.py                  # Entry point
└── README.md
```

---

## Contact & Support

For implementation questions or customization requests, contact the AI Automation team.

**Version**: 1.0.0  
**Last Updated**: January 2026