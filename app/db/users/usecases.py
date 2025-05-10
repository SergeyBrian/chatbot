from typing import Protocol
from model.user import User


class Usecases(Protocol):
    def create(self, User) -> User:
        ...

    def get(self, SelectInput) -> list(User):
        ...
