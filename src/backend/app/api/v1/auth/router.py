"""
Authentication API routes.
Handles login, token refresh, logout, and password reset flows.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_db
from app.schemas.auth import LoginRequest, TokenResponse, RefreshRequest

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=TokenResponse)
async def login(
    payload: LoginRequest,
    db: AsyncSession = Depends(get_db),
):
    """
    Authenticate a user and return access and refresh tokens.

    Accepts username or email. Returns short-lived access token (15 min)
    and longer-lived refresh token (7 days).

    Note:
        Authentication logic is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


@router.post("/refresh", response_model=TokenResponse)
async def refresh_token(
    payload: RefreshRequest,
    db: AsyncSession = Depends(get_db),
):
    """
    Exchange a valid refresh token for a new access token.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


@router.post("/logout")
async def logout(db: AsyncSession = Depends(get_db)):
    """
    Invalidate the current session tokens.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


@router.post("/forgot-password")
async def forgot_password(db: AsyncSession = Depends(get_db)):
    """
    Send a password reset email with a time-limited reset token.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


@router.post("/reset-password")
async def reset_password(db: AsyncSession = Depends(get_db)):
    """
    Set a new password using a valid reset token.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")
