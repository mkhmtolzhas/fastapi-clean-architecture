from abc import ABC, abstractmethod

class Connection(ABC):
    @abstractmethod
    async def connect(self):
        """Establish a connection."""
        pass

    @abstractmethod
    async def close(self):
        """Close the connection."""
        pass