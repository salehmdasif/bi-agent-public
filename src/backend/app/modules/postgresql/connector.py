"""
PostgreSQL connector — direct asyncpg connection with natural language to SQL.
"""


async def execute_nl_query(
    credentials: dict,
    question: str,
    table_hint: str = "",
    llm=None,
    row_limit: int = 100,
) -> dict:
    """
    Execute a natural language query against a connected PostgreSQL database.

    Flow:
      1. Build a SQL generation prompt from the user's question
      2. Call the LLM to generate a SELECT query
      3. Validate the SQL through sql_validator
      4. Inject a row limit
      5. Execute against the user's database via asyncpg
      6. Return results as columns + rows

    Args:
        credentials: Decrypted dict with host, port, database, username, password.
        question: Natural language question to answer from the database.
        table_hint: Optional schema hint to improve SQL generation accuracy.
        llm: The configured LLM instance for SQL generation.
        row_limit: Maximum rows to return.

    Returns:
        Dict with 'columns', 'rows', 'row_count', and 'sql_used'.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


async def test_connection(credentials: dict) -> bool:
    """
    Verify that the provided credentials can connect to the PostgreSQL database.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")
