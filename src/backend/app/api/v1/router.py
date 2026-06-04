"""
API v1 root router. Aggregates all feature routers.
"""
from fastapi import APIRouter

from app.api.v1.auth.router import router as auth_router
from app.api.v1.chat.router import router as chat_router
from app.api.v1.kpi.router import router as kpi_router
from app.api.v1.insights.router import router as insights_router
from app.api.v1.alerts.router import router as alerts_router
from app.api.v1.reports.router import router as reports_router
from app.api.v1.files.router import router as files_router
from app.api.v1.users.router import router as users_router
from app.api.v1.admin.router import router as admin_router
from app.api.v1.super_admin.router import router as super_admin_router
from app.api.v1.activity.router import router as activity_router
from app.api.v1.profile.router import router as profile_router
from app.api.v1.telegram.router import router as telegram_router
from app.api.v1.public.router import router as public_router
from app.api.v1.health.router import router as health_router
from app.api.v1.onboarding.router import router as onboarding_router

api_router = APIRouter()

api_router.include_router(health_router)
api_router.include_router(auth_router)
api_router.include_router(chat_router)
api_router.include_router(kpi_router)
api_router.include_router(insights_router)
api_router.include_router(alerts_router)
api_router.include_router(reports_router)
api_router.include_router(files_router)
api_router.include_router(users_router)
api_router.include_router(admin_router)
api_router.include_router(super_admin_router)
api_router.include_router(activity_router)
api_router.include_router(profile_router)
api_router.include_router(telegram_router)
api_router.include_router(public_router)
api_router.include_router(onboarding_router)
