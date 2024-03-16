from .story_block_base_dto import StoryBlockBaseDto


class StoryBlockOutDto(StoryBlockBaseDto):
    children: list["StoryBlockOutDto"] = None
