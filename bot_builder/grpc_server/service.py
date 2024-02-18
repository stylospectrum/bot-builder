import json

from sqlmodel import Session, select, and_

from ..postgres.engine import engine
from ..proto.bot_builder import bot_builder_pb2_grpc, bot_builder_pb2
from ..story_blocks.enum import StoryBlockType
from ..story_blocks.schemas.story_block_schema import StoryBlock
from ..story_blocks.dto.story_block_out_dto import StoryBlockOutDto
from ..bot_responses.schemas.bot_response_schema import BotResponse
from ..bot_responses.dto.bot_response_out_dto import BotResponseOutDto


class BotBuilderServicer(bot_builder_pb2_grpc.BotBuilderServiceServicer):
    def GetStoryBlocks(self, request, context):
        with Session(engine) as session:
            story_block = session.exec(select(StoryBlock).where(
                and_(StoryBlock.type == StoryBlockType.StartPoint, StoryBlock.user_id == request.user_id))).first()
            sb_json = json.loads(StoryBlockOutDto.model_validate(
                story_block).model_dump_json())
            return bot_builder_pb2.StoryBlock(**sb_json)

    def GetBotResponses(self, request, context):
        with Session(engine) as session:
            bot_responses = session.exec(select(BotResponse).where(
                BotResponse.story_block_id == request.story_block_id)).all()
            result = []

            for response in bot_responses:
                r = BotResponseOutDto.model_validate(response)
                result.append({
                    'type': r.type,
                    'variants': [v.content for v in r.variants]
                })
            print(result)
            return bot_builder_pb2.GetBotResponsesResponse(responses=result)
