import uuid

from sqlmodel import Field, SQLModel, Enum
from datetime import datetime
from typing import Optional

from ..enum import BotResponseType


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
