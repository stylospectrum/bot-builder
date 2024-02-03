import uuid

from sqlmodel import Field, SQLModel, Enum, Relationship
from datetime import datetime
from typing import Optional, TYPE_CHECKING

from ..enum import BotResponseType

if TYPE_CHECKING:
    from .bot_response_text_schema import BotResponseText
    from .bot_response_button_schema import BotResponseButton


class BotResponse(SQLModel, table=True):
    __tablename__ = "bot_response"

    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4, primary_key=True)
    story_block_id: uuid.UUID = Field(foreign_key="story_block.id")
    type: BotResponseType = Enum(BotResponseType)
    created_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)

    variants: Optional[list['BotResponseText']] = Relationship(
        back_populates="bot_response", sa_relationship_kwargs=dict(
            order_by='BotResponseText.created_at',
        ))

    buttons: Optional[list['BotResponseButton']] = Relationship(
        back_populates="bot_response", sa_relationship_kwargs=dict(
            order_by='BotResponseButton.updated_at',
        ))
