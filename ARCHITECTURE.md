# Architecture: BI Agent Platform

## Overview

The platform is built as a decoupled system with four main process groups: the Next.js frontend, the FastAPI backend (including the agent), Celery workers for background tasks, and external services (PostgreSQL, Redis, ChromaDB). Each group scales independently. The backend is stateless by design, which means any number of backend instances can sit behind a load balancer.

---

## Component Interaction Diagram

> View this diagram: open the `.mmd` file in [Mermaid Live Editor](https://mermaid.live)

See [docs/diagrams/architecture.mmd](docs/diagrams/architecture.mmd)

---

## Request Lifecycle

### Web Chat Request

```
User types message
    -> Browser sends POST /api/v1/chat/message
    -> Nginx proxies to FastAPI backend
    -> LicenseMiddleware checks license cache (Redis)
    -> Rate limiter checks request count (Redis)
    -> JWT auth extracts user identity
    -> Route handler calls run_agent()
    -> Agent loads AI settings from DB
    -> Agent fetches user's allowed modules from DB
    -> Agent builds tool list (only permitted tools)
    -> LangGraph starts agentic loop
        -> LLM chooses a tool
        -> Tool fetches data from external API or DB
        -> Result fed back to LLM
        -> Loop continues until final answer or HITL signal
    -> Response saved to conversation in DB
    -> JSON response returned to frontend
    -> Frontend renders message and optional chart
```

### Background Alert Check

```
Celery Beat fires monitoring task on schedule
    -> Task loads all configured alerts from DB
    -> For each alert:
        -> Fetch current metric from data source
        -> Compare against threshold
        -> If breached: create alert record in DB
        -> Send email via SMTP
        -> Send Telegram message if bot is configured
```

---

## Service Dependency Map

```
FastAPI Backend
    required: PostgreSQL, Redis
    optional: ChromaDB (if file upload used), Telegram Bot API

Celery Worker
    required: PostgreSQL, Redis
    optional: Telegram Bot API, SMTP server

Celery Beat
    required: Redis (for lock and schedule)

Next.js Frontend
    required: FastAPI Backend
```

---

## Module Architecture

### Agent Module (`app/agent/`)

The agent module is the most critical part of the system. It has five components:

| File | Role |
| ---- | ---- |
| `brain.py` | Main agent loop. Loads settings, builds tools, runs LangGraph loop, saves results. |
| `tools.py` | All LangChain StructuredTool implementations. One function per tool. Tools support demo mode. |
| `hitl.py` | Creates and resolves PendingAction records. |
| `memory.py` | Loads and saves conversation history. Applies sliding window. |
| `rag.py` | ChromaDB client. Embeds and queries uploaded file content. |
| `sql_validator.py` | Static SQL analysis. Blocks non-SELECT statements. Injects row limits. |
| `demo.py` | Realistic fake data for demo mode. Used by all tools when `is_demo=True`. |

### API Module (`app/api/v1/`)

Each feature area has its own router file. The main `router.py` aggregates them with path prefixes. All routes use dependency injection for database sessions and current user identity.

### Core Module (`app/core/`)

| File | Role |
| ---- | ---- |
| `config.py` | Pydantic settings loaded from environment variables. |
| `database.py` | Async SQLAlchemy engine and session factory. |
| `security.py` | Password hashing, JWT creation and validation, AES-256 encryption utilities. |
| `license.py` | License JWT verification and cache management. |
| `license_middleware.py` | ASGI middleware that blocks requests if license is not valid. |
| `rate_limit.py` | SlowAPI limiter configuration. |
| `module_registry.py` | Seeds default modules to DB. Caches enabled module list in Redis. |
| `notifier.py` | Alert dispatch: email and Telegram. |
| `email.py` | Async SMTP client. Sends HTML emails from Jinja2 templates. |
| `activity.py` | Writes to the activity log. |
| `deps.py` | FastAPI dependency functions: get_db, get_current_user, require_admin. |

### Modules (`app/modules/`)

Each integration is an independent package. Connectors load encrypted credentials from the database, connect to the external API, and return normalized data. KPI modules extract standardized metric shapes.

| Module | Integration |
| ------ | ----------- |
| `meta_ads/` | Meta Ads Graph API v19.0 |
| `shopify/` | Shopify Admin REST API 2024-01 |
| `woocommerce/` | WooCommerce REST API v3 |
| `postgresql/` | asyncpg direct connection |
| `mysql/` | aiomysql direct connection |
| `google_sheets/` | Google Sheets API v4 |
| `google_ads/` | Google Ads API (in progress) |
| `telegram/` | Telegram Bot API (webhook mode) |
| `n8n/` | n8n webhook trigger |

### Tasks (`app/tasks/`)

| Task | Schedule | Purpose |
| ---- | -------- | ------- |
| `monitoring.py` | Every 15 minutes | Evaluate alert thresholds and dispatch notifications |
| `insights.py` | Daily | Generate AI-written summaries of key metric trends |
| `reports.py` | Weekly | Build and email PDF performance reports |
| `token_check.py` | Daily | Expire and clean up old API tokens |

---

## Data Flow: Natural Language to SQL

```
User question
    -> Agent passes question to LLM with a SQL generation prompt
    -> LLM returns a SQL string
    -> sql_validator.safe_execute_check() parses the SQL with sqlglot
    -> If any non-SELECT statement found: return error, do not execute
    -> sql_validator.inject_row_limit() rewrites the query to add LIMIT 100
    -> Query executes against the user's connected database
    -> Results returned to agent as JSON
    -> Agent formats and explains the result in natural language
```

---

## Data Flow: File RAG

```
File upload
    -> Backend validates file type and size
    -> File saved to local volume
    -> UploadedFile record created in DB
    -> Background task extracts text by file type
    -> Text split into overlapping chunks
    -> Chunks embedded via LLM embedding model
    -> Vectors stored in ChromaDB keyed by user_id + file_id

Chat query referencing a file
    -> query_uploaded_files tool called with the user's question
    -> ChromaDB vector similarity search scoped to user_id
    -> Top N chunks returned as context
    -> Agent synthesizes answer from chunks
```

---

## Middleware Stack (LIFO Execution Order)

```
Request comes in
    -> CORSMiddleware        (allows/blocks cross-origin)
    -> LicenseMiddleware     (blocks if license invalid, allows health + auth)
    -> SlowAPIMiddleware     (rate limiting per IP and user)
    -> Route handler         (business logic)
```

Because FastAPI applies middleware in last-in-first-out order, CORS is evaluated first in the outbound direction but last-registered. LicenseMiddleware sits between rate limiting and application logic, so rate limit rejections skip the license check.

---

## Key Interfaces

### Tool Interface (all agent tools follow this shape)

```python
StructuredTool(
    name: str,                   # tool identifier used by LLM
    description: str,            # what the tool does (shown to LLM)
    args_schema: BaseModel,      # Pydantic input model
    coroutine: async function,   # the actual implementation
)
```

### KPI Connector Interface (all module KPI files follow this shape)

```python
async def get_kpi_summary(
    credentials: dict,           # decrypted credential dict
    date_range: str,             # standard date preset
) -> dict:                       # normalized KPI response
    ...
```

### HITL Signal Shape (returned by destructive tools)

```json
{
    "hitl_required": true,
    "action_type": "pause_adset",
    "action_data": { "adset_id": "123" },
    "suggestion": "Pause Ad Set 123. Approve?"
}
```
