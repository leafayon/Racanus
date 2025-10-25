from sqlalchemy import create_engine

from .settings import Settings

DATABASE_ENGINE = create_engine(f"sqlite:///{Settings().racanus_database_name}.db")
