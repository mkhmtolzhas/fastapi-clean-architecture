from fastapi import APIRouter
from .v1.router import router as v1_router

router = APIRouter(prefix="/api")


router.include_router(v1_router)

@router.get("/")
async def health_check():
    return {"status": "ok"}

