import uuid

from sqlmodel import Field, SQLModel
from datetime import datetime
from typing import Optional


class BotResponseText(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4, primary_key=True)
    bot_response_id: uuid.UUID = Field(foreign_key="bot_response.id")
    gallery_id: uuid.UUID = Field(foreign_key="bot_response_gallery.id")
    content: str = Field(nullable=False)
    go_to: str = Field(nullable=False)
    created_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)
