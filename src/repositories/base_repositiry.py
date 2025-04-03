from abc import ABC, abstractmethod
from contextlib import AbstractAsyncContextManager
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.base_model import BaseModel
from typing import Callable, TypeVar, Type, Optional, List

T = TypeVar("T", bound=BaseModel)

class BaseRepository:
    def __init__(self, session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]], model: Type[T]) -> None:
        self.session_factory = session_factory
        self.model = model

    async def create(self, obj: T) -> T:
        async with self.session_factory() as session:
            try:
                await session.add(obj)
            except Exception as e:
                await session.rollback()
                raise e
            await session.commit()
            await session.refresh(obj)

            return obj
            

    async def get(self, id: int) -> Optional[T]:
        async with self.session_factory() as session:
            obj = await session.get(self.model, id)
            return obj

    async def update(self, obj: T) -> T:
        async with self.session_factory() as session:
            try:
                await session.merge(obj)
            except Exception as e:
                await session.rollback()
                raise e
            await session.commit()
            await session.refresh(obj)

            return obj

    async def delete(self, id: int) -> None:
        async with self.session_factory() as session:
            obj = await session.get(self.model, id)
            if obj:
                try:
                    await session.delete(obj)
                except Exception as e:
                    await session.rollback()
                    raise e
                await session.commit()
            else:
                raise ValueError(f"Object with id {id} not found")

    async def list(self, limit: int = 10, offset: int = 0) -> List[T]:
        async with self.session_factory() as session:
            query = select(self.model).limit(limit).offset(offset)
            try:
                result = await session.execute(query)
            except Exception as e:
                await session.rollback()
                raise e
            await session.commit()
            return result.scalars().all()


    


