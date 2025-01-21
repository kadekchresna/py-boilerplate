

from sqlalchemy import text, select
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from .interface.repository_interface import IExampleRepository
from .dao.example import ExampleDAO
from ..model.example import Example


class ExampleRepository(IExampleRepository):
    def __init__(self, db: Engine):
        self.db = db
        pass

    async def get_example(self) -> Example:
        try:
            session = Session(self.db)
            stmt = select(ExampleDAO).limit(1)
            result = session.execute(stmt)
            return result.scalar().to_example()
        except Exception as e:
            raise e