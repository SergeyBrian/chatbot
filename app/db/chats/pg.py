from app.db.chats.usecases import Interface, SelectInput, UpdateInput
from app.db.connector import get_cursor
from app.model.chat import Chat


class Repo(Interface):
    def __init__(self):
        self.cur = get_cursor

    def create(self, msg: Chat) -> Chat:
        ...

    def get(self, req: SelectInput) -> list[Chat]:
        ...

    # TODO здесь нужно будет если статус closed,
    # то также обновлять closed_at = текущий timestamp
    def update(selef, chat: UpdateInput) -> Chat:
        ...
