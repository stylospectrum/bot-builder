from typing import Optional
from sqlmodel import SQLModel

from .bot_response_base_dto import BotResponseBaseDto
from ...story_blocks.dto.update_story_block_dto import UpdateStoryBlockDto


class CreateBotResponseBaseDto(BotResponseBaseDto):
    deleted: Optional[bool] = False
    image_id: Optional[str] = None
    pass

class CreateBotResponseDto(SQLModel):
    bot_responses: list[CreateBotResponseBaseDto]
    story_block: UpdateStoryBlockDto