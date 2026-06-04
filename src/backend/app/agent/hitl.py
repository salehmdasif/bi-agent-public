"""
Human-in-the-Loop (HITL) manager.
Creates, retrieves, and resolves pending action records.
"""
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession


async def create_pending_action(
    conversation_id: str,
    user_id: str,
    action_type: str,
    action_data: dict,
    agent_suggestion: str,
    db: AsyncSession,
):
    """
    Create a PendingAction record for human approval.

    Called when a tool returns a hitl_required signal. The record is
    persisted so the frontend can render an approval card tied to it.

    Args:
        conversation_id: The conversation this action belongs to.
        user_id: The user who triggered the action.
        action_type: Machine-readable action identifier (e.g. 'pause_adset').
        action_data: Payload needed to execute the action (e.g. {'adset_id': '123'}).
        agent_suggestion: Human-readable description shown in the approval card.
        db: Async database session.

    Returns:
        The created PendingAction ORM object.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


async def approve_pending_action(
    action_id: str,
    user_id: str,
    db: AsyncSession,
) -> dict:
    """
    Execute an approved pending action against the external API.

    Args:
        action_id: The pending action record ID.
        user_id: Must match the user who originally created the action.
        db: Async database session.

    Returns:
        Execution result dict with status and confirmation message.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


async def reject_pending_action(
    action_id: str,
    user_id: str,
    db: AsyncSession,
) -> dict:
    """
    Mark a pending action as rejected. No external calls are made.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")
