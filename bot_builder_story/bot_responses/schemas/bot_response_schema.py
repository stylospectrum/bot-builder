import uuid

from sqlmodel import Field, SQLModel, Enum, Relationship, Column, UUID, ForeignKey
from datetime import datetime
from typing import Optional, TYPE_CHECKING

from ..enum import BotResponseType

if TYPE_CHECKING:
    from .bot_response_text_schema import BotResponseText
    from .bot_response_button_schema import BotResponseButton
    from .bot_response_gallery_item_schema import BotResponseGalleryItem
    from ...story_blocks.schemas.story_block_schema import StoryBlock


class BotResponse(SQLModel, table=True):
    __tablename__ = "bot_response"

    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    story_block_id: uuid.UUID = Field(
        sa_column=Column(UUID, ForeignKey("story_block.id", ondelete="CASCADE"))
    )
    type: BotResponseType = Enum(BotResponseType)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    story_block: Optional["StoryBlock"] = Relationship(
        back_populates="bot_responses",
    )

    gallery: Optional[list["BotResponseGalleryItem"]] = Relationship(
        back_populates="bot_response",
        sa_relationship_kwargs=dict(
            cascade="delete",
            passive_deletes=True,
            order_by="BotResponseGalleryItem.updated_at",
        ),
    )

    variants: Optional[list["BotResponseText"]] = Relationship(
        back_populates="bot_response",
        sa_relationship_kwargs=dict(
            cascade="delete",
            passive_deletes=True,
            order_by="BotResponseText.created_at",
        ),
    )

    buttons: Optional[list["BotResponseButton"]] = Relationship(
        back_populates="bot_response",
        sa_relationship_kwargs=dict(
            cascade="delete",
            passive_deletes=True,
            order_by="BotResponseButton.updated_at",
        ),
    )
