from fastapi import APIRouter


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
