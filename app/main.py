
from fastapi import FastAPI

from .handler.http_route.v1.health import HealthHandler
from .core.v1.health.usecase.health_usecase import HealthUseCase
from .core.v1.health.repository.health_repository import HealthRepository

from .infrastructure.db import db

app = FastAPI(title="Python FastAPI")

database = db.get_db_engine()

health_router = HealthHandler(HealthUseCase(HealthRepository(database)))
app.include_router(health_router.router, prefix="/api/v1", tags=["health"])

# health_router.get_health()