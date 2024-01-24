from .story_block_base_dto import StoryBlockBaseDto


class GetStoryBlockOutDto(StoryBlockBaseDto):
    children: list['GetStoryBlockOutDto'] = None
