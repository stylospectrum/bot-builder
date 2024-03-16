from sqlmodel import SQLModel

from .user_input_base_dto import UserInputBaseDto
from ...story_blocks.dto.update_story_block_dto import UpdateStoryBlockDto


class CreateUserInputBaseDto(UserInputBaseDto):
    pass


class CreateUserInputDto(SQLModel):
    user_inputs: list[CreateUserInputBaseDto]
    story_block: UpdateStoryBlockDto
