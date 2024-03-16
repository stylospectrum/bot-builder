from fastapi import Depends, Request

from .filters_service import FiltersService
from ..story_blocks.story_blocks_service import StoryBlocksService
from ..core.controller import Controller, Get, Post
from ..decorators.validate_token import validate_token
from ..deps.auth_service_stub import AuthServiceStubDepend
from .dto.create_filter_dto import CreateFilterDto


@Controller("filter")
class FiltersController:
    filters_service: FiltersService = Depends(FiltersService)
    story_block_service: StoryBlocksService = Depends(StoryBlocksService)

    @Get("/{story_block_id}/")
    @validate_token
    def find(
        self,
        request: Request,
        auth_service_stub: AuthServiceStubDepend,
        story_block_id: str,
    ):
        story_block = self.story_block_service.find_by_id(story_block_id)
        filter = self.filters_service.find(story_block_id)

        return {"story_block": story_block, "filter": filter}

    @Post("/")
    @validate_token
    def create(
        self,
        request: Request,
        auth_service_stub: AuthServiceStubDepend,
        create_filter_dto: CreateFilterDto,
    ):
        story_block = None

        if create_filter_dto.story_block.id:
            story_block = self.story_block_service.update(create_filter_dto.story_block)

        if create_filter_dto.filter:
            self.filters_service.create(create_filter_dto.filter)

        return {
            "story_block": {
                "id": story_block.id if story_block else "",
                "name": story_block.name if story_block else "",
            },
        }
