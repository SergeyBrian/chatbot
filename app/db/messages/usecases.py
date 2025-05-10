from typing import Protocol, Optional
from app.model.message import Message
from pydantic import BaseModel


class SelectInput(BaseModel):
    limit: Optional[int] = 25
    offset: Optional[int] = 0
    chat_id: int


class UpdateInput(BaseModel):
    id: int = 0
    useful: bool | None = None


class Interface(Protocol):
    def create(self, msg: Message) -> Message:
        ...

    def get(self, req: SelectInput) -> list[Message]:
        ...

    def update(self, req: UpdateInput) -> Message:
        ...


class Usecases:
    def __init__(self, conn: Interface):
        self.db: Interface = conn

    def create(self, msg: Message) -> Message:
        return self.db.create(msg)

    def get(self, req: SelectInput) -> list[Message]:
        return self.db.get(req=req)

    def update(self, req: UpdateInput) -> Message:
        return self.db.get(req=req)
