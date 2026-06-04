"""
Admin API routes.
Data source management, AI settings, module configuration.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_db, require_admin

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/data-sources")
async def list_data_sources(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(require_admin),
):
    """
    List all data source modules with their connection status.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


@router.post("/data-sources/{source_name}/connect")
async def connect_data_source(
    source_name: str,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(require_admin),
):
    """
    Store encrypted credentials and mark a data source as connected.

    Credentials are encrypted with AES-256 before storage.
    A connection test is run before saving.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


@router.delete("/data-sources/{source_name}")
async def disconnect_data_source(
    source_name: str,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(require_admin),
):
    """
    Remove credentials and mark a data source as disconnected.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


@router.get("/ai-settings")
async def get_ai_settings(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(require_admin),
):
    """
    Get current AI configuration (provider, model, behavior settings).
    API key is not returned.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


@router.post("/ai-settings")
async def save_ai_settings(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(require_admin),
):
    """
    Save LLM provider, model, API key, and behavior settings.
    API key is encrypted before storage.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")
