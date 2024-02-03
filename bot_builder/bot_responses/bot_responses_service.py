import uuid

from sqlmodel import select
from datetime import datetime

from .enum import BotResponseType
from .schemas.bot_response_schema import BotResponse
from .schemas.bot_response_text_schema import BotResponseText
from .schemas.bot_response_button_schema import BotResponseButton
from .dto.create_bot_response_dto import CreateBotResponseDto

from ..deps.postgres_session import PostgresSessionDepend
from ..deps.auth_service_stub import AuthServiceStubDepend


class BotResponsesService:
    def __init__(self, session: PostgresSessionDepend, auth_service_stub: AuthServiceStubDepend):
        self.session = session
        self.auth_service_stub = auth_service_stub

    def find(self, story_block_id: str):
        return self.session.exec(select(BotResponse).where(
            BotResponse.story_block_id == story_block_id).order_by(BotResponse.updated_at)).all()

    def create(self, create_bot_response_dto: list[CreateBotResponseDto]):
        for block in create_bot_response_dto:
            block = block.model_dump()

            if block['id'] is None:
                bot_response = BotResponse(
                    story_block_id=block['story_block_id'], type=block['type'])
                self.session.add(bot_response)
                self.session.commit()
                
            if block['type'] == BotResponseType.QuickReply:
                if block['id'] is None:
                    for button in block['buttons']:
                        bot_response_button = BotResponseButton(
                            bot_response_id=bot_response.id, content=button['content'], go_to=button['go_to'])
                        self.session.add(bot_response_button)
                        self.session.commit()
                else:
                    buttons = self.session.exec(select(BotResponseButton).where(
                        BotResponseButton.bot_response_id == block['id'])).all()
                    if block['deleted']:
                        for button in buttons:
                            self.session.delete(button)
                            self.session.commit()
                    else:
                        for raw_button in block['buttons']:
                            if raw_button['id'] is None:
                                button = BotResponseButton(
                                    bot_response_id=block['id'], content=raw_button['content'], go_to=raw_button['go_to'])
                                self.session.add(button)
                                self.session.commit()
                            else:
                                button = self.session.exec(select(BotResponseButton).where(
                                    BotResponseButton.id == raw_button['id'])).first()
                                if raw_button['deleted']:
                                    self.session.delete(button)
                                    self.session.commit()
                                else:
                                    button.updated_at = datetime.utcnow()
                                    button.content = raw_button['content']
                                    button.go_to = raw_button['go_to']
                                    self.session.add(button)
                                    self.session.commit()

            if block['type'] == BotResponseType.RandomText or block['type'] == BotResponseType.Text or block['type'] == BotResponseType.QuickReply:
                if block['id'] is None:
                    for variant in block['variants']:
                        bot_response_text = BotResponseText(
                            bot_response_id=bot_response.id, content=variant['content'])
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
                        for raw_variant in block['variants']:
                            if raw_variant['id'] is None:
                                variant = BotResponseText(
                                    bot_response_id=block['id'], content=raw_variant['content'])
                                self.session.add(variant)
                                self.session.commit()
                            else:
                                variant = self.session.exec(select(BotResponseText).where(
                                    BotResponseText.id == raw_variant['id'])).first()
                                if raw_variant['deleted']:
                                    self.session.delete(variant)
                                    self.session.commit()
                                else:
                                    variant.content = raw_variant['content']
                                    self.session.add(variant)
                                    self.session.commit()

            if block['id'] is not None:
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
