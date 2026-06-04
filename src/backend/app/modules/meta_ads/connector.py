"""
Meta Ads connector — Graph API v19.0.
Handles authentication and data fetching for the Meta Ads module.
"""
from typing import Optional


async def get_campaigns(
    credentials: dict,
    date_preset: str = "last_30d",
    limit: int = 20,
) -> dict:
    """
    Fetch campaign performance data from the Meta Ads Graph API.

    Args:
        credentials: Decrypted credential dict with 'access_token' and 'ad_account_id'.
        date_preset: Date range preset (last_7d, last_30d, last_90d, this_month).
        limit: Maximum number of campaigns to return.

    Returns:
        Dict with 'campaigns' list, 'total_spend', 'avg_roas', and 'period'.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


async def update_adset_status(
    credentials: dict,
    adset_id: str,
    status: str,
) -> dict:
    """
    Update the status of a Meta Ads ad set (ACTIVE or PAUSED).

    This is a write operation. It is only called after HITL approval.

    Args:
        credentials: Decrypted credential dict.
        adset_id: The ad set ID to update.
        status: 'ACTIVE' or 'PAUSED'.

    Returns:
        API response confirmation dict.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


async def update_adset_budget(
    credentials: dict,
    adset_id: str,
    daily_budget_usd: float,
) -> dict:
    """
    Update the daily budget of a Meta Ads ad set.

    This is a write operation. It is only called after HITL approval.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


async def test_connection(credentials: dict) -> bool:
    """
    Verify that the provided credentials can reach the Meta Ads API.

    Returns True if the connection succeeds, raises an exception with
    a human-readable error message if it fails.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")
