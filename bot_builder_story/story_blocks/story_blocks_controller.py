from fastapi import Depends, Request

from .story_blocks_service import StoryBlocksService
from .dto.story_block_out_dto import StoryBlockOutDto
from .dto.create_story_block_dto import CreateStoryBlockDto
from .dto.delete_story_block_dto import DeleteStoryBlockDto
from .dto.update_story_block_dto import UpdateStoryBlockDto
from ..core.controller import Controller, Get, Post, Delete, Put
from ..decorators.validate_token import validate_token
from ..deps.auth_service_stub import AuthServiceStubDepend
from ..bot_responses.bot_responses_service import BotResponsesService


@Controller("story-block")
class StoryBlocksController:
    story_block_service: StoryBlocksService = Depends(StoryBlocksService)
    bot_response_service: BotResponsesService = Depends(BotResponsesService)

    @Get("/", response_model=StoryBlockOutDto)
    @validate_token
    def find(self, request: Request, auth_service_stub: AuthServiceStubDepend):
        user_id = request.__dict__["user"].id
        return self.story_block_service.find(user_id)
    
    @Get("/user-input-block/")
    @validate_token
    def find_user_input_blocks(self, request: Request, auth_service_stub: AuthServiceStubDepend):
        user_id = request.__dict__["user"].id
        return self.story_block_service.find_user_input_blocks(user_id)

    @Post("/", response_model=StoryBlockOutDto)
    @validate_token
    def create(
        self,
        request: Request,
        auth_service_stub: AuthServiceStubDepend,
        create_story_block_dto: CreateStoryBlockDto,
    ):
        user_id = request.__dict__["user"].id
        create_story_block_dto = create_story_block_dto.model_dump()
        create_story_block_dto["user_id"] = user_id
        return self.story_block_service.create(
            CreateStoryBlockDto(**create_story_block_dto)
        )

    @Put("/", response_model=StoryBlockOutDto)
    @validate_token
    def update(
        self,
        request: Request,
        auth_service_stub: AuthServiceStubDepend,
        update_story_block_dto: UpdateStoryBlockDto,
    ):
        return self.story_block_service.update(update_story_block_dto)

    @Delete("/", response_model=StoryBlockOutDto)
    @validate_token
    def delete(
        self,
        request: Request,
        auth_service_stub: AuthServiceStubDepend,
        delete_story_block_dto: DeleteStoryBlockDto,
    ):
        user_id = request.__dict__["user"].id
        self.bot_response_service.delete(delete_story_block_dto.id)
        return self.story_block_service.delete(delete_story_block_dto, user_id=user_id)
