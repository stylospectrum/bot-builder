
import grpc

from typing import Annotated
from fastapi import Depends

from ..proto.bot_builder_nlp.bot_builder_nlp_pb2_grpc import BotBuilderNlpServiceStub
from ..config.settings import settings


def get_stub():
    with grpc.insecure_channel(settings.BOT_BUILDER_NLP_SERVICE_URL) as channel:
        stub = BotBuilderNlpServiceStub(channel=channel)
        yield stub


BotBuilderNlpServiceStubDepend = Annotated[BotBuilderNlpServiceStub, Depends(
    get_stub)]
