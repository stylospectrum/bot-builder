import uuid

from fastapi import HTTPException
from sqlmodel import select, and_
from datetime import datetime

from .enum import BotResponseType
from .schemas.bot_response_schema import BotResponse
from .schemas.bot_response_text_schema import BotResponseText
from .dto.create_bot_response_dto import CreateBotResponseDto

from ..deps.postgres_session import PostgresSessionDepend
from ..deps.auth_service_stub import AuthServiceStubDepend


class BotResponsesService:
    def __init__(self, session: PostgresSessionDepend, auth_service_stub: AuthServiceStubDepend):
        self.session = session
        self.auth_service_stub = auth_service_stub

    def find(self, story_block_id: str):
        responses = self.session.exec(select(BotResponse, BotResponseText).where(
            and_(BotResponseText.bot_response_id == BotResponse.id, BotResponse.story_block_id == story_block_id)).order_by(BotResponse.updated_at)).all()

        if len(responses) == 0:
            return []

        output = []

        for response in responses:
            bot_response, bot_response_text = response

            output.append({
                **bot_response.model_dump(),
                'text': bot_response_text
            })

        return output

    def create(self, create_bot_response_dto: list[CreateBotResponseDto]):
        for block in create_bot_response_dto:
            block = block.model_dump()
            bot_response_id = uuid.uuid4()

            if block['type'] == BotResponseType.Text:
                if block['id'] is None:
                    bot_response_text = BotResponseText(
                        bot_response_id=bot_response_id, content=block['text']['content'])
                    self.session.add(bot_response_text)
                    self.session.commit()
                else:
                    bot_response_text = self.session.exec(select(BotResponseText).where(
                        BotResponseText.bot_response_id == block['id'])).first()
                    if block['deleted']:
                        self.session.delete(bot_response_text)
                        self.session.commit()
                    else:
                        bot_response_text.content = block['text']['content']
                        self.session.add(bot_response_text)
                        self.session.commit()

            if block['type'] == BotResponseType.RandomText:
                if block['id'] is None:
                    for variant in block['variants']:
                        bot_response_text = BotResponseText(
                            bot_response_id=bot_response_id, content=variant['content'])
                        self.session.add(bot_response_text)
                        self.session.commit()
                else:
                    variants = self.session.exec(select(BotResponseText).where(
                        BotResponseText.bot_response_id == block['id'])).all()
                    if block['deleted']:
                        for variant in variants:
                            self.session.delete(variant)
                            self.session.commit()
                    else:
                        bot_response_text.content = block['variants'][0]['content']
                        self.session.add(bot_response_text)
                        self.session.commit()

            if block['id'] is None:
                bot_response = BotResponse(
                    story_block_id=block['story_block_id'], type=block['type'], id=bot_response_id)
                self.session.add(bot_response)
                self.session.commit()
            else:
                bot_response = self.session.exec(select(BotResponse).where(
                    BotResponse.id == block['id'])).first()

                if block['deleted']:
                    self.session.delete(bot_response)
                    self.session.commit()

                else:
                    bot_response.updated_at = datetime.utcnow()
                    self.session.add(bot_response)
                    self.session.commit()
        return True
