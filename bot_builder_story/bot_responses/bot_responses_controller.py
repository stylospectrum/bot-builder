from fastapi import Depends, Request

from .dto.bot_response_out_dto import BotResponseOutDto
from .dto.create_bot_response_dto import CreateBotResponseDto
from .bot_responses_service import BotResponsesService
from ..core.controller import Controller, Get, Post
from ..decorators.validate_token import validate_token
from ..deps.auth_service_stub import AuthServiceStubDepend
from ..story_blocks.story_blocks_service import StoryBlocksService


@Controller("bot-response")
class BotResponsesController:
    story_block_service: StoryBlocksService = Depends(StoryBlocksService)
    bot_response_service: BotResponsesService = Depends(BotResponsesService)

    @Get("/{story_block_id}/")
    @validate_token
    def find(
        self,
        request: Request,
        auth_service_stub: AuthServiceStubDepend,
        story_block_id: str,
    ):
        bot_responses = self.bot_response_service.find(story_block_id)
        bot_responses = [
            BotResponseOutDto.model_validate(response) for response in bot_responses
        ]
        story_block = self.story_block_service.find_by_id(story_block_id)

        return {"story_block": story_block, "bot_responses": bot_responses}

    @Post("/")
    @validate_token
    def create(
        self,
        request: Request,
        auth_service_stub: AuthServiceStubDepend,
        create_bot_response_dto: CreateBotResponseDto,
    ):
        story_block = None
        bot_responses = False

        if create_bot_response_dto.story_block.id:
            story_block = self.story_block_service.update(
                create_bot_response_dto.story_block
            )

        if len(create_bot_response_dto.bot_responses) > 0:
            bot_responses = self.bot_response_service.create(
                create_bot_response_dto.bot_responses
            )

        return {
            "story_block": {
                "id": story_block.id if story_block else "",
                "name": story_block.name if story_block else "",
            },
            "bot_responses": bot_responses,
        }
