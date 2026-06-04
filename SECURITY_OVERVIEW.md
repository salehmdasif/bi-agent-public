# Security Overview: BI Agent Platform

## Authentication

The platform uses JWT-based authentication with two token types:

**Session tokens (web app users):**
- Access token: short-lived (15 minutes by default), HS256 signed, contains user ID and role
- Refresh token: longer-lived (7 days by default), stored and rotated on each use
- Tokens are sent in the `Authorization: Bearer` header

**API tokens (programmatic access):**
- Long-lived tokens (90 days by default) generated from the user profile
- Stored as a one-way hash in the database (the plaintext token is shown only once at creation)
- Support the same `Authorization: Bearer` header pattern
- Can be revoked instantly

Both token types go through the same authentication middleware. The middleware determines the token type by structure and validates accordingly.

---

## Authorization Model

Role-based access control (RBAC) operates at two levels:

**Role level:** The user's role (super_admin, admin, manager, viewer) gates entire API route groups. Admin-only endpoints return 403 for non-admins regardless of other state.

**Module permission level:** Data source access is controlled per-user per-module. Even users with the same role do not share data source access by default. An admin explicitly grants permission for each module to each user. This is checked at agent tool assembly time before every chat request.

---

## Credential Storage

All third-party API credentials (Meta Ads access tokens, Shopify API keys, database passwords, Google service account JSON) are encrypted before storage using AES-256 (Fernet symmetric encryption). The encryption key is a deployment-specific environment variable, not stored in the database. Credentials are decrypted only at the moment of use inside the backend process and never returned via the API in plaintext.

---

## License System

The license enforcement system is proprietary and not described in detail in this public version. At a high level:

- Each deployment holds a license JWT
- A middleware layer validates the license on every API request
- The validation result is cached in Redis to avoid a database round-trip per request
- If the license is not valid, all non-essential endpoints return 403
- Health check and a small set of auth endpoints remain accessible for troubleshooting

---

## SQL Injection Prevention

When the agent generates SQL from natural language, the generated query is passed through a static analysis validator (using sqlglot) before execution. The validator:

- Blocks any statement that is not a SELECT
- Blocks statements containing DDL keywords (CREATE, DROP, ALTER)
- Blocks statements containing DML keywords (INSERT, UPDATE, DELETE)
- Rejects statements with subqueries that attempt writes

A row limit is also injected into every query before execution regardless of what the LLM produced.

---

## Rate Limiting

API rate limiting is applied at the middleware level using SlowAPI (a FastAPI-compatible limiter backed by Redis). Limits are applied per IP address and per authenticated user. The auth endpoints have lower limits than general API endpoints to slow brute-force login attempts.

---

## Input Validation

All request bodies are validated through Pydantic schemas before reaching route handlers. Type coercion, required field checks, and length limits are applied at the schema layer. File uploads are validated for MIME type and size before any processing begins.

---

## Data Isolation

Each user's uploaded files and ChromaDB vectors are scoped by user ID. Cross-user file access is not possible through the API. Conversation records are scoped to the owning user.

---

## Transport Security

All production traffic is served over HTTPS via Nginx with Let's Encrypt certificates. The internal Docker network is isolated and not exposed to the public internet. Service-to-service communication inside Docker uses unencrypted private network connections, which is standard for this deployment model.

---

## Secrets Management

All secrets are stored in a `.env` file on the VPS, outside the repository. The `.env` file is never committed to version control (`.gitignore` excludes it). The repository includes only `.env.example` with placeholder values.

---

## What Is Not Included

The following are proprietary and not present in this public version:

- License system implementation details (validation logic, domain locking mechanism)
- Security implementation internals (hash configurations, token generation specifics)
- Encryption key derivation logic
