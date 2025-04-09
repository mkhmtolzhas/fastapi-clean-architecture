from contextlib import asynccontextmanager
from ..connections.connection import Connection
from ..connections.postgres_connection import postgres
from ..connections.redis_connection import redis
from ..logger.logger import logger




@asynccontextmanager
async def lifespan(app):
    logger.info("Starting up the application...")
    await startup(postgres)
    await startup(redis)
    logger.info("Application started up successfully.")
    yield
    logger.info("Shutting down the application...")
    await shutdown(postgres)
    await shutdown(redis)
    logger.info("Application shut down successfully.")


async def startup(app: Connection):
    await app.connect()


async def shutdown(app: Connection):
    await app.close()


