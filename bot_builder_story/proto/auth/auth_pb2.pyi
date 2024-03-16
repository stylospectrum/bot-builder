from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor

class JwtPayload(_message.Message):
    __slots__ = ("id", "email", "role")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    id: str
    email: str
    role: str
    def __init__(
        self,
        id: _Optional[str] = ...,
        email: _Optional[str] = ...,
        role: _Optional[str] = ...,
    ) -> None: ...

class TokenRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class TokenResponse(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: JwtPayload
    def __init__(
        self, payload: _Optional[_Union[JwtPayload, _Mapping]] = ...
    ) -> None: ...
