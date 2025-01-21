from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from ...model.example import Example

class Base(DeclarativeBase):
    pass

class ExampleDAO(Base):
    __tablename__ = "examples"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    def to_example(self) -> Example:
        return Example(
            id=self.id,
            name=self.name
        )