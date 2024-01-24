
import grpc

from typing import Annotated
from fastapi import Depends

from ..proto.auth_pb2_grpc import AuthServiceStub
from ..config.settings import settings


async def get_stub():
    async with grpc.aio.insecure_channel(settings.AUTH_SERVICE_URL) as channel:
        stub = AuthServiceStub(channel=channel)
        yield stub


AuthServiceStubDepend = Annotated[AuthServiceStub, Depends(get_stub)]
