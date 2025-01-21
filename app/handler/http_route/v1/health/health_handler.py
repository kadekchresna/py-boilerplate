
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi import status
from typing import Dict, Any

from .....core.v1.health import IHealthUseCase

class HealthHandler():
    def __init__(self, health_usecase: IHealthUseCase):
        self.health_usecase = health_usecase
        self.router = APIRouter()
        self._register_routes()
    
    def _register_routes(self) -> None:
        self.router.add_api_route(
            "/health",
            self.get_health,
            methods=["GET"],
            response_model=Dict[str, Any],
            status_code=status.HTTP_200_OK
        )
    
    async def get_health(self)-> Dict[str, Any]:
        try:
            health_check = await self.health_usecase.get_health()
            if health_check.get("status") == False:
                return JSONResponse(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    content={
                        "message": "System unhealthy",
                        "status": False,
                        "details": {
                            "database": False
                        }
                    }
                )
            return {
                "message": "System healthy",
                "status": True,
                "details": {
                    "database": True
                }
            }
        except Exception as e:
            return JSONResponse(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                content={
                    "message": "System unhealthy",
                    "status": False,
                    "details": {
                        "database": False
                    }
                }
            )