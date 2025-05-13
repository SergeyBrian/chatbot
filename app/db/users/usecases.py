from typing import Protocol
from app.model.user import User
from pydantic import BaseModel


class SelectInput(BaseModel):
    user_id: int
    username: str


class Interface(Protocol):
    def create(self, msg: User) -> User:
        ...

    def get(self, req: SelectInput) -> User:
        ...


class Usecases:
    def __init__(self, conn: Interface):
        self.db: Interface = conn

    def create(self, msg: User) -> User:
        return self.db.create(msg)

    def get(self, req: SelectInput) -> User:
        return self.db.get(req=req)
