from fastapi import Depends, Request

from .dto.bot_response_out_dto import BotResponseOutDto
from .dto.create_bot_response_dto import CreateBotResponseDto
from .bot_responses_service import BotResponsesService
from ..decorators.controller import Controller, Get, Post
from ..decorators.validate_token import validate_token
from ..deps.auth_service_stub import AuthServiceStubDepend


@Controller('story-block/bot-response')
class BotResponsesController:
    bot_response_service: BotResponsesService = Depends(BotResponsesService)

    @Get('/{story_block_id}/', response_model=list[BotResponseOutDto])
    @validate_token
    def find(self, request: Request, auth_service_stub: AuthServiceStubDepend, story_block_id: str):
        return self.bot_response_service.find(story_block_id)

    @Post('/')
    @validate_token
    def create(self, request: Request, auth_service_stub: AuthServiceStubDepend, create_bot_response_dto: list[CreateBotResponseDto]):
        return self.bot_response_service.create(create_bot_response_dto)
