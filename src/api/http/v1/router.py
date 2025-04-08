from fastapi import APIRouter
from .endpoints.domain_router import router as domain_router

router = APIRouter(prefix="/v1")


router.include_router(domain_router)