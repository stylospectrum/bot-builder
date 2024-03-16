import uuid

from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime
from typing import Optional


class UserInput(SQLModel, table=True):
    __tablename__ = "user_input"

    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    story_block_id: uuid.UUID = Field(foreign_key="story_block.id")
    content: str = Field(nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
