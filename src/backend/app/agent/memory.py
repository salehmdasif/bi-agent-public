"""
Conversation memory management.
Loads and saves message history with a sliding window.
"""
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession


async def get_or_create_conversation(
    user_id: str,
    db: AsyncSession,
    conversation_id: Optional[str] = None,
    is_demo: bool = False,
):
    """
    Get an existing conversation or create a new one.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


async def get_conversation_history(
    conversation_id: str,
    db: AsyncSession,
    window: int = 20,
) -> list:
    """
    Load the last N messages from a conversation as LangChain message objects.

    Args:
        conversation_id: The conversation to load.
        db: Async database session.
        window: Maximum number of messages to load (sliding window).

    Returns:
        List of LangChain HumanMessage and AIMessage objects.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


async def save_message(
    conversation_id: str,
    role: str,
    content: str,
    db: AsyncSession,
    tool_calls: Optional[dict] = None,
):
    """
    Persist a single message to the conversation.

    Args:
        conversation_id: The conversation to append to.
        role: 'user' or 'assistant'.
        content: Message text content.
        db: Async database session.
        tool_calls: Optional metadata about which tools were used.

    Returns:
        The created Message ORM object.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")
