"""
Agent Brain — LangGraph-powered multi-step reasoning agent.
Permission-aware, demo-mode-aware, HITL-integrated.
"""
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession


async def run_agent(
    user_id: str,
    message: str,
    db: AsyncSession,
    conversation_id: Optional[str] = None,
    file_ids: Optional[list[str]] = None,
    is_demo: bool = False,
) -> dict:
    """
    Run the agent for one user turn.

    Loads AI settings, assembles the user's permitted tool set, builds the
    LangGraph agentic loop, and returns a structured response.

    Args:
        user_id: The authenticated user's ID.
        message: The user's plain-language question or request.
        db: Async database session.
        conversation_id: Existing conversation ID to continue, or None to start a new one.
        file_ids: Optional list of uploaded file IDs to include in RAG context.
        is_demo: If True, all tools return realistic sample data instead of live API calls.

    Returns:
        Dict with keys: conversation_id, message_id, content, pending_action,
        chart_data, used_tools, token_count, is_demo.

    Note:
        Core agent loop logic, system prompt, and tool orchestration are proprietary
        and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")
