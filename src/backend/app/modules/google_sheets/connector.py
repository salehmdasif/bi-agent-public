"""
Google Sheets connector — Sheets API v4 via service account.
"""
from typing import Optional


async def read_sheet(
    credentials: dict,
    range_name: str = "Sheet1",
    max_rows: int = 100,
) -> dict:
    """
    Read data from a Google Sheet.

    Args:
        credentials: Decrypted dict with 'service_account_json' and 'sheet_id'.
        range_name: Sheet tab name or A1 notation range.
        max_rows: Maximum rows to return.

    Returns:
        Dict with 'range', 'values' (2D list), and 'row_count'.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


async def write_sheet(
    credentials: dict,
    range_name: str,
    values: list,
    append: bool = False,
) -> dict:
    """
    Write or append data to a Google Sheet.

    This is a write operation. It is only called after HITL approval.

    Args:
        credentials: Decrypted credential dict.
        range_name: Range to write, e.g. 'Sheet1!A2'.
        values: 2D list of values.
        append: True to append rows, False to overwrite the range.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


async def test_connection(credentials: dict) -> bool:
    """
    Verify that the service account can access the configured spreadsheet.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")
