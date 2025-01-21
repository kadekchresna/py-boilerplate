import os
from sqlalchemy import create_engine, Engine


def get_db_engine() -> Engine:
    return create_engine(os.getenv("POSTGRES_URL"))