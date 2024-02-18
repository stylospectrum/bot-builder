import grpc
import logging

from concurrent import futures

from .service import BotBuilderServicer
from ..proto.bot_builder import bot_builder_pb2_grpc
from ..config.settings import settings


def serve_grpc():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    bot_builder_pb2_grpc.add_BotBuilderServiceServicer_to_server(
        BotBuilderServicer(), server)
    server.add_insecure_port(f"[::]:{settings.SERVICE_URL}")
    server.start()

    logging.basicConfig(level=logging.INFO)
    logging.info("gRPC server running...")
    
    return server
