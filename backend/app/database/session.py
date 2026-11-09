from collections.abc import Generator

from sqlalchemy.orm import Session, sessionmaker

from backend.app.database.database import engine


SessionLocal = sessionmaker(
    bind=engine,
    class_=Session,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


def get_db() -> Generator[Session, None, None]:
    """
    Provide a database session for the duration of a request.
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
