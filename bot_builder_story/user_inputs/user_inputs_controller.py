from fastapi import Depends, Request

from .user_inputs_service import UserInputsService
from ..story_blocks.story_blocks_service import StoryBlocksService
from .dto.create_user_input_dto import CreateUserInputDto
from ..core.controller import Controller, Get, Post
from ..decorators.validate_token import validate_token
from ..deps.auth_service_stub import AuthServiceStubDepend


@Controller('user-input')
class UserInputsController:
    user_input_service: UserInputsService = Depends(UserInputsService)
    story_block_service: StoryBlocksService = Depends(StoryBlocksService)

    @Get('/{story_block_id}/')
    @validate_token
    def find(self, request: Request, auth_service_stub: AuthServiceStubDepend, story_block_id: str):
        story_block = self.story_block_service.find_by_id(story_block_id)
        user_inputs = self.user_input_service.find(story_block_id)

        return {
            "story_block": story_block,
            "user_inputs": user_inputs
        }

    @Post('/')
    @validate_token
    def create(self, request: Request, auth_service_stub: AuthServiceStubDepend, create_user_input_dto: CreateUserInputDto):
        user_id = request.__dict__['user'].id
        story_block = None
        user_inputs = False

        if create_user_input_dto.story_block.id:
            story_block = self.story_block_service.update(create_user_input_dto.story_block)

        if len(create_user_input_dto.user_inputs) > 0:
            user_inputs = self.user_input_service.create(create_user_input_dto.user_inputs, user_id)
    
        return {
            "story_block": {
                'id': story_block.id if story_block else '',
                'name': story_block.name if story_block else '',
            },
            "user_inputs": user_inputs
        }
