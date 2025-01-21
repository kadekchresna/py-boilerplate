import os
import logging
from dotenv import load_dotenv
from fastapi import FastAPI

from .handler.http_route.v1.middleware import RateLimitMiddleware
from .handler.http_route.v1.health import HealthHandler
from .core.v1.health.usecase.health_usecase import HealthUseCase
from .core.v1.health.repository.health_repository import HealthRepository

from .handler.http_route.v1.example import ExampleHandler
from .core.v1.example.usecase.example_usecase import ExampleUseCase
from .core.v1.example.repository.example_repository import ExampleRepository


from .infrastructure.db import db

load_dotenv(dotenv_path=".env")
database = db.get_db_engine()

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s',
    handlers=[
        logging.StreamHandler()         # Logs to the console
    ]
)

app = FastAPI(title="Python FastAPI")
app.add_middleware(RateLimitMiddleware, max_requests=int(os.getenv("MAX_REQUESTS")), time_window=int(os.getenv("MAX_REQUESTS_TIME_FRAME")))

health_router = HealthHandler(HealthUseCase(HealthRepository(database)))
example_router = ExampleHandler(ExampleUseCase(ExampleRepository(database)))

app.include_router(health_router.router, prefix="/api/v1", tags=["health"])
app.include_router(example_router.router, prefix="/api/v1", tags=["health"])