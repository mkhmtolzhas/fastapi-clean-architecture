from contextlib import asynccontextmanager
from ..connections.connection import Connection
from ..connections.database import database
from ..connections.cache import cache
from ..logger.logger import logger




@asynccontextmanager
async def lifespan(app):
    logger.info("Starting up the application...")
    await startup(database)
    await startup(cache)
    logger.info("Application started up successfully.")
    yield
    logger.info("Shutting down the application...")
    await shutdown(database)
    await shutdown(cache)
    logger.info("Application shut down successfully.")


async def startup(app: Connection):
    await app.connect()


async def shutdown(app: Connection):
    await app.close()


