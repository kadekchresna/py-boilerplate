from abc import ABC, abstractmethod

class IHealthRepository(ABC):
    @abstractmethod
    async def get_health_status(self) -> bool:
        """Get the health status of the system"""
        pass