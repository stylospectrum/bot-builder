
import grpc

from typing import Annotated
from fastapi import Depends

from ..proto.file.file_pb2_grpc import FileServiceStub
from ..config.settings import settings


def get_stub():
    with grpc.insecure_channel(settings.FILE_SERVICE_URL) as channel:
        stub = FileServiceStub(channel=channel)
        yield stub


FileServiceStubDepend = Annotated[FileServiceStub, Depends(get_stub)]
