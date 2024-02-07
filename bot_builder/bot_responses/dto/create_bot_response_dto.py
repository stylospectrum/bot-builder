from typing import Optional

from .bot_response_base_dto import BotResponseBaseDto


class CreateBotResponseDto(BotResponseBaseDto):
    deleted: Optional[bool] = False
    image_id: Optional[str] = None
    pass
