from typing import Protocol, Optional
from app.model.question import Question
from pydantic import BaseModel


class SelectInput(BaseModel):
    limit: Optional[int] = 25
    offset: Optional[int] = 0
    category_id: int = 0
    search: Optional[str] = ""


class Interface(Protocol):
    def create(self, msg: Question) -> Question:
        ...

    def get(self, req: SelectInput) -> list[Question]:
        ...


class Usecases:
    def __init__(self, conn: Interface):
        self.db: Interface = conn

    def create(self, msg: Question) -> Question:
        return self.db.create(msg)

    def get(self, req: SelectInput) -> list[Question]:
        return self.db.get(req=req)
