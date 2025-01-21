

from sqlalchemy import text
from sqlalchemy.engine import Engine

from .interface.repository_interface import IHealthRepository


class HealthRepository(IHealthRepository):
    def __init__(self, db: Engine):
        self.db = db
        pass

    async def get_health_status(self) -> bool:
        try:
            raw_query = text("SELECT 1")
            db = self.db.connect()
            db.execute(raw_query)
            db.close()
            return True
        except Exception as e:
            return False
