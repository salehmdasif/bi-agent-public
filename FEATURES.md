# Features: BI Agent Platform

## Feature List

---

### 1. Conversational AI Chat

**What it does:** Users ask business questions in natural language and get data-backed answers. The agent pulls live data from connected sources, runs analysis, and explains the result in plain language. Charts render inline in the chat window.

**Who uses it:** All users.

**Workflow:**
1. User types a question in the chat window
2. Agent selects the appropriate data source tools
3. Agent fetches live data and processes it
4. Agent returns a written answer with numbers and optional chart
5. User can follow up with additional questions in the same conversation

**Business value:** Reduces the time needed to get answers from multiple platforms. Non-technical users can get the same insight a data analyst would produce, without any SQL or API knowledge.

**Edge cases handled:**
- If the requested data source is not connected, the agent says so and suggests the admin connects it
- If the AI is not configured (no API key), the chat returns a clear error message
- If a question exceeds the tool call iteration limit, the agent summarizes what it found so far
- Demo mode returns realistic sample data when no live credentials are present

---

### 2. Human-in-the-Loop (HITL) Approvals

**What it does:** Prevents the AI from taking irreversible actions without human confirmation. When the agent wants to pause an ad, update a budget, or write to a Google Sheet, it creates an approval request. The user sees a card in the chat with the proposed action and Approve/Reject buttons.

**Who uses it:** All users who have write-action tools enabled.

**Workflow:**
1. User asks agent to take an action ("Pause the low-ROAS ad set")
2. Agent calls the relevant tool
3. Tool returns a HITL signal instead of executing
4. A PendingAction record is created in the database
5. Frontend renders an approval card tied to that record
6. User clicks Approve or Reject
7. If approved: the action executes against the external API
8. If rejected: the pending action is marked rejected, nothing changes

**Business value:** Gives businesses the benefit of AI-driven suggestions without the risk of automated changes to live ad accounts or databases.

**Edge cases handled:**
- Pending actions expire after a configurable timeout
- Expired actions cannot be approved
- Approval endpoint verifies the action belongs to the requesting user

---

### 3. KPI Dashboard

**What it does:** Displays a visual overview of key business metrics from all connected data sources. Metric cards show current values and period-over-period changes. Charts show trends.

**Who uses it:** All users.

**Workflow:**
1. Admin connects at least one data source
2. Dashboard automatically fetches KPIs from connected sources
3. User selects a date range
4. Metric cards update to show current vs. previous period
5. User clicks a metric card to see a detailed chart

**Business value:** Replaces manual reporting. One screen shows the full health of the business.

**Edge cases handled:**
- Disconnected sources show a placeholder card with a "connect" prompt
- API rate limit errors return cached values from the last successful fetch
- Zero-value metrics are handled without division-by-zero errors in percentage calculations

---

### 4. Automated Alerts

**What it does:** Monitors configured metrics and sends notifications when values go outside set thresholds. Alerts can be sent by email and Telegram.

**Who uses it:** Admin and Manager roles.

**Workflow:**
1. Admin creates an alert: select a metric, set a threshold, pick notification channels
2. Celery Beat fires the monitoring task on schedule (default: every 15 minutes)
3. Task fetches the current metric value from the connected source
4. If the threshold condition is true, an alert record is created
5. Notification is sent to the configured email and/or Telegram chat
6. Admin can view triggered alert history in the Alerts panel

**Business value:** Teams find out about problems immediately, not on the next manual check.

**Edge cases handled:**
- Alerts are not sent again for the same condition until it resolves and re-triggers (cooldown period)
- If the data source is unreachable, the alert job records the failure without spamming notifications
- Alerts can be paused without deleting them

---

### 5. Scheduled Reports

**What it does:** Generates a weekly performance report with KPI tables and charts and delivers it by email as a PDF.

**Who uses it:** Admin configures. All recipients receive it.

**Workflow:**
1. Admin sets a report schedule and recipient email list
2. Celery Beat triggers the report task at the scheduled time
3. Backend fetches KPI data from all connected sources
4. Plotly generates chart images
5. Weasyprint renders an HTML template with the data and charts to PDF
6. PDF is sent as an email attachment

**Business value:** Keeps stakeholders informed without anyone spending time preparing reports.

**Edge cases handled:**
- If a data source is offline during report generation, the section for that source is skipped with a note
- Report PDF is saved to disk and accessible for download from the Reports panel for 30 days
- Failed deliveries are retried via Celery retry mechanism

---

### 6. File Upload and Semantic Search (RAG)

**What it does:** Users upload business documents (PDFs, spreadsheets, reports, Word files) and ask questions about their content in chat. The agent retrieves the most relevant sections and uses them to answer.

