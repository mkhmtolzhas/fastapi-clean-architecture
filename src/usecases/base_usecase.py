from typing import Protocol
from src.schemas.base_schema import BaseSchema
from typing import List
from abc  import ABC, abstractmethod

class RepositoryProtocol(Protocol):
    async def create(self, obj: object) -> object:
        ...

    async def get(self, id: int) -> object:
        ...

    async def update(self, obj: object) -> object:
        ...

    async def delete(self, id: int) -> None:
        ...

    async def list(self, limit: int = 10, offset: int = 0) -> List[object]:
        ...


class BaseUseCase(ABC):
    def __init__(self, repository: RepositoryProtocol) -> None:
        self._repository = repository

    @abstractmethod
    async def create(self, obj: BaseSchema) -> BaseSchema:
        """Create an object in the repository."""
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> BaseSchema:
        """Get an object from the repository by ID."""
        pass

    @abstractmethod
    async def update(self, obj: BaseSchema) -> BaseSchema:
        """Update an object in the repository."""
        pass

    @abstractmethod
    async def delete_by_id(self, id: int) -> bool:
        """Delete an object from the repository by ID."""
        pass

    @abstractmethod
    async def list(self, limit: int = 10, offset: int = 0) -> List[BaseSchema]:
        """List objects from the repository."""
        pass

    