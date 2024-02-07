from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileRequest(_message.Message):
    __slots__ = ("id", "type", "owner_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: str
    owner_id: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ..., owner_id: _Optional[str] = ...) -> None: ...

class CreateFileResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class GetFileRequest(_message.Message):
    __slots__ = ("owner_id",)
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    owner_id: str
    def __init__(self, owner_id: _Optional[str] = ...) -> None: ...

class GetFileResponse(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class DeleteFileRequest(_message.Message):
    __slots__ = ("owner_id",)
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    owner_id: str
    def __init__(self, owner_id: _Optional[str] = ...) -> None: ...

class DeleteFileResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
