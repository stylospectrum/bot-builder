from sqlmodel import select, delete
from datetime import datetime

from .enum import BotResponseType
from .schemas.bot_response_schema import BotResponse
from .schemas.bot_response_text_schema import BotResponseText
from .schemas.bot_response_button_schema import BotResponseButton
from .schemas.bot_response_gallery_item_schema import BotResponseGalleryItem
from .schemas.bot_response_button_expr_schema import BotResponseButtonExpr
from .dto.create_bot_response_dto import CreateBotResponseBaseDto
from .dto.bot_response_out_dto import BotResponseOutDto

from ..deps.postgres_session import PostgresSessionDepend
from ..deps.file_service_stub import FileServiceStubDepend
from ..proto.file.file_pb2 import (
    CreateFileRequest,
    GetFileRequest,
    GetFileResponse,
    DeleteFileRequest,
)


class BotResponsesService:
    def __init__(
        self, session: PostgresSessionDepend, file_service_stub: FileServiceStubDepend
    ):
        self.session = session
        self.file_service_stub = file_service_stub

    def find(self, story_block_id: str):
        result = []
        bot_responses: list[BotResponse] = self.session.exec(
            select(BotResponse)
            .where(BotResponse.story_block_id == story_block_id)
            .order_by(BotResponse.updated_at)
        ).all()

        for bot_response in bot_responses:
            bot_response_out = BotResponseOutDto.model_validate(bot_response)

            if bot_response_out.type == BotResponseType.Image:
                file_response: GetFileResponse = self.file_service_stub.GetFile(
                    GetFileRequest(owner_id=str(bot_response.id))
                )

                bot_response_out.image_url = file_response.url

            if bot_response_out.type == BotResponseType.Gallery:
                bot_response_out.gallery = [
                    item.model_dump() for item in bot_response_out.gallery
                ]

                for gallery_item in bot_response_out.gallery:
                    if gallery_item["id"]:
                        file_response: GetFileResponse = self.file_service_stub.GetFile(
                            GetFileRequest(owner_id=str(gallery_item["id"]))
                        )

                        gallery_item["image_url"] = file_response.url

            result.append(bot_response_out)

        return result

    def handle_image_block(self, block, owner_id: str):
        if not block["image_id"]:
            return

        if block["deleted"]:
            self.file_service_stub.DeleteFile(DeleteFileRequest(owner_id=str(owner_id)))
        else:
            self.file_service_stub.CreateFile(
                CreateFileRequest(
                    id=block["image_id"], owner_id=str(owner_id), type="image"
                )
            )

    def handle_gallery_items(self, gallery_raw, bot_response_id):
        existing_gallery_items = {
            item.id: item
            for item in self.session.exec(
                select(BotResponseGalleryItem).where(
                    BotResponseGalleryItem.bot_response_id == bot_response_id
                )
            ).all()
        }

        for gallery_item_raw in gallery_raw:
            gallery_item_id = gallery_item_raw["id"]

            if gallery_item_raw.get("deleted", False):
                if gallery_item_raw["id"] in existing_gallery_items:
                    self.session.delete(existing_gallery_items[gallery_item_raw["id"]])
            elif gallery_item_raw["id"] is None:
                new_gallery_item = BotResponseGalleryItem(
                    bot_response_id=bot_response_id,
                    title=gallery_item_raw["title"],
                    description=gallery_item_raw["description"],
                )
                self.session.add(new_gallery_item)
                self.handle_buttons(
                    gallery_item_raw.get("buttons", []),
                    new_gallery_item.id,
                    "GalleryItem",
                )
                gallery_item_id = new_gallery_item.id
            else:
                if gallery_item_raw["id"] in existing_gallery_items:
                    existing_item = existing_gallery_items[gallery_item_raw["id"]]
                    existing_item.title = gallery_item_raw["title"]
                    existing_item.description = gallery_item_raw["description"]
                    existing_item.updated_at = datetime.utcnow()
                    self.handle_buttons(
                        gallery_item_raw.get("buttons", []),
                        gallery_item_raw["id"],
                        "GalleryItem",
                    )
            self.handle_image_block(gallery_item_raw, gallery_item_id)
        self.session.commit()

    def handle_button_exprs(self, exprs_raw, button_id):
        for expr_raw in exprs_raw:
            if expr_raw["id"] is None:
                expr = BotResponseButtonExpr(
                    button_id=button_id,
                    value=expr_raw["value"],
                    variable_id=expr_raw["variable_id"],
                )
                self.session.add(expr)
            else:
                expr = self.session.exec(
                    select(BotResponseButtonExpr).where(
                        BotResponseButtonExpr.id == expr_raw["id"]
                    )
                ).first()
                if expr_raw["deleted"]:
                    self.session.delete(expr)
                else:
                    expr.value = expr_raw["value"]
                    expr.variable_id = expr_raw["variable_id"]
            self.session.commit()

    def handle_buttons(self, buttons_raw, parent_id: str, parent_type):
        for button_raw in buttons_raw:
            if button_raw["id"] is None:
                button = BotResponseButton(
                    gallery_item_id=parent_id if parent_type == "GalleryItem" else None,
                    bot_response_id=parent_id if parent_type == "QuickReply" else None,
                    content=button_raw["content"],
                    go_to=button_raw["go_to"],
                )
                self.session.add(button)
                self.handle_button_exprs(button_raw.get("exprs", []), button.id)
            else:
                button = self.session.exec(
                    select(BotResponseButton).where(
                        BotResponseButton.id == button_raw["id"]
                    )
                ).first()
                if button_raw["deleted"]:
                    self.session.delete(button)
                else:
                    button.content = button_raw["content"]
                    button.go_to = button_raw["go_to"]
                    button.updated_at = datetime.utcnow()
                    self.handle_button_exprs(button_raw.get("exprs", []), button_raw["id"])
            self.session.commit()

    def handle_text_variants(self, variants_raw, bot_response_id):
        for variant_raw in variants_raw:
            if variant_raw["id"] is None:
                variant = BotResponseText(
                    bot_response_id=bot_response_id, content=variant_raw["content"]
                )
                self.session.add(variant)
            else:
                variant = self.session.exec(
                    select(BotResponseText).where(
                        BotResponseText.id == variant_raw["id"]
                    )
                ).first()
                if variant_raw["deleted"]:
                    self.session.delete(variant)
                else:
                    variant.content = variant_raw["content"]
            self.session.commit()

    def get_or_create_bot_response(self, block):
        if block["id"] is not None:
            bot_response = self.session.exec(
                select(BotResponse).where(BotResponse.id == block["id"])
            ).first()
            if bot_response:
                return bot_response

        bot_response = BotResponse(
            story_block_id=block.get("story_block_id"), type=block["type"]
        )
        self.session.add(bot_response)
        self.session.commit()
        return bot_response

    def finalize_bot_response(self, block, bot_response):
        if block.get("deleted", False):
            self.session.delete(bot_response)
        else:
            bot_response.updated_at = datetime.utcnow()
        self.session.commit()

    def create(self, create_bot_response_dto: list[CreateBotResponseBaseDto]):
        for block in create_bot_response_dto:
            block = block.model_dump()
            bot_response = self.get_or_create_bot_response(block)

            if block["type"] == BotResponseType.Image:
                self.handle_image_block(block, bot_response.id)
            elif block["type"] == BotResponseType.Gallery:
                self.handle_gallery_items(block.get("gallery", []), bot_response.id)
            elif block["type"] == BotResponseType.QuickReply:
                self.handle_text_variants(block.get("variants", []), bot_response.id)
                self.handle_buttons(
                    block["buttons"], bot_response.id, "QuickReply"
                )
            elif block["type"] in [BotResponseType.RandomText, BotResponseType.Text]:
                self.handle_text_variants(block.get("variants", []), bot_response.id)

            self.finalize_bot_response(block, bot_response)
        return True
    
    def delete(self, story_block_id: str):
        self.session.exec(
            delete(BotResponse).where(BotResponse.story_block_id == story_block_id)
        )
        self.session.commit()
        return True
