from typing import Optional
from sqlmodel import SQLModel

from .bot_response_base_dto import BotResponseBaseDto
from ...story_blocks.dto.update_story_block_dto import UpdateStoryBlockDto


class CreateBotResponseDto(BotResponseBaseDto):
    deleted: Optional[bool] = False
    image_id: Optional[str] = None
    pass

class CreateBotResponseAndUpdateStoryBlockDto(SQLModel):
    bot_responses: list[CreateBotResponseDto]
    story_block: UpdateStoryBlockDto