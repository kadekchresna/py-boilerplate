from abc import ABC, abstractmethod

class IHealthUseCase(ABC):
    @abstractmethod
    async def get_health(self) -> dict:
        """Get the health status of the system"""
        pass