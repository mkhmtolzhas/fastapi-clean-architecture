from redis.asyncio import Redis
from ..config import settings, Settings
from .connection import Connection
from ..logger.logger import logger

class RedisConnection(Connection):
    def __init__(self, settings: Settings):
        self.redis = Redis.from_url(
            url=settings.redis_url(),
            decode_responses=True,
        )
        logger.info(f"Redis URL: {settings.redis_url()}")
    
    async def connect(self):
        try:
            await self.redis.ping()
            logger.info("Connected to Redis")
        except Exception as e:
            logger.error(f"Failed to connect to Redis: {e}")
            raise e
    
    async def close(self):
        try:
            await self.redis.close()
            logger.info("Disconnected from Redis")
        except Exception as e:
            logger.error(f"Failed to disconnect from Redis: {e}")
            raise e


redis = RedisConnection(settings=settings)