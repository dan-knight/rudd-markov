# pyright: reportUnusedImport=false
from sqlalchemy import create_engine, Engine
from dotenv import dotenv_values

from markov.database.models import Base
from markov.database.models.event import Event


def get_engine() -> Engine:
    config = dotenv_values()
    database_uri: str | None = config.get("DATABASE_URI")
    if database_uri is None:
        raise ValueError("No \"DATABASE_URI\" environment variable specified.")
    
    return create_engine(database_uri)


engine: Engine = get_engine()


def reset_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
