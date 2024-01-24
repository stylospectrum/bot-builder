from sqlmodel import select

from .dto.create_story_block_dto import CreateStoryBlockDto
from .schemas.story_block_schema import StoryBlock
from .enum import StoryBlockType

from ..deps.postgres_session import PostgresSessionDepend
from ..deps.auth_service_stub import AuthServiceStubDepend


class StoryBlocksService:
    def __init__(self, session: PostgresSessionDepend, auth_service_stub: AuthServiceStubDepend):
        self.session = session
        self.auth_service_stub = auth_service_stub

    def select_by_user_id(self, user_id: str):
        statement = select(StoryBlock).where(
            StoryBlock.type == StoryBlockType.StartPoint)
        results = self.session.exec(statement)
        story_block = results.first()

        if not story_block:
            start_point_block = self.create(
                CreateStoryBlockDto(user_id=user_id, type=StoryBlockType.StartPoint))
            start_point_block = start_point_block.model_dump()

            self.create(
                CreateStoryBlockDto(user_id=user_id, name='Welcome message', type=StoryBlockType.BotResponse, parent_id=start_point_block['id']))

            default_fallback_block = self.create(
                CreateStoryBlockDto(user_id=user_id, type=StoryBlockType.DefaultFallback, parent_id=start_point_block['id']))
            default_fallback_block = default_fallback_block.model_dump()

            self.create(
                CreateStoryBlockDto(user_id=user_id, name='Fallback message', type=StoryBlockType.BotResponse, parent_id=default_fallback_block['id']))

            return self.select_by_user_id(user_id)

        return story_block

    def create(self, create_story_block_dto: CreateStoryBlockDto):
        story_block = StoryBlock(**create_story_block_dto.model_dump())
        self.session.add(story_block)
        self.session.commit()
        self.session.refresh(story_block)
        return story_block
