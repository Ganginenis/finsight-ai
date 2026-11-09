from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.schemas.document import DocumentCreate, DocumentResponse
from backend.app.services.document_service import (
    DocumentAlreadyExistsError,
    DocumentService,
)


router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post(
    "/",
    response_model=DocumentResponse,
    status_code=status.HTTP_201_CREATED,
)
def register_document(
    payload: DocumentCreate,
    db: Annotated[Session, Depends(get_db)],
):
    service = DocumentService(db)

    try:
        return service.register_document(
            document_id=payload.document_id,
            filename=payload.filename,
            content_type=payload.content_type,
            file_size=payload.file_size,
        )

    except DocumentAlreadyExistsError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exc),
        ) from exc


@router.get(
    "/",
    response_model=list[DocumentResponse],
)
def list_documents(
    db: Annotated[Session, Depends(get_db)],
):
    service = DocumentService(db)
    return service.list_documents()


@router.get(
    "/{document_id}",
    response_model=DocumentResponse,
)
def get_document(
    document_id: str,
    db: Annotated[Session, Depends(get_db)],
):
    service = DocumentService(db)

    document = service.get_document(document_id)

    if document is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Document {document_id} not found",
        )

    return document
