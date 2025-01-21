

from ..repository import *
from .interface import IExampleUseCase
from ..model.example import Example


class ExampleUseCase(IExampleUseCase):
    def __init__(self, example_repository: IExampleRepository):
        self.example_repository = example_repository

    async def get_example(self) -> Example:
        try:
            return await self.example_repository.get_example()
        except Exception as e:
            raise e