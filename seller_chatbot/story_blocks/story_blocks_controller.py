from fastapi import Depends, Request

from .story_blocks_service import StoryBlocksService
from .dto.story_block_out_dto import StoryBlockOutDto
from .dto.create_story_block_dto import CreateStoryBlockDto
from ..decorators.controller import Controller, Get, Post
from ..decorators.validate_token import validate_token
from ..deps.auth_service_stub import AuthServiceStubDepend


@Controller('story-block')
class StoryBlocksController:
    story_block_service: StoryBlocksService = Depends(StoryBlocksService)

    @Get('/', response_model=StoryBlockOutDto)
    @validate_token
    def select_by_user_id(self, request: Request, auth_service_stub: AuthServiceStubDepend):
        user_id = request.__dict__['user'].id
        return self.story_block_service.select_by_user_id(user_id)

    @Post('/', response_model=StoryBlockOutDto)
    @validate_token
    def create(self, request: Request, auth_service_stub: AuthServiceStubDepend, create_story_block_dto: CreateStoryBlockDto):
        user_id = request.__dict__['user'].id
        create_story_block_dto = create_story_block_dto.model_dump()
        create_story_block_dto['user_id'] = user_id
        return self.story_block_service.create(CreateStoryBlockDto(**create_story_block_dto))
