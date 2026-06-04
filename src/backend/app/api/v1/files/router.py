"""
File upload API routes.
Manages uploaded files for RAG-based semantic search.
"""
from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_db, get_current_user

router = APIRouter(prefix="/files", tags=["Files"])


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Upload a document for RAG indexing.

    Supported types: PDF, CSV, XLSX, DOCX, TXT.
    File is validated for type and size, saved to disk, and queued
    for text extraction and embedding.

    Note:
        Upload handling and processing pipeline are proprietary
        and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


@router.get("/")
async def list_files(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    List all uploaded files for the current user.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


@router.delete("/{file_id}")
async def delete_file(
    file_id: str,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Delete an uploaded file and remove its vectors from ChromaDB.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")
