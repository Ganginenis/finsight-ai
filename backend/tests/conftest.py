import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.engine import make_url
from sqlalchemy.orm import Session, sessionmaker

from backend.app.core.config import get_settings
from backend.app.database.base import Base
from backend.app.database.session import get_db
from backend.app.main import app
from backend.app.models.document import Document  # noqa: F401


@pytest.fixture(scope="session")
def test_engine():
    settings = get_settings()
    database_url = make_url(settings.test_database_url)

    # Safety guard: never run test setup against another database.
    if database_url.database != "finsight_test":
        raise RuntimeError(
            "Refusing to run tests: database must be finsight_test."
        )

    engine = create_engine(
        settings.test_database_url,
        pool_pre_ping=True,
    )

    try:
        Base.metadata.create_all(bind=engine)
        yield engine
    finally:
        try:
            Base.metadata.drop_all(bind=engine)
        finally:
            engine.dispose()


@pytest.fixture
def db_session(test_engine):
    connection = test_engine.connect()
    transaction = connection.begin()

    TestingSessionLocal = sessionmaker(
        bind=connection,
        class_=Session,
        autoflush=False,
        autocommit=False,
        expire_on_commit=False,
        join_transaction_mode="create_savepoint",
    )

    session = TestingSessionLocal()

    try:
        yield session
    finally:
        session.close()

        if transaction.is_active:
            transaction.rollback()

        connection.close()


@pytest.fixture
def client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        app.dependency_overrides.pop(get_db, None)
