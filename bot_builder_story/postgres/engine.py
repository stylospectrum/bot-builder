from sqlmodel import create_engine, SQLModel
from ..config.settings import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI.unicode_string())

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)