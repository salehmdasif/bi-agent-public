"""
Shopify connector — Admin REST API 2024-01.
"""
from typing import Optional


async def get_orders(
    credentials: dict,
    days: int = 30,
    status: str = "any",
    limit: int = 50,
) -> dict:
    """
    Fetch order data from the Shopify Admin API.

    Args:
        credentials: Decrypted dict with 'store_url' and 'access_token'.
        days: Number of days to look back.
        status: Order status filter.
        limit: Maximum orders to return.

    Returns:
        Dict with total_orders, total_revenue, average_order_value, and sample orders.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


async def get_products(
    credentials: dict,
    limit: int = 50,
    stock_alert_only: bool = False,
) -> dict:
    """
    Fetch product and inventory data from Shopify.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


async def test_connection(credentials: dict) -> bool:
    """
    Verify that the provided credentials can reach the Shopify API.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")
