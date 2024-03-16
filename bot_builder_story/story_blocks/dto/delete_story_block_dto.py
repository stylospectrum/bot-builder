from sqlmodel import SQLModel


class DeleteStoryBlockDto(SQLModel):
    id: str
    is_delete_many: bool
