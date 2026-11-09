from fastapi import APIRouter

from backend.app.api.v1.documents import router as documents_router


api_router = APIRouter()


@api_router.get("/", tags=["API"])
async def api_root():
    """
    Return information about the current API version.
    """
    return {
        "api_version": "v1",
        "message": "FinSight AI API is operational",
    }


api_router.include_router(documents_router)
