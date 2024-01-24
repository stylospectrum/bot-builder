from typing import Annotated, Generator
from sqlmodel import Session
from fastapi import Depends

from ..postgres.engine import engine


def get_db() -> Generator:
    with Session(engine) as session:
        yield session


PostgresSessionDepend = Annotated[Session, Depends(get_db)]
