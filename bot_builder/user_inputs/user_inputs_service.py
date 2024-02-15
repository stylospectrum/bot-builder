from sqlmodel import select, delete

from .schemas.user_input_schema import UserInput
from .dto.create_user_input_dto import CreateUserInputDto
from ..deps.postgres_session import PostgresSessionDepend


class UserInputsService:
    def __init__(self, session: PostgresSessionDepend):
        self.session = session

    def find(self, story_block_id: str):
        return self.session.exec(select(UserInput).where(
            UserInput.story_block_id == story_block_id).order_by(UserInput.created_at)).all()

    def create(self, user_inputs_raw: list[CreateUserInputDto]):
        user_inputs = []

        for user_input_raw in user_inputs_raw:
            user_input_raw = user_input_raw.model_dump()

            if user_input_raw['deleted']:
                self.session.exec(delete(UserInput).where(
                    UserInput.id == user_input_raw['id']))
            elif user_input_raw['id']:
                user_input = self.session.exec(select(UserInput).where(
                    UserInput.id == user_input_raw['id'])).first()
                user_input.content = user_input_raw['content']

                user_inputs.append(user_input)
            else:
                user_inputs.append(UserInput(
                    id=user_input_raw['id'], story_block_id=user_input_raw['story_block_id'], content=user_input_raw['content']))
        
        if len(user_inputs) > 0:
            self.session.add_all(user_inputs)

        self.session.commit()
        return True
