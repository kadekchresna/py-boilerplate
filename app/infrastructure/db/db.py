from sqlalchemy import create_engine, Engine


def get_db_engine() -> Engine:
    return create_engine("postgresql://postgres:admin@localhost:5432/postgres?sslmode=disable")