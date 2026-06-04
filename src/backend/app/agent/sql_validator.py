"""
SQL safety validator for AI-generated queries.
Prevents execution of non-SELECT statements and injects row limits.
"""


def safe_execute_check(sql: str) -> str | None:
    """
    Validate that a SQL string is safe to execute.

    Parses the SQL with sqlglot and checks for disallowed statement types.
    Returns an error string if validation fails, or None if the query is safe.

    Blocked patterns:
    - Any statement other than SELECT
    - DDL statements (CREATE, DROP, ALTER, TRUNCATE)
    - DML statements (INSERT, UPDATE, DELETE, MERGE)
    - Statements with CTEs that contain write operations

    Args:
        sql: The SQL string to validate.

    Returns:
        Error message string if unsafe, None if safe to execute.

    Note:
        Validation logic is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


def inject_row_limit(sql: str, limit: int = 100) -> str:
    """
    Rewrite a SQL SELECT query to enforce a row limit.

    If the query already has a LIMIT clause, it is replaced with the
    lower of the existing limit and the provided limit. If no LIMIT
    exists, one is appended.

    Args:
        sql: A validated SELECT query.
        limit: Maximum rows to allow (default 100).

    Returns:
        The rewritten SQL with row limit applied.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")
