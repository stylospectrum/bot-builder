from sqlmodel import select, delete

from .dto.create_story_block_dto import CreateStoryBlockDto
from .dto.update_story_block_dto import UpdateStoryBlockDto
from .dto.delete_story_block_dto import DeleteStoryBlockDto
from .dto.story_block_out_dto import StoryBlockOutDto
from .schemas.story_block_schema import StoryBlock
from .enum import StoryBlockType

from ..deps.postgres_session import PostgresSessionDepend


class StoryBlocksService:
    def __init__(self, session: PostgresSessionDepend):
        self.session = session

    def create_base(self, create_story_block_dto: CreateStoryBlockDto):
        story_block = StoryBlock(**create_story_block_dto.model_dump())
        self.session.add(story_block)
        self.session.commit()
        self.session.refresh(story_block)
        return story_block

    def nodes_from_tree(self, parent: StoryBlock):
        r = [parent.id]
        for child in parent.children:
            r.extend(self.nodes_from_tree(child))
        return r
    
    def find_by_id(self, id: str):
        return self.session.exec(select(StoryBlock).where(StoryBlock.id == id)).first()

    def find(self, user_id: str):
        story_block = self.session.exec(select(StoryBlock).where(
            StoryBlock.type == StoryBlockType.StartPoint)).first()

        if not story_block:
            start_point_block = self.create_base(
                CreateStoryBlockDto(user_id=user_id, type=StoryBlockType.StartPoint))
            start_point_block = start_point_block.model_dump()

            self.create_base(
                CreateStoryBlockDto(user_id=user_id, name='Welcome message', type=StoryBlockType.BotResponse, parent_id=start_point_block['id']))

            default_fallback_block = self.create_base(
                CreateStoryBlockDto(user_id=user_id, type=StoryBlockType.DefaultFallback, parent_id=start_point_block['id']))
            default_fallback_block = default_fallback_block.model_dump()

            self.create_base(
                CreateStoryBlockDto(user_id=user_id, name='Fallback message', type=StoryBlockType.BotResponse, parent_id=default_fallback_block['id']))

            return self.find(user_id)

        return story_block

    def update(self, update_story_block_dto: UpdateStoryBlockDto):
        story_block = self.session.exec(
            select(StoryBlock).where(StoryBlock.id == update_story_block_dto.id)).first()
        story_block.name = update_story_block_dto.name
        self.session.add(story_block)
        self.session.commit()
        self.session.refresh(story_block)
        return story_block

    def create(self, create_story_block_dto: CreateStoryBlockDto):
        params = create_story_block_dto.model_dump()
        subsequent_blocks = self.session.exec(
            select(StoryBlock).where(
                StoryBlock.parent_id == params['parent_id'])
        ).all()
        new_block = self.create_base(CreateStoryBlockDto(**params))

        if len(subsequent_blocks) > 0 and (subsequent_blocks[0].type == StoryBlockType.BotResponse or params['type'] == StoryBlockType.BotResponse):
            for block in subsequent_blocks:
                block.parent_id = new_block.id
                self.session.add(block)
                self.session.commit()

        return self.find(params['user_id'])

    def delete(self, delete_story_block_dto: DeleteStoryBlockDto, user_id: str):
        id, is_delete_many = delete_story_block_dto.model_dump().values()
        story_block = self.session.exec(
            select(StoryBlock).where(StoryBlock.id == id)).first()

        if is_delete_many:
            list_id = self.nodes_from_tree(
                StoryBlockOutDto.model_validate(story_block))
            list_id.pop(0)

            self.session.exec(delete(StoryBlock).where(StoryBlock.id.in_(list_id)))
            self.session.commit()
        else:
            for sub_story_block in story_block.children:
                sub_story_block.parent_id = story_block.parent_id
                self.session.add(sub_story_block)
                self.session.commit()

        self.session.delete(story_block)
        self.session.commit()

        return self.find(user_id=user_id)
