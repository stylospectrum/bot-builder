from sqlmodel import select, delete, and_

from ..deps.postgres_session import PostgresSessionDepend
from .schemas.filter_schema import Filter
from .dto.create_filter_dto import CreateBaseFilterDto
from .dto.filter_out_dto import FilterOutDto


class FiltersService:
    def __init__(self, session: PostgresSessionDepend):
        self.session = session

    def find(self, story_block_id: str):
        filter = self.session.exec(
            select(Filter).where(and_(Filter.story_block_id == story_block_id, Filter.parent_id == None))
        ).first()

        if not filter:
            return None

        return FilterOutDto.model_validate(filter)

    def create_base(self, create_filter_dto: CreateBaseFilterDto):
        create_filter_dto = create_filter_dto.model_dump()
        filter = Filter(
            attribute=create_filter_dto["attribute"],
            operator=create_filter_dto["operator"],
            value=create_filter_dto["value"],
            story_block_id=create_filter_dto["story_block_id"],
            parent_id=create_filter_dto["parent_id"],
        )
        self.session.add(filter)
        self.session.commit()
        self.session.refresh(filter)

        parent_id = filter.id

        if create_filter_dto["sub_exprs"]:
            for sub_expr in create_filter_dto["sub_exprs"]:
                sub_expr["parent_id"] = parent_id
                sub_expr["story_block_id"] = create_filter_dto["story_block_id"]
                self.create_base(CreateBaseFilterDto(**sub_expr))

        return True

    def create(self, create_filter_dto: CreateBaseFilterDto):
        self.session.exec(
            delete(Filter).where(Filter.story_block_id == create_filter_dto.story_block_id)
        )
        self.session.commit()
        self.create_base(create_filter_dto)
        return True