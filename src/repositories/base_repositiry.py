from abc import ABC, abstractmethod

from src.core.connections.database import Sessionable
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.base_model import BaseModel
from typing import TypeVar, Type

T = TypeVar("T", bound=BaseModel)

class BaseRepository(ABC):
    def __init__(self, sessionable_database: Sessionable, model: Type[T]) -> None:
        self.database = sessionable_database
        self.model = model

        
    @abstractmethod
    async def create(self, obj: T) -> T:
        pass

    @abstractmethod
    async def get(self, id: int) -> T:
        pass

    @abstractmethod
    async def update(self, obj: T) -> T:
        pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        pass

    


