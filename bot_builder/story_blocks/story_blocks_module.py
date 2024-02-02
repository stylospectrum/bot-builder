from .story_blocks_service import StoryBlocksService
from .story_blocks_controller import StoryBlocksController

class StoryBlocksModule:
    controllers = [StoryBlocksController]
    services = [StoryBlocksService]