from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.app.models.document import Document


class DocumentRepository:
    """
    Handles database operations for documents.
    """

    def __init__(self, db: Session):
        self.db = db

    def create(self, document: Document) -> Document:
        """
        Add a document to the current database session.
        """

        self.db.add(document)
        return document

    def get_by_id(self, document_uuid: UUID) -> Document | None:
        """
        Retrieve a document using its internal UUID.
        """

        return self.db.get(Document, document_uuid)

    def get_by_document_id(self, document_id: str) -> Document | None:
        """
        Retrieve a document using its business identifier.
        """

        statement = select(Document).where(
            Document.document_id == document_id
        )

        return self.db.scalar(statement)

    def list_documents(self) -> list[Document]:
        """
        Retrieve all documents, newest first.
        """

        statement = select(Document).order_by(
            Document.created_at.desc()
        )

        return list(self.db.scalars(statement).all())
