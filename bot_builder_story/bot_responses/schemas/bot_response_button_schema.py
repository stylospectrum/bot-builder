import uuid

from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .bot_response_schema import BotResponse
    from .bot_response_gallery_item_schema import BotResponseGalleryItem



class BotResponseButton(SQLModel, table=True):
    __tablename__ = "bot_response_button"

    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4, primary_key=True)
    bot_response_id: Optional[uuid.UUID] = Field(foreign_key="bot_response.id")
    gallery_item_id: Optional[uuid.UUID] = Field(foreign_key="bot_response_gallery_item.id")
    content: str = Field(nullable=False)
    go_to: str = Field(nullable=False)
    created_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)

    bot_response: Optional['BotResponse'] = Relationship(
        back_populates="buttons")
    gallery_item: Optional['BotResponseGalleryItem'] = Relationship(
        back_populates="buttons")
