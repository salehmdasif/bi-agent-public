"""
KPI API routes.
Returns normalized metric data for the dashboard.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_db, get_current_user

router = APIRouter(prefix="/kpi", tags=["KPI"])


@router.get("/summary")
async def get_kpi_summary(
    date_preset: str = "last_30d",
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Return aggregated KPI metrics from all connected and permitted data sources.

    Args:
        date_preset: Date range for the metrics. Options: last_7d, last_30d, last_90d.

    Returns:
        Dict with per-source KPI cards: spend, revenue, ROAS, orders, AOV, CTR.

    Note:
        KPI aggregation logic is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


@router.get("/chart/{metric}")
async def get_metric_chart(
    metric: str,
    date_preset: str = "last_30d",
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Return time-series data for a specific metric for chart rendering.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")
