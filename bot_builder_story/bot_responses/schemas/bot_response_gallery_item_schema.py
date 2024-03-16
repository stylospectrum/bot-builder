import uuid

from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .bot_response_schema import BotResponse
    from .bot_response_button_schema import BotResponseButton


class BotResponseGalleryItem(SQLModel, table=True):
    __tablename__ = "bot_response_gallery_item"

    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    bot_response_id: uuid.UUID = Field(foreign_key="bot_response.id")
    title: str = Field(nullable=False)
    description: str = Field(nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    bot_response: Optional["BotResponse"] = Relationship(back_populates="gallery")
    buttons: Optional[list["BotResponseButton"]] = Relationship(
        back_populates="gallery_item",
        sa_relationship_kwargs=dict(
            order_by="BotResponseButton.updated_at",
        ),
    )
