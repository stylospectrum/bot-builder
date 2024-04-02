import uuid

from sqlmodel import Field, SQLModel, Column, UUID, ForeignKey, Relationship
from datetime import datetime
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from ...story_blocks.schemas.story_block_schema import StoryBlock


class UserInput(SQLModel, table=True):
    __tablename__ = "user_input"

    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    story_block_id: uuid.UUID = Field(
        sa_column=Column(UUID, ForeignKey("story_block.id", ondelete="CASCADE"))
    )
    content: str = Field(nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    story_block: Optional["StoryBlock"] = Relationship(
        back_populates="user_inputs",
    )
