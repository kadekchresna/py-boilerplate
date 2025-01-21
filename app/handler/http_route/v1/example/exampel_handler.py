
import logging
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import status
from typing import Dict, Any

from .....core.v1.example import IExampleUseCase
from .....core.v1.example.model.example import Example

class ExampleHandler():
    def __init__(self, example_usecase: IExampleUseCase):
        self.example_usecase = example_usecase
        self.router = APIRouter()
        self._register_routes()
    
    def _register_routes(self) -> None:
        self.router.add_api_route(
            "/example",
            self.get_health,
            methods=["GET"],
            response_model=Dict[str, Any],
            status_code=status.HTTP_200_OK
        )
    
    async def get_health(self)-> Dict[str, Any]:
        try:
            ex = await self.example_usecase.get_example()
            if ex is not None:
                return {
                    "message": "Success",
                    "status": True,
                    "data": jsonable_encoder(ex)
                }

        except Exception as e:
            logging.error(f"ERROR OCCURRED. \n{e}")
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "message": "Failed. Please try again later",
                    "status": False,
                    "error": str(e)
                }
            )