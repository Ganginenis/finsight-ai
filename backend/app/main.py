from fastapi import FastAPI

from backend.app.api.v1.router import api_router
from backend.app.core.config import get_settings


# Load application configuration.
settings = get_settings()


# Initialize the FastAPI application.
app = FastAPI(
    title=settings.app_name,
    description=(
        "Intelligent Financial Operations and Risk Intelligence "
        "Platform"
    ),
    version="0.1.0",
    debug=settings.debug,
)


# Include versioned API routes.
app.include_router(
    api_router,
    prefix=settings.api_v1_prefix,
)


@app.get("/", tags=["General"])
async def root():
    """
    Return basic application information.
    """
    return {
        "application": settings.app_name,
        "message": "Welcome to FinSight AI",
        "version": "0.1.0",
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """
    Check whether the API application is running.
    """
    return {
        "status": "healthy",
        "application": settings.app_name,
    }
