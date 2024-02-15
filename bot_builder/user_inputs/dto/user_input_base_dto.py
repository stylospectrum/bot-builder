import uuid

from sqlmodel import SQLModel
from typing import Optional

class UserInputBaseDto(SQLModel):
    id: Optional[uuid.UUID] = None
    content: Optional[str] = None
    deleted: Optional[bool] = False
    story_block_id: Optional[uuid.UUID] = None