import re

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from backend.app.models.document import Document
from backend.app.repositories.document_repository import DocumentRepository


DOCUMENT_ID_PATTERN = re.compile(
    r"DOC-[A-Za-z0-9][A-Za-z0-9_-]{0,45}"
)

DOCUMENT_ID_UNIQUE_INDEX = "ix_documents_document_id"


class DocumentAlreadyExistsError(Exception):
    """Raised when a document identifier already exists."""


class DocumentService:
    """
    Handles business logic for document operations.
    """

    def __init__(self, db: Session):
        self.repository = DocumentRepository(db)
        self.db = db

    @staticmethod
    def _is_document_id_duplicate(exc: IntegrityError) -> bool:
        """
        Identify a unique violation specifically on document_id.
        """

        original_error = exc.orig
        sqlstate = getattr(original_error, "sqlstate", None)

        diagnostic = getattr(original_error, "diag", None)
        constraint_name = getattr(diagnostic, "constraint_name", None)

        return (
            sqlstate == "23505"
            and constraint_name == DOCUMENT_ID_UNIQUE_INDEX
        )

    def register_document(
        self,
        document_id: str,
        filename: str,
        content_type: str,
        file_size: int,
    ) -> Document:

        if (
            not isinstance(document_id, str)
            or not DOCUMENT_ID_PATTERN.fullmatch(document_id)
        ):
            raise ValueError(
                "Document ID must start with DOC- and contain "
                "only letters, numbers, hyphens, or underscores."
            )

        if not isinstance(filename, str) or not filename.strip():
            raise ValueError("Filename is required")

        filename = filename.strip()

        if len(filename) > 255:
            raise ValueError("Filename cannot exceed 255 characters")

        if not isinstance(content_type, str) or not content_type.strip():
            raise ValueError("Content type is required")

        content_type = content_type.strip()

        if len(content_type) > 100:
            raise ValueError("Content type cannot exceed 100 characters")

        if isinstance(file_size, bool) or not isinstance(file_size, int):
            raise ValueError("File size must be an integer")

        if file_size < 0:
            raise ValueError("File size cannot be negative")

        existing_document = self.repository.get_by_document_id(
            document_id
        )

        if existing_document:
            raise DocumentAlreadyExistsError(
                f"Document {document_id} already exists"
            )

        document = Document(
            document_id=document_id,
            filename=filename,
            content_type=content_type,
            file_size=file_size,
        )

        try:
            self.repository.create(document)
            self.db.commit()
            self.db.refresh(document)

            return document

        except IntegrityError as exc:
            self.db.rollback()

            if self._is_document_id_duplicate(exc):
                raise DocumentAlreadyExistsError(
                    f"Document {document_id} already exists"
                ) from exc

            # Preserve unexpected database errors.
            raise

        except Exception:
            self.db.rollback()
            raise

    def get_document(self, document_id: str) -> Document | None:
        return self.repository.get_by_document_id(document_id)

    def list_documents(self) -> list[Document]:
        return self.repository.list_documents()
