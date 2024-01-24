from fastapi import Depends, Request

from .story_blocks_service import StoryBlocksService
from .dto.get_story_block_out_dto import GetStoryBlockOutDto
from ..decorators.controller import Controller, Get
from ..decorators.validate_token import validate_token
from ..deps.auth_service_stub import AuthServiceStubDepend

@Controller('story-block')
class StoryBlocksController:
    story_block_service: StoryBlocksService = Depends(StoryBlocksService)

    @Get('/', response_model=GetStoryBlockOutDto)
    @validate_token
    def select_by_user_id(self, request: Request, auth_service_stub: AuthServiceStubDepend):
        user_id = request.__dict__['user'].id
        return self.story_block_service.select_by_user_id(user_id)
