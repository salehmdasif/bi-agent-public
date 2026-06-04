"""
BI Agent Platform — FastAPI application entry point.

Startup sequence:
  1. Initialize Redis connection
  2. Run database table creation (Alembic handles migrations in production)
  3. Seed default modules
  4. Ensure system accounts exist
  5. Register Telegram webhook if configured
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import os

from app.core.config import settings
from app.core.database import engine, Base
from app.core.redis_client import init_redis, close_redis
from app.core.module_registry import seed_default_modules, load_module_cache
from app.core.rate_limit import limiter, rate_limit_exceeded_handler
from app.core.license_middleware import LicenseMiddleware
from app.api.v1.router import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan: startup and shutdown."""
    await init_redis()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    from app.core.database import AsyncSessionLocal
    async with AsyncSessionLocal() as db:
        await seed_default_modules(db)
        await load_module_cache(db)
        await _ensure_system_accounts(db)
    await _register_telegram_webhook()
    yield
    from app.core.redis_client import close_redis
    await close_redis()
    await engine.dispose()


async def _ensure_system_accounts(db):
    """
    Create required system accounts on first boot.

    Note:
        System account logic is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


async def _register_telegram_webhook():
    """
    Register Telegram webhook URL on startup if bot token is configured.

    Note:
        Webhook registration logic is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    lifespan=lifespan,
)

app.state.limiter = limiter
app.add_middleware(LicenseMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=settings.UPLOAD_DIR), name="uploads")

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"app": settings.APP_NAME, "status": "running"}
