from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from .lifespan import lifespan
from src.api.api_router import router as api_router
from src.core.logger.logger import logger, Logger

class AppCreator:
    def __init__(self, lifespan: callable) -> None:
        self._app = FastAPI(lifespan=lifespan)

    def create_app(self) -> FastAPI:
        return self._app

    def add_router(self, router: APIRouter) -> None:
        self._app.include_router(router)

    def add_cors(self, allow_origins: List[str]) -> None:
        self._app.add_middleware(
            CORSMiddleware,
            allow_origins=allow_origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    
    def add_logging(self, logger: Logger) -> None:
        @self._app.middleware("http")
        async def log_request(request, call_next):
            logger.info(f"Request: {request.method} {request.url}")
            response = await call_next(request)
            logger.info(f"Response: {response.status_code}")
            return response
        
        

app_creator = AppCreator(lifespan=lifespan)
app_creator.add_router(api_router)
app_creator.add_cors(allow_origins=["*"])
app_creator.add_logging(logger)