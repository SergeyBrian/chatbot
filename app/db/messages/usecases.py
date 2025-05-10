from typing import Protocol, Optional
from app.model.message import Message
from pydantic import BaseModel


class SelectInput(BaseModel):
    limit: Optional[int] = 25
    offset: Optional[int] = 0
    chat_id: int


class Interface(Protocol):
    def create(self, msg: Message) -> Message:
        ...

    def get(self, req: SelectInput) -> list[Message]:
        ...


class Usecases:
    def __init__(self, conn: Interface):
        self.db: Interface = conn

    def create(self, msg: Message) -> Message:
        return {"res": self.db.create(msg)}

    def get(self, req: SelectInput) -> list[Message]:
        messages = self.db.get(req=SelectInput(chat_id=id))
        return {"res": messages}
