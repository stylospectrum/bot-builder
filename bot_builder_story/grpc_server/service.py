import json
import grpc

from sqlmodel import Session, select, and_

from ..postgres.engine import engine
from ..proto.file.file_pb2_grpc import FileServiceStub
from ..proto.file.file_pb2 import GetFileRequest, GetFileResponse
from ..proto.bot_builder_story import bot_builder_story_pb2_grpc, bot_builder_story_pb2
from ..story_blocks.enum import StoryBlockType
from ..story_blocks.schemas.story_block_schema import StoryBlock
from ..story_blocks.dto.story_block_out_dto import StoryBlockOutDto
from ..bot_responses.schemas.bot_response_schema import BotResponse
from ..bot_responses.dto.bot_response_out_dto import BotResponseOutDto
from ..bot_responses.enum import BotResponseType
from ..config.settings import settings


class BotBuilderStoryServicer(bot_builder_story_pb2_grpc.BotBuilderStoryServiceServicer):
    def __init__(self):
        channel = grpc.insecure_channel(settings.FILE_SERVICE_URL)
        self.file_service_stub = FileServiceStub(channel=channel)

    def GetStoryBlocks(self, request, context):
        with Session(engine) as session:
            story_block = session.exec(select(StoryBlock).where(
                and_(StoryBlock.type == StoryBlockType.StartPoint, StoryBlock.user_id == request.user_id))).first()
            sb_json = json.loads(StoryBlockOutDto.model_validate(
                story_block).model_dump_json())
            return bot_builder_story_pb2.StoryBlock(**sb_json)

    def GetBotResponses(self, request, context):
        with Session(engine) as session:
            bot_responses = session.exec(select(BotResponse).where(
                BotResponse.story_block_id == request.story_block_id)).all()
            result = []

            for bot_response in bot_responses:
                bot_response_out = BotResponseOutDto.model_validate(
                    bot_response)

                if bot_response_out.type == BotResponseType.Image:
                    file_response: GetFileResponse = self.file_service_stub.GetFile(
                        GetFileRequest(owner_id=str(bot_response.id)))

                    bot_response_out.image_url = file_response.url

                if bot_response_out.type == BotResponseType.Gallery:
                    bot_response_out.gallery = [
                        item.model_dump() for item in bot_response_out.gallery]

                    for gallery_item in bot_response_out.gallery:
                        file_response: GetFileResponse = self.file_service_stub.GetFile(
                            GetFileRequest(owner_id=str(gallery_item['id'])))

                        gallery_item['image_url'] = file_response.url

                gallery = []

                for gallery_item in bot_response_out.gallery:
                    buttons = []

                    for button in gallery_item['buttons']:
                        buttons.append({
                            'content': button['content'],
                            'go_to': button['go_to']
                        })
                    
                    gallery.append({
                        'title': gallery_item['title'],
                        'description': gallery_item['description'],
                        'img_url': gallery_item['image_url'],
                        'buttons': buttons
                    })

                result.append({
                    'type': bot_response_out.type,
                    'variants': [v.content for v in bot_response_out.variants],
                    'img_url': bot_response_out.image_url,
                    'gallery': gallery,
                    'buttons': [{'content': button.content, 'go_to': button.go_to} for button in bot_response_out.buttons],
                })

            return bot_builder_story_pb2.GetBotResponsesResponse(responses=result)
