from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetStoryBlocksRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class StoryBlock(_message.Message):
    __slots__ = ("id", "name", "type", "user_id", "parent_id", "children")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    type: str
    user_id: str
    parent_id: str
    children: _containers.RepeatedCompositeFieldContainer[StoryBlock]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., user_id: _Optional[str] = ..., parent_id: _Optional[str] = ..., children: _Optional[_Iterable[_Union[StoryBlock, _Mapping]]] = ...) -> None: ...

class GetBotResponsesRequest(_message.Message):
    __slots__ = ("story_block_id",)
    STORY_BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    story_block_id: str
    def __init__(self, story_block_id: _Optional[str] = ...) -> None: ...

class GetBotResponsesResponse(_message.Message):
    __slots__ = ("responses",)
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    responses: _containers.RepeatedCompositeFieldContainer[BotResponse]
    def __init__(self, responses: _Optional[_Iterable[_Union[BotResponse, _Mapping]]] = ...) -> None: ...

class BotResponse(_message.Message):
    __slots__ = ("type", "variants")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VARIANTS_FIELD_NUMBER: _ClassVar[int]
    type: str
    variants: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, type: _Optional[str] = ..., variants: _Optional[_Iterable[str]] = ...) -> None: ...
