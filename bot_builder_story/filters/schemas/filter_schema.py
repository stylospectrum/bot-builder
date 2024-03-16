import uuid

from sqlmodel import Field, SQLModel, Enum, Relationship
from datetime import datetime
from typing import Optional

from ..enum import FilterOperator


class Filter(SQLModel, table=True):
    __tablename__ = "filter"

    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    attribute: Optional[str]
    value: Optional[str]
    operator: FilterOperator = Enum(FilterOperator)
    story_block_id: str
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
