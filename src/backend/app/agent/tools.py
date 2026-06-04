"""
Agent tools — LangChain StructuredTool implementations.
Each tool supports demo mode (no real API calls, realistic sample data).
"""
from typing import Optional
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession


def build_meta_ads_tools(db: AsyncSession, is_demo: bool) -> list[StructuredTool]:
    """
    Build LangChain tools for Meta Ads interaction.

    Provides: get_meta_campaigns, pause_meta_adset, enable_meta_adset,
    update_meta_adset_budget.

    Destructive tools (pause, enable, budget update) return a HITL signal
    instead of executing directly.

    Note:
        Tool implementation details are proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


def build_shopify_tools(db: AsyncSession, is_demo: bool) -> list[StructuredTool]:
    """
    Build LangChain tools for Shopify interaction.

    Provides: get_shopify_orders, get_shopify_products.

    Note:
        Tool implementation details are proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


def build_woocommerce_tools(db: AsyncSession, is_demo: bool) -> list[StructuredTool]:
    """
    Build LangChain tools for WooCommerce interaction.

    Provides: get_woocommerce_orders.

    Note:
        Tool implementation details are proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


def build_postgresql_tool(db_session: AsyncSession, is_demo: bool, llm) -> list[StructuredTool]:
    """
    Build a LangChain tool for natural language PostgreSQL queries.

    Generates a SELECT-only SQL query from the user's question using the
    configured LLM, validates it through sql_validator, injects a row limit,
    and executes it against the user's connected database.

    Note:
        Tool implementation details are proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


def build_mysql_tool(db_session: AsyncSession, is_demo: bool, llm) -> list[StructuredTool]:
    """
    Build a LangChain tool for natural language MySQL queries.

    Same safety pipeline as the PostgreSQL tool.

    Note:
        Tool implementation details are proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


def build_google_sheets_tools(db: AsyncSession, is_demo: bool) -> list[StructuredTool]:
    """
    Build LangChain tools for Google Sheets interaction.

    Provides: read_google_sheet, write_google_sheet.
    The write tool returns a HITL signal instead of executing directly.

    Note:
        Tool implementation details are proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


def build_chart_tool() -> list[StructuredTool]:
    """
    Build a LangChain tool for generating Plotly charts.

    Supports chart types: bar, line, pie, scatter.
    Returns Plotly JSON for inline rendering in the frontend.

    Note:
        Tool implementation details are proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


def build_rag_tool(user_id: str, is_demo: bool) -> list[StructuredTool]:
    """
    Build a LangChain tool for semantic search over uploaded files.

    Queries ChromaDB for the most relevant text chunks from the user's
    uploaded documents and returns them as context for the agent.

    Note:
        Tool implementation details are proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


async def build_agent_tools(
    db: AsyncSession,
    user_id: str,
    allowed_modules: list[str],
    is_demo: bool,
    llm,
) -> list[StructuredTool]:
    """
    Assemble the tool list for a specific user based on their permitted modules.

    Args:
        db: Async database session.
        user_id: The user's ID (used for scoping RAG queries).
        allowed_modules: List of module names the user has permission to use.
        is_demo: If True, all tools return sample data.
        llm: The configured LLM instance (needed by SQL generation tools).

    Returns:
        List of StructuredTool instances ready for LLM binding.

    Note:
        Tool assembly logic is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")
