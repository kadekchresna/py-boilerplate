
from ..repository import *
from .interface import IHealthUseCase


class HealthUseCase(IHealthUseCase):
    def __init__(self, health_repository: IHealthRepository):
        self.health_repository = health_repository

    async def get_health(self):
        db = await self.health_repository.get_health_status()
        if not db:
            return {"message": "not ok", "status": False}
        return {"message": "ok", "status": True}