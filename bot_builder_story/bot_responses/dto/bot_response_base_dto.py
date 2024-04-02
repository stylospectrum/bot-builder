import uuid

from sqlmodel import SQLModel
from typing import Optional

from ..enum import BotResponseType

class BotResponseButtonExprDto(SQLModel):
    id: Optional[uuid.UUID] = None
    deleted: Optional[bool] = False
    variable_id: Optional[str] = None
    value: Optional[str] = None

class BotResponseButtonDto(SQLModel):
    id: Optional[uuid.UUID] = None
    content: Optional[str] = None
    go_to: Optional[str] = None
    deleted: Optional[bool] = False
    exprs: Optional[list[BotResponseButtonExprDto]] = []


class BotResponseTextDto(SQLModel):
    id: Optional[uuid.UUID] = None
    content: Optional[str] = None
    deleted: Optional[bool] = False


class BotResponseGalleryItemDto(SQLModel):
    id: Optional[uuid.UUID] = None
    image_id: Optional[str] = None
    image_url: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    buttons: Optional[list[BotResponseButtonDto]] = []
    deleted: Optional[bool] = False


class BotResponseBaseDto(SQLModel):
    id: Optional[uuid.UUID] = None
    story_block_id: Optional[uuid.UUID] = None
    type: Optional[BotResponseType]
    variants: Optional[list[BotResponseTextDto]] = []
    buttons: Optional[list[BotResponseButtonDto]] = []
    gallery: Optional[list[BotResponseGalleryItemDto]] = []
