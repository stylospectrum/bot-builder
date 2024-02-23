from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserInput(_message.Message):
    __slots__ = ("id", "content", "story_block_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    STORY_BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    content: str
    story_block_id: str
    def __init__(self, id: _Optional[str] = ..., content: _Optional[str] = ..., story_block_id: _Optional[str] = ...) -> None: ...

class UpsertEmbeddingRequest(_message.Message):
    __slots__ = ("user_id", "user_inputs")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_INPUTS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    user_inputs: _containers.RepeatedCompositeFieldContainer[UserInput]
    def __init__(self, user_id: _Optional[str] = ..., user_inputs: _Optional[_Iterable[_Union[UserInput, _Mapping]]] = ...) -> None: ...

class UpsertEmbeddingResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class DeleteEmbeddingRequest(_message.Message):
    __slots__ = ("ids",)
    IDS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ids: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteEmbeddingResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class GetStoryBlockIdRequest(_message.Message):
    __slots__ = ("user_id", "user_input")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_INPUT_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    user_input: str
    def __init__(self, user_id: _Optional[str] = ..., user_input: _Optional[str] = ...) -> None: ...

class GetStoryBlockIdResponse(_message.Message):
    __slots__ = ("story_block_id",)
    STORY_BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    story_block_id: str
    def __init__(self, story_block_id: _Optional[str] = ...) -> None: ...
