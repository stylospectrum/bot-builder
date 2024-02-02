import uuid

from sqlmodel import Field, SQLModel
from datetime import datetime
from typing import Optional


class BotResponseGalleryItem(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4, primary_key=True)
    bot_response_id: uuid.UUID = Field(foreign_key="bot_response.id")
    image_id: uuid.UUID = Field(foreign_key="bot_response_image.id")
    title: str = Field(nullable=False)
    description: str = Field(nullable=False)
    created_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)