**Who uses it:** All users.

**Supported file types:** PDF, CSV, XLSX, DOCX, TXT

**Workflow:**
1. User uploads a file from the Files panel or directly in chat
2. System extracts and chunks the text
3. Chunks are embedded and stored in ChromaDB, scoped to the user
4. In chat, user asks a question about the document
5. The `query_uploaded_files` tool performs a semantic search
6. Agent uses the returned chunks to write an answer

**Business value:** Static reports and PDFs become queryable. Useful for analyzing downloaded ad reports, financial summaries, or any document that is not in a live data source.

**Edge cases handled:**
- Files over the size limit are rejected with a clear error message
- Unsupported file types return an error at upload time
- If no relevant content is found, the agent says so rather than hallucinating an answer
- Each user's file data is isolated from other users

---

### 7. Data Source Connectors

**What it does:** Connects the platform to external APIs and databases. Admin enters credentials in the UI. The system encrypts and stores them. All agent tools and KPI widgets then use these credentials transparently.

**Supported sources:**
- Meta Ads Graph API (campaigns, ad sets, spend, ROAS, CTR)
- Shopify Admin API (orders, revenue, AOV, product stock)
- WooCommerce REST API (orders, revenue)
- PostgreSQL (direct connection, natural language queries)
- MySQL (direct connection, natural language queries)
- Google Sheets (read and write, via service account)
- Google Ads API (in progress)

**Workflow:**
1. Admin opens the Admin panel, selects a module
2. Admin enters the required credentials (API keys, database host/password, etc.)
3. System runs a test connection and shows success or error
4. Once connected, the module is available to all permitted users
5. Credentials can be updated or disconnected at any time

**Business value:** Single setup per data source. After connection, all users benefit without needing their own API access.

**Edge cases handled:**
- Credentials are encrypted at rest. They are never returned in plaintext via the API.
- Test connection errors show the specific failure reason (wrong key, network unreachable, etc.)
- Disconnecting a source disables all agent tools for that source immediately

---

### 8. Telegram Bot

**What it does:** Connects the platform to a Telegram bot for chat interaction and alert delivery.

**Capabilities:**
- Receive threshold alerts as Telegram messages
- Receive weekly report summaries in Telegram
- Chat with the AI agent by messaging the bot

**Workflow:**
1. Admin creates a Telegram bot via BotFather and copies the token into the environment config
2. On startup, the backend registers its webhook URL with Telegram
3. Messages to the bot are routed to the agent brain
4. Alerts and reports are delivered to the configured Telegram chat ID

**Business value:** Teams that live in Telegram can interact with the platform without switching to the web app.

**Edge cases handled:**
- Webhook registration failures are caught on startup without crashing the app
- Telegram API errors during alert delivery are logged and retried

---

### 9. User and Team Management

**What it does:** Admins can invite team members, assign roles, and control which data sources each person can query.

**Workflow:**
1. Admin sends an invitation email to a new team member
2. The invitation contains a time-limited signup link
3. Invitee sets a password and gets access
4. Admin assigns module permissions per user
5. User can only access tools and data sources they have been granted permission for
6. Admin can deactivate a user without deleting their data

**Business value:** Keeps data access controlled. The marketing manager only sees ads data. The finance manager only sees database access. No one sees everything unless the admin grants it.

**Edge cases handled:**
- Expired invitations cannot be accepted
- Deactivated users lose API access immediately on next token refresh
- Password reset is handled via time-limited email tokens

---

### 10. License and Deployment Control

**What it does:** Enforces that only authorized deployments of the platform can operate. The license system controls which modules are active and how many users are allowed.

**Business value:** Enables controlled distribution of the platform as a product. Clients cannot share a license across multiple deployments.

**Technical summary:** The license system is proprietary and not included in this public version. It operates at the middleware level.

---

### 11. Activity Log

**What it does:** Records a searchable audit trail of all significant actions: logins, credential updates, report deliveries, user invitations, and AI interactions.

**Who uses it:** Admin.

**Business value:** Compliance and debugging. Admins can see exactly what happened and when.

---

### 12. API Token Management

**What it does:** Users can generate long-lived API tokens from their profile for programmatic access to the public REST API.

**Workflow:**
1. User opens Profile, creates a named API token
2. Token is shown once at creation time
3. User includes the token in `Authorization: Bearer <token>` headers for API calls
4. Tokens expire after 90 days by default
5. User can revoke tokens at any time

**Business value:** Enables integrations with other tools (e.g. dashboards, custom scripts) without sharing login credentials.
