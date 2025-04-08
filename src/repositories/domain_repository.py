from contextlib import AbstractAsyncContextManager
from typing import Callable, List

from sqlalchemy import select
from src.schemas.domain_schema import DomainCreateSchema, DomainUpdateSchema, DomainReadSchema
from src.utils.model_adapter import model_to_schema
from src.models.domain_model import DomainModel
from .base_repositiry import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.connections.database import database


class DomainRepository(BaseRepository):
    """
    Repository for domain operations.
    """
    def __init__(self, session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]]) -> None:
        super().__init__(session_factory, DomainModel)
    
    
    
    async def create(self, obj: DomainCreateSchema) -> DomainReadSchema:
        """
        Create a domain.
        """
        async with self.session_factory() as session:
            domain = self.model(**obj.dict())
            session.add(domain)
            await session.commit()
            await session.refresh(domain)
            return model_to_schema(domain, DomainReadSchema)
        
    
    async def get(self, id: int) -> DomainReadSchema:
        async with self.session_factory() as session:
            domain = await session.get(self.model, id)
            if not domain:
                return None
            return model_to_schema(domain, DomainReadSchema)
    
    async def update(self, obj: DomainUpdateSchema) -> DomainReadSchema:
        """
        Update a domain.
        """
        async with self.session_factory() as session:
            domain = await session.get(DomainModel, obj.id)
            if not domain:
                return None
            for key, value in obj.dict(exclude_unset=True).items():
                setattr(domain, key, value)
            await session.commit()
            await session.refresh(domain)
            return await model_to_schema(domain, DomainReadSchema)
        
    async def delete(self, id: int) -> bool:
        """
        Delete a domain.
        """
        async with self.session_factory() as session:
            domain = await session.get(DomainModel, id)
            if not domain:
                return False
            await session.delete(domain)
            await session.commit()
            return True
        
    async def list(self, limit = 10, offset = 0) -> List[DomainReadSchema]:
        async with self.session_factory() as session:
            domains = await session.execute(
                select(DomainModel).offset(offset).limit(limit)
            )
            domains = domains.scalars().all()
            return [model_to_schema(domain, DomainReadSchema) for domain in domains]
    

domain_repository = DomainRepository(database.session_factory())

