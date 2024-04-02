import uuid

from sqlmodel import Field, SQLModel, Relationship, Column, UUID, ForeignKey
from datetime import datetime
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .bot_response_button_schema import BotResponseButton


class BotResponseButtonExpr(SQLModel, table=True):
    __tablename__ = "bot_response_button_expr"

    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    button_id: Optional[uuid.UUID] = Field(
        sa_column=Column(UUID, ForeignKey("bot_response_button.id", ondelete="CASCADE"))
    )
    variable_id: str = Field(nullable=False)
    value: str = Field(nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    button: Optional["BotResponseButton"] = Relationship(back_populates="exprs")
