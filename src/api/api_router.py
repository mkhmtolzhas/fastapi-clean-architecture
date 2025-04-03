from fastapi import APIRouter
from src.core.logger.logger import logger
from .v1.router import router as v1_router

router = APIRouter(prefix="/api")


router.include_router(v1_router)

@router.get("/api")
async def health_check():
    return {"status": "ok"}

