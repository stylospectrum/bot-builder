import uuid

from sqlmodel import Field, SQLModel, Enum, Relationship, Column, UUID, ForeignKey
from datetime import datetime
from typing import Optional, TYPE_CHECKING

from ..enum import FilterOperator

if TYPE_CHECKING:
    from ...story_blocks.schemas.story_block_schema import StoryBlock


class Filter(SQLModel, table=True):
    __tablename__ = "filter"

    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    variable_id: Optional[str]
    value: Optional[str]
    operator: FilterOperator = Enum(FilterOperator)
    story_block_id: uuid.UUID = Field(
        sa_column=Column(UUID, ForeignKey("story_block.id", ondelete="CASCADE"))
    )
    parent_id: Optional[uuid.UUID] = Field(foreign_key="filter.id")
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    parent: Optional["Filter"] = Relationship(
        back_populates="sub_exprs",
        sa_relationship_kwargs=dict(
            remote_side="Filter.id",
            order_by="Filter.created_at",
        ),
    )

    sub_exprs: list["Filter"] = Relationship(
        back_populates="parent",
        sa_relationship_kwargs=dict(
            order_by="Filter.created_at",
        ),
    )

    story_block: Optional["StoryBlock"] = Relationship(
        back_populates="filter",
    )
