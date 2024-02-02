import uuid

from sqlmodel import SQLModel
from typing import Optional

from ..enum import BotResponseType
from .bot_response_text_dto import BotResponseTextDto


class BotResponseBaseDto(SQLModel):
    id: Optional[uuid.UUID] = None
    story_block_id: Optional[uuid.UUID] = None
    type: Optional[BotResponseType]
    text: Optional[BotResponseTextDto] = None
    variants: Optional[list[BotResponseTextDto]] = None
