import uuid

from sqlmodel import Field, SQLModel, Enum, Relationship
from datetime import datetime
from typing import Optional, TYPE_CHECKING

from ..enum import StoryBlockType

if TYPE_CHECKING:
    from ...bot_responses.schemas.bot_response_schema import BotResponse
    from ...user_inputs.schemas.user_input_schema import UserInput
    from ...filters.schemas.filter_schema import Filter


class StoryBlock(SQLModel, table=True):
    __tablename__ = "story_block"

    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    name: Optional[str]
    type: StoryBlockType = Enum(StoryBlockType)
    user_id: str
    parent_id: Optional[uuid.UUID] = Field(foreign_key="story_block.id")
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    bot_responses: Optional[list["BotResponse"]] = Relationship(
        back_populates="story_block",
        sa_relationship_kwargs=dict(
            cascade="delete",
            passive_deletes=True
        ),
    )

    user_inputs: Optional[list["UserInput"]] = Relationship(
        back_populates="story_block",
        sa_relationship_kwargs=dict(
            cascade="delete",
            passive_deletes=True
        ),
    )

    filter: Optional["Filter"] = Relationship(
        back_populates="story_block",
        sa_relationship_kwargs=dict(
            cascade="delete",
            passive_deletes=True
        ),
    )

    parent: Optional["StoryBlock"] = Relationship(
        back_populates="children",
        sa_relationship_kwargs=dict(
            remote_side="StoryBlock.id",
            order_by="StoryBlock.created_at",
        ),
    )
    children: list["StoryBlock"] = Relationship(
        back_populates="parent",
        sa_relationship_kwargs=dict(
            order_by="StoryBlock.created_at",
        ),
    )
