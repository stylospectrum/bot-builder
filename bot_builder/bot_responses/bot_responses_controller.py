from fastapi import Depends, Request

from .dto.bot_response_out_dto import BotResponseOutDto
from .dto.create_bot_response_dto import CreateBotResponseAndUpdateStoryBlockDto
from .bot_responses_service import BotResponsesService
from ..core.controller import Controller, Get, Post
from ..decorators.validate_token import validate_token
from ..deps.auth_service_stub import AuthServiceStubDepend
from ..story_blocks.story_blocks_service import StoryBlocksService
from ..story_blocks.dto.story_block_out_dto import StoryBlockOutDto


@Controller('story-block/bot-response')
class BotResponsesController:
    story_block_service: StoryBlocksService = Depends(StoryBlocksService)
    bot_response_service: BotResponsesService = Depends(BotResponsesService)

    @Get('/{story_block_id}/')
    @validate_token
    def find(self, request: Request, auth_service_stub: AuthServiceStubDepend, story_block_id: str):
        bot_response = self.bot_response_service.find(story_block_id)
        bot_response = [BotResponseOutDto.model_validate(response) for response in bot_response]
        story_block = self.story_block_service.find_by_id(story_block_id)

        return {
            "story_block": story_block,
            "bot_response": bot_response
        }


    @Post('/')
    @validate_token
    def create(self, request: Request, auth_service_stub: AuthServiceStubDepend, mixed: CreateBotResponseAndUpdateStoryBlockDto):
        user_id = request.__dict__['user'].id
        story_block = None
        bot_response = []

        if mixed.story_block.id:
            story_block = self.story_block_service.update(mixed.story_block, user_id)

        if len(mixed.bot_responses) > 0:
            bot_response = self.bot_response_service.create(mixed.bot_responses)

        return {
            "story_block": story_block,
            "bot_response": bot_response
        }
