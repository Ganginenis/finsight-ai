from sqlalchemy import create_engine

from backend.app.core.config import get_settings


settings = get_settings()


engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
)
