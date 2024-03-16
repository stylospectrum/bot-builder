from .filter_base_dto import FilterBaseDto
from ...story_blocks.dto.update_story_block_dto import UpdateStoryBlockDto


class CreateBaseFilterDto(FilterBaseDto):
    pass


class CreateFilterDto(FilterBaseDto):
    filter: CreateBaseFilterDto
    story_block: UpdateStoryBlockDto
