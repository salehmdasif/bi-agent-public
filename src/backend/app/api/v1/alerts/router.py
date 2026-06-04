"""
Alerts API routes.
Alert configuration and triggered alert history.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_db, get_current_user, require_admin

router = APIRouter(prefix="/alerts", tags=["Alerts"])


@router.get("/")
async def list_alerts(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(require_admin),
):
    """
    List all configured alerts with their current status.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


@router.post("/")
async def create_alert(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(require_admin),
):
    """
    Create a new alert with a threshold and notification configuration.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


@router.delete("/{alert_id}")
async def delete_alert(
    alert_id: str,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(require_admin),
):
    """
    Delete an alert configuration.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


@router.get("/history")
async def get_alert_history(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(require_admin),
):
    """
    Return triggered alert history with timestamps and metric values.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")
