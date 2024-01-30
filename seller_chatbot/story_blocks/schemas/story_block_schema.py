import uuid

from sqlmodel import Field, SQLModel, Enum, Relationship
from datetime import datetime

from typing import Optional
from ..enum import StoryBlockType


class StoryBlock(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4, primary_key=True)
    name: Optional[str]
    type: StoryBlockType = Enum(StoryBlockType)
    user_id: str
    parent_id: Optional[uuid.UUID] = Field(foreign_key="storyblock.id")
    created_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)

    parent: Optional['StoryBlock'] = Relationship(
        back_populates='children',
        sa_relationship_kwargs=dict(
            remote_side='StoryBlock.id',
        )
    )
    children: list['StoryBlock'] = Relationship(back_populates='parent')
