from abc import ABC, abstractmethod
from contextlib import AbstractAsyncContextManager
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.base_model import BaseModel
from typing import Callable, TypeVar, Type, List
from src.schemas.base_schema import BaseSchema

T = TypeVar("T", bound=BaseModel)

class BaseRepository(ABC):
    def __init__(self, session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]], model: Type[T]) -> None:
        self.session_factory = session_factory
        self.model = model

    @abstractmethod
    async def create(self, obj: BaseSchema) -> BaseSchema:
        pass
            
    
    @abstractmethod
    async def get(self, id: int) -> BaseSchema:
        pass


    @abstractmethod
    async def update(self, obj: BaseSchema) -> BaseSchema:
        pass

    @abstractmethod
    async def delete(self, id: int) -> bool:
        pass

    @abstractmethod
    async def list(self, limit: int = 10, offset: int = 0) -> List[BaseSchema]:
        pass





    


