from typing import Protocol, Optional, Literal
from app.model.chat import Chat
from pydantic import BaseModel, Field


class SelectInput(BaseModel):
    limit: Optional[int] = 25
    offset: Optional[int] = 0


class UpdateInput(BaseModel):
    id: int
    status: Literal['new', 'in_progress',
                    'closed'] | None = Field(default='new')


class Interface(Protocol):
    def create(self, msg: Chat) -> Chat:
        ...

    def get(self, req: SelectInput) -> list[Chat]:
        ...

    def update(selef, chat: UpdateInput) -> Chat:
        ...


class Usecases:
    def __init__(self, conn: Interface):
        self.db: Interface = conn

    def create(self, msg: Chat) -> Chat:
        return self.db.create(msg)

    def get(self, req: SelectInput) -> list[Chat]:
        return self.db.get(req=req)

    def update(self, chat: UpdateInput) -> Chat:
        return self.db.update(chat=chat)
