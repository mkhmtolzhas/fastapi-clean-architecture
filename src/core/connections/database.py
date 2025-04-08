from abc import ABC, abstractmethod
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from src.core.logger.logger import logger
from src.core.config import settings, Settings
from .connection import Connection


class Sessionable(ABC):
    @abstractmethod
    def session_factory(self) -> async_sessionmaker:
        raise NotImplementedError("Subclasses must implement get_session method")


class Database(Connection, Sessionable):
    def __init__(self, settings: Settings) -> None:
        self.engine = create_async_engine(
            settings.db_async_url(),
            echo=False,
        )
        self._session_factory = async_sessionmaker(self.engine, class_=AsyncSession, expire_on_commit=False)

    def session_factory(self) -> async_sessionmaker:
        return self._session_factory

    async def connect(self):
        try:
            async with self.engine.connect() as conn:
                await conn.execute(text("SELECT 1"))
                logger.info(f"Database connection URL: {settings.db_async_url()}")
        except Exception as e:
            print(f"Failed to connect to the database: {e}")
            raise e

    
    async def close(self):
        try:
            await self.engine.dispose()
            logger.info("Disconnected from the database")
        except Exception as e:
            logger.error(f"Failed to disconnect from the database: {e}")
            raise e




database = Database(settings)

