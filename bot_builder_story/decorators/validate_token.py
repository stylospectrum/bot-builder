from functools import wraps

from fastapi import Request

from ..proto.auth.auth_pb2 import TokenRequest, TokenResponse
from ..deps.auth_service_stub import AuthServiceStubDepend


def validate_token(func):
    @wraps(func)
    async def wrapper(
        request: Request, auth_service_stub: AuthServiceStubDepend, *args, **kwargs
    ):
        authorization = request.headers.get("Authorization")
        token = ""

        if authorization:
            token = authorization.split(" ")[1]

        if token:
            response: TokenResponse = await auth_service_stub.ValidateToken(
                TokenRequest(token=token)
            )
            request.__dict__["user"] = response.payload

        return func(
            *args, request=request, auth_service_stub=auth_service_stub, **kwargs
        )

    return wrapper
