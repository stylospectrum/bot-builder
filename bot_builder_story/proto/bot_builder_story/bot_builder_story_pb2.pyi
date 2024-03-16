from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Iterable as _Iterable,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

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
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        type: _Optional[str] = ...,
        user_id: _Optional[str] = ...,
        parent_id: _Optional[str] = ...,
        children: _Optional[_Iterable[_Union[StoryBlock, _Mapping]]] = ...,
    ) -> None: ...

class GetBotResponsesRequest(_message.Message):
    __slots__ = ("story_block_id",)
    STORY_BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    story_block_id: str
    def __init__(self, story_block_id: _Optional[str] = ...) -> None: ...

class GetBotResponsesResponse(_message.Message):
    __slots__ = ("responses",)
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    responses: _containers.RepeatedCompositeFieldContainer[BotResponse]
    def __init__(
        self, responses: _Optional[_Iterable[_Union[BotResponse, _Mapping]]] = ...
    ) -> None: ...

class BotResponseButton(_message.Message):
    __slots__ = ("content", "go_to")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    GO_TO_FIELD_NUMBER: _ClassVar[int]
    content: str
    go_to: str
    def __init__(
        self, content: _Optional[str] = ..., go_to: _Optional[str] = ...
    ) -> None: ...

class BotResponseGalleryItem(_message.Message):
    __slots__ = ("img_url", "title", "description", "buttons")
    IMG_URL_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BUTTONS_FIELD_NUMBER: _ClassVar[int]
    img_url: str
    title: str
    description: str
    buttons: _containers.RepeatedCompositeFieldContainer[BotResponseButton]
    def __init__(
        self,
        img_url: _Optional[str] = ...,
        title: _Optional[str] = ...,
        description: _Optional[str] = ...,
        buttons: _Optional[_Iterable[_Union[BotResponseButton, _Mapping]]] = ...,
    ) -> None: ...

class BotResponse(_message.Message):
    __slots__ = ("type", "variants", "img_url", "buttons", "gallery")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VARIANTS_FIELD_NUMBER: _ClassVar[int]
    IMG_URL_FIELD_NUMBER: _ClassVar[int]
    BUTTONS_FIELD_NUMBER: _ClassVar[int]
    GALLERY_FIELD_NUMBER: _ClassVar[int]
    type: str
    variants: _containers.RepeatedScalarFieldContainer[str]
    img_url: str
    buttons: _containers.RepeatedCompositeFieldContainer[BotResponseButton]
    gallery: _containers.RepeatedCompositeFieldContainer[BotResponseGalleryItem]
    def __init__(
        self,
        type: _Optional[str] = ...,
        variants: _Optional[_Iterable[str]] = ...,
        img_url: _Optional[str] = ...,
        buttons: _Optional[_Iterable[_Union[BotResponseButton, _Mapping]]] = ...,
        gallery: _Optional[_Iterable[_Union[BotResponseGalleryItem, _Mapping]]] = ...,
    ) -> None: ...
