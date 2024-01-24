import json

from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


class ResponseInterceptor(BaseHTTPMiddleware):
    def __init__(
            self,
            app,
    ):
        super().__init__(app)

    status_messages = {
        200: 'OK',
        201: 'Created',
        202: 'Accepted',
        203: 'NonAuthoritativeInfo',
        204: 'NoContent',
        205: 'ResetContent',
        206: 'PartialContent',
    }

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        status_code = response.status_code
        message = self.status_messages.get(status_code, 'Unknown Status Code')
        response_body = b""

        async for chunk in response.body_iterator:
            response_body += chunk

        custom_response = {
            "statusCode": status_code,
            "message": message,
            "data": json.loads(response_body.decode()),
        }

        return JSONResponse(content=custom_response)
