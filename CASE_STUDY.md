# Case Study: BI Agent Platform

> A conversational business intelligence platform that replaced manual cross-platform reporting for marketing and e-commerce teams, cutting the time to answer a business question from 30 minutes to under 30 seconds.

---

## Client / Context

A digital marketing agency managing multiple e-commerce clients needed a smarter way to monitor performance. The team was manually checking Meta Ads, Shopify, and a PostgreSQL analytics database every morning and compiling a report by hand. This took hours each week and still left important questions unanswered until someone got around to looking.

The same problem repeated across clients. Each one had their own set of platforms, their own team members with different access needs, and their own tolerance for risk when it came to making changes to live ad campaigns.

The project was designed to solve this for any marketing or e-commerce team that manages data across multiple platforms and needs a faster, safer way to get answers and take action.

---

## The Challenge

The core problem was fragmentation. Every piece of data that mattered lived in a different place. Getting a complete picture meant logging into four different platforms, pulling numbers, and putting them together manually. By the time the report was done, the data was already hours old.

There was also a second problem: acting on the data. When a campaign was underperforming, someone had to go into Meta Ads Manager, find the right ad set, and pause it. With the AI tools available, it was tempting to automate that. But fully automated changes to live ad budgets are a business risk. One wrong move and thousands of dollars in budget could be misallocated.

### Key Pain Points

- Marketing managers spent 30 to 60 minutes each morning pulling numbers from Meta Ads, Shopify, and a database to answer basic questions
- No single view of ROAS, revenue, and order volume together
- Acting on insights required switching platforms and risking human error in the wrong ad account
- Distributing the right data to the right team members required setting up separate logins across every platform

---

## The Approach

The starting point was a clear user story: a marketing manager should be able to type "What was my ROAS last week?" and get a real answer backed by live data in under 30 seconds. Everything else was secondary to making that work reliably.

### Discovery Phase

The key constraints identified early:

- The platform would be deployed per client, not shared. Each client's data needed to be completely isolated.
- Different team members needed different access. The agency account manager should not see the database. The database analyst should not see the ad account credentials.
- Some actions (pausing ads, writing to sheets) needed a human checkpoint. Full automation was not acceptable to the clients.
- The system needed to work with whatever AI model the client was willing to pay for. Some wanted Claude. Some were already paying for OpenAI.

### Architecture Decision

The central question was: build a simple chatbot on top of an API, or build a proper agentic system?

A simple chatbot would have one LLM call per user message. Fast and simple. But it cannot handle multi-step questions ("Show me which campaigns are underperforming, then compare them to last month"). It cannot combine data from two different sources in one answer. It cannot pause and ask for approval mid-flow.

LangGraph was chosen for the agent layer. It provides a structured multi-step reasoning loop where the agent can call tools repeatedly, accumulate results, and decide when it has enough information to answer. The tradeoff is added complexity in the agent layer. That complexity pays off for a system where the primary user experience is "ask a question and get a real answer."

The Human-in-the-Loop pattern was designed as a first-class feature from the start, not added later. Destructive tools return a signal instead of executing. The frontend handles the confirmation UI. This separation keeps the agent stateless about approvals and makes the flow testable.

### Engineering Priorities

The project optimized for three things in this order:

1. **Correctness:** Every answer the agent gives must come from real data. No hallucination about business metrics. The agent only states numbers it fetched from a live source.

2. **Safety:** No irreversible action without human approval. Generated SQL is validated before execution. Stored credentials are encrypted at rest.

3. **Deployability:** The whole system deploys with one command on a standard Linux VPS. No cloud dependencies. No Kubernetes. A client with a $20/month VPS can run this.

---

## What Was Built

A multi-tenant business intelligence platform with a conversational AI front-end and a modular data connector backend.

### Core Capabilities

- Any team member can ask a business question in plain English and get a live data answer with a chart in under 30 seconds
- The system connects to Meta Ads, Shopify, WooCommerce, PostgreSQL, MySQL, and Google Sheets through a single admin setup
- Threshold-based alerts monitor metrics automatically and push notifications to email and Telegram when something goes wrong
- Weekly performance reports are generated and emailed as PDFs without anyone compiling them manually
- Uploaded documents (PDFs, spreadsheets, reports) become searchable through the same chat interface via RAG

### Technical Highlights

- LangGraph multi-step agent loop: the agent can chain multiple tool calls in one conversation turn to answer complex questions
- HITL approval pattern: write-action tools return a structured signal that becomes a database record; the frontend renders the confirmation card without the agent needing to know about the UI
- SQL safety layer: AI-generated queries go through a static analysis pass using sqlglot before execution, with row limits injected regardless of what the LLM produced
- Per-deployment license system: each client deployment requires a signed license JWT; domain locking ensures the license cannot be transferred to another server

---

## Results and Impact

| Metric | Before | After |
| ------ | ------ | ----- |
| Time to answer "what was my ROAS last week?" | 15 to 30 minutes (manual) | Under 30 seconds |
| Platforms logged into for daily check | 3 to 4 | 1 |
| Manual steps to pause an underperforming ad set | 5 to 8 clicks across platform | 1 approval click in chat |
| Time to produce weekly report | 2 to 3 hours manual | Automated delivery |
| Onboarding a new team member to data access | Days (separate logins per platform) | Minutes (one admin panel, permission toggle) |

The platform gives marketing teams back roughly 5 to 10 hours per week that was previously spent on manual data collection and reporting. More importantly, questions that would have been answered the next morning are now answered in seconds, which changes how teams make decisions in real time.

---

## Lessons Learned

### What Went Well

- The HITL pattern solved a real tension between automation speed and business safety. Clients were much more comfortable with AI-driven suggestions when they kept final control over actions.
- LangGraph was the right choice. The structured loop made it straightforward to add new tools, handle timeouts, and interrupt the loop for HITL without special-casing the agent logic.
- The modular connector architecture paid off early. Adding WooCommerce after Meta Ads and Shopify was a matter of implementing one connector interface, not touching the agent or the chat system.

### What I Would Do Differently

- The natural language to SQL feature needed more work on schema discovery. Users sometimes asked questions the agent could not answer because it did not know the table structure. An automatic schema introspection step at connection time would have helped.
- The demo mode data was added late. Building it in from day one as a first-class test fixture would have made development faster and reduced the gap between development and production behavior.

---

## Technologies Used

Python, FastAPI, LangGraph, LangChain, Anthropic Claude, OpenAI GPT, PostgreSQL, Redis, ChromaDB, Celery, Next.js, React, TypeScript, Tailwind CSS, Plotly.js, Docker, Docker Compose, Nginx, Alembic, SQLAlchemy, asyncpg, Weasyprint

---

## Want to Discuss This Project?

I am available for a private demo and technical walkthrough.

**Contact:** salehmdasif@gmail.com
**LinkedIn:** linkedin.com/in/salehmdasif
**Portfolio:** asif.ravelweb.com
