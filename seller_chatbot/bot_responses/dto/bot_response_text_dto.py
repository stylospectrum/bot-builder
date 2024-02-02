import uuid

from sqlmodel import SQLModel

class BotResponseTextDto(SQLModel):
  content: str = None