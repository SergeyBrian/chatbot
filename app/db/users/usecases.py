from typing import Protocol, Optional
from model.user import User
from pydantic import BaseModel


class SelectInput(BaseModel):
    limit: Optional[int] = 25
    offset: Optional[int] = 0


class Interface(Protocol):
    def create(self, User) -> User:
        ...

    def get(self, SelectInput) -> list(User):
        ...
