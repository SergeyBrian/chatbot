from typing import Protocol, Optional
from app.model.category import Category
from pydantic import BaseModel


class SelectInput(BaseModel):
    limit: Optional[int] = 25
    offset: Optional[int] = 0
    search: Optional[str] = ""


class Interface(Protocol):
    def create(self, msg: Category) -> Category:
        ...

    def get(self, req: SelectInput) -> list[Category]:
        ...


class Usecases:
    def __init__(self, conn: Interface):
        self.db: Interface = conn

    def create(self, msg: Category) -> Category:
        return self.db.create(msg)

    def get(self, req: SelectInput) -> list[Category]:
        return self.db.get(req=req)
