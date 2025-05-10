from typing import Protocol, Optional
from app.model.chat import Chat
from pydantic import BaseModel


class SelectInput(BaseModel):
    limit: Optional[int] = 25
    offset: Optional[int] = 0


class Interface(Protocol):
    def create(self, msg: Chat) -> Chat:
        ...

    def get(self, req: SelectInput) -> list[Chat]:
        ...


class Usecases:
    def __init__(self, conn: Interface):
        self.db: Interface = conn

    def create(self, msg: Chat) -> Chat:
        return self.db.create(msg)

    def get(self, req: SelectInput) -> list[Chat]:
        return self.db.get(req=req)
