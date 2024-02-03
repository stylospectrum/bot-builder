import uuid

from sqlmodel import SQLModel
from typing import Optional

from ..enum import BotResponseType


class BotResponseButtonDto(SQLModel):
    id: Optional[uuid.UUID] = None
    content: Optional[str] = None
    go_to: Optional[str] = None
    deleted: Optional[bool] = False

class BotResponseTextDto(SQLModel):
    id: Optional[uuid.UUID] = None
    content: Optional[str] = None
    deleted: Optional[bool] = False

class BotResponseBaseDto(SQLModel):
    id: Optional[uuid.UUID] = None
    story_block_id: Optional[uuid.UUID] = None
    type: Optional[BotResponseType]
    variants: Optional[list[BotResponseTextDto]] = None
    buttons: Optional[list[BotResponseButtonDto]] = None
