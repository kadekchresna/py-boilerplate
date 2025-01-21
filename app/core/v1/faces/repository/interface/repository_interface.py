from abc import ABC, abstractmethod

class IExampleRepository(ABC):
    @abstractmethod
    async def get_example(self) -> dict:
        """Implement this method to get an example"""
        pass