from .bot_responses_service import BotResponsesService
from .bot_responses_controller import BotResponsesController


class BotResponsesModule:
    controllers = [BotResponsesController]
    services = [BotResponsesService]
