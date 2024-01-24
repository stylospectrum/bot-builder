import uuid

from sqlmodel import SQLModel
from typing import Optional

from ..enum import StoryBlockType

class StoryBlockBaseDto(SQLModel):
  id: Optional[uuid.UUID] = None
  name: Optional[str] = None
  type: StoryBlockType
  user_id: str
  parent_id: Optional[uuid.UUID] = None