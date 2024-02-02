import uuid

from sqlmodel import Field, SQLModel
from datetime import datetime
from typing import Optional


class BotResponseImage(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4, primary_key=True)
    bot_response_id: uuid.UUID = Field(foreign_key="bot_response.id")
    url: str = Field(nullable=False)
    created_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)
