from abc import ABC, abstractmethod

from ...model.example import Example

class IExampleRepository(ABC):
    @abstractmethod
    async def get_example(self) -> Example:
        """Implement this method to get an example"""
        pass