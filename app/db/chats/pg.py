from app.db.chats.usecases import Interface, SelectInput
from app.db.connector import get_cursor
from app.model.chat import Chat


class Repo(Interface):
    def __init__(self):
        self.cur = get_cursor

    def create(self, msg: Chat) -> Chat:
        ...

    def get(self, req: SelectInput) -> list[Chat]:
        ...
