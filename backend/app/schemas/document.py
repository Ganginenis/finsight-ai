from datetime import datetime
from uuid import UUID
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StringConstraints


DocumentId = Annotated[
    str,
    StringConstraints(
        min_length=5,
        max_length=50,
        pattern=r"^DOC-[A-Za-z0-9][A-Za-z0-9_-]{0,45}$",
    ),
]

DocumentFilename = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        min_length=1,
        max_length=255,
    ),
]

DocumentContentType = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        min_length=1,
        max_length=100,
    ),
]


class DocumentCreate(BaseModel):
    """Request schema for registering a document."""

    document_id: DocumentId
    filename: DocumentFilename
    content_type: DocumentContentType
    file_size: int = Field(strict=True, ge=0)


class DocumentResponse(BaseModel):
    """Response schema for a registered document."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    document_id: str
    filename: str
    content_type: str
    file_size: int
    status: str
    created_at: datetime
    updated_at: datetime
