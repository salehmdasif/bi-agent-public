# Deployment Overview: BI Agent Platform

## Deployment Model

Each client gets their own isolated deployment. The platform is packaged as a Docker Compose stack with all required services bundled. A single `docker-compose.yml` and a `.env` file are all that is needed to bring up a full production environment on any Linux VPS.

This single-tenant model was chosen because it gives each client complete data isolation, allows the operator to customize the deployment per client (different domains, license tiers, enabled modules), and keeps operational complexity low compared to a multi-tenant cloud-native architecture.

---

## Infrastructure Diagram

```
                         Internet
                             |
                     [Domain DNS / SSL]
                             |
                    [Nginx Reverse Proxy]
                             |
              +--------------+--------------+
              |                             |
   [Next.js Frontend :3000]    [FastAPI Backend :8000]
                                            |
              +--------------+--------------+----------+
              |              |              |           |
    [PostgreSQL :5432]  [Redis :6379]  [ChromaDB]  [File Volume]
                                            |
              +------------------+----------+
              |                  |
   [Celery Worker]       [Celery Beat]
```

---

## Services

| Service | Image / Build | Purpose |
| ------- | ------------ | ------- |
| `backend` | Custom Python 3.12 image | FastAPI API server |
| `frontend` | Custom Node.js 20 image | Next.js 14 server-side rendered UI |
| `postgres` | `postgres:16-alpine` | Primary relational database |
| `redis` | `redis:7-alpine` | Cache, rate limiting, Celery broker |
| `chromadb` | `chromadb/chroma:0.5.23` | Vector store for file RAG |
| `celery_worker` | Same as backend | Background task executor |
| `celery_beat` | Same as backend | Periodic task scheduler |
| `n8n` | `n8nio/n8n` | Optional: workflow automation (disabled by default) |

---

## Deployment Environments

| Environment | Purpose | Key Differences |
| ----------- | ------- | --------------- |
| Development | Local developer machine | `APP_ENV=development`, no license domain check, hot reload |
| Staging | VPS preview instance | Full production config, preview domain, used for client review |
| Production | VPS client instance | Client domain, valid license, real API credentials |

---

## Infrastructure Components and Choices

### Nginx (Reverse Proxy)

Nginx handles TLS termination, routes `/api` requests to the FastAPI backend, and routes all other requests to the Next.js frontend. This means both services are accessible on port 443 from a single domain, which simplifies DNS and SSL management.

The `nginx/bi-agent.conf` configuration is not included in this public version as it contains client-specific paths.

### Docker Volumes

Five named volumes persist data outside container lifecycles:

| Volume | Contents |
| ------ | -------- |
| `postgres_data` | All application database records |
| `redis_data` | Persistent Redis AOF log |
| `chromadb_data` | Embedded vectors for file RAG |
| `uploads` | Raw uploaded files (PDF, Excel, etc.) |
| `reports` | Generated PDF report files |
| `backups` | Database backup archives |

### Health Checks

Both the backend and PostgreSQL have Docker health checks configured. The frontend `depends_on` the backend health check before starting. This prevents the frontend from starting before the backend is ready to accept API calls.

### Network Isolation

All services communicate on an internal Docker bridge network (`bi_net`). Only the frontend and backend are exposed via Nginx. The database, Redis, and ChromaDB have no public ports.

---

## Deployment Steps (Summary)

1. Provision a Linux VPS (Ubuntu 22.04 or 24.04 recommended)
2. Install Docker and Docker Compose
3. Clone the repository to the VPS
4. Copy `.env.example` to `.env` and fill in all values
5. Point the client domain to the VPS IP in DNS
6. Configure Nginx with the client domain and SSL certificate (Certbot/Let's Encrypt)
7. Run `./start.sh` to pull images, run migrations, and start all services
8. Verify the health endpoint returns 200

### `start.sh` Sequence

```bash
docker compose pull
docker compose build
docker compose up -d postgres redis chromadb
# wait for postgres health check
docker compose run --rm backend alembic upgrade head
docker compose up -d
```

---

## Backup Strategy

A backup script (`scripts/backup.sh`) runs on a daily cron job on the VPS. It performs a `pg_dump` of the PostgreSQL database and compresses the output. Backups are retained for 30 days locally. Operators are advised to also sync backups to an off-site location (S3, Backblaze B2, or similar).

---

## Scaling Considerations

The stateless FastAPI backend can be scaled horizontally by adding more backend service replicas. Redis holds all shared state. Celery workers scale independently from the API server. For very high volume, the single-server Docker Compose model should be replaced with a container orchestration platform (Kubernetes or Docker Swarm) with a managed PostgreSQL and Redis instance.
