from src.schemas.domain_schema import DomainCreateSchema, DomainUpdateSchema, DomainReadSchema
from .base_usecase import BaseUseCase
from src.repositories.domain_repository import DomainRepository, domain_repository
from typing import AsyncGenerator
from typing import List


class DomainUseCase(BaseUseCase):
    """
    Use case for domain operations.
    """
    def __init__(self, repository: DomainRepository) -> None:
        super().__init__(repository)

    async def create(self, obj: DomainCreateSchema) -> DomainReadSchema:
        return await self._repository.create(obj=obj)
    
    async def get_by_id(self, id: int) -> DomainReadSchema:
        return await self._repository.get(id=id)
    
    async def update(self, obj: DomainUpdateSchema) -> DomainReadSchema:
        return await self._repository.update(obj=obj)

    async def delete_by_id(self, id: int) -> bool:
        return await self._repository.delete(id=id)
    
    async def list(self, page: int = 1, limit: int = 10) -> List[DomainReadSchema]:
        return await self._repository.list(limit=limit, offset = (page - 1) * limit)
    

async def get_domain_usecase() -> AsyncGenerator[DomainUseCase, None]:
    yield DomainUseCase(domain_repository)
