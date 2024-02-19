from typing import Optional

from .bot_response_base_dto import BotResponseBaseDto


class BotResponseOutDto(BotResponseBaseDto):
    image_url: Optional[str] = None
    pass
