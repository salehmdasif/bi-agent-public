"""
Chat API routes.
Handles message submission, conversation management, and HITL approvals.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_db, get_current_user
from app.schemas.chat import ChatMessageRequest, ChatMessageResponse

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/message", response_model=ChatMessageResponse)
async def send_message(
    payload: ChatMessageRequest,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Send a message to the AI agent and receive a response.

    Runs the LangGraph agent loop, returns the assistant's reply with
    optional chart data, used tools list, and any pending HITL action.

    Note:
        Business logic is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


@router.get("/conversations")
async def list_conversations(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    List all conversations for the current user, ordered by most recent.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


@router.get("/conversations/{conversation_id}/messages")
async def get_conversation_messages(
    conversation_id: str,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Load all messages for a specific conversation.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


@router.post("/approve/{action_id}")
async def approve_action(
    action_id: str,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Approve a pending HITL action and execute it.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


@router.post("/reject/{action_id}")
async def reject_action(
    action_id: str,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Reject a pending HITL action without executing it.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")
