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



class Sessionable(ABC):
    @abstractmethod
    def session_factory(self):
        raise NotImplementedError("Subclasses must implement get_session method")
