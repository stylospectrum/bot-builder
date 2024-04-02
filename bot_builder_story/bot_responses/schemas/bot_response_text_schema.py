import uuid

from sqlmodel import Field, SQLModel, Relationship, Column, UUID, ForeignKey
from datetime import datetime
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .bot_response_schema import BotResponse


class BotResponseText(SQLModel, table=True):
    __tablename__ = "bot_response_text"

    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    bot_response_id: uuid.UUID = Field(
        sa_column=Column(UUID, ForeignKey("bot_response.id", ondelete="CASCADE"))
    )
    content: str = Field(nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    bot_response: Optional["BotResponse"] = Relationship(
        back_populates="variants",
    )
