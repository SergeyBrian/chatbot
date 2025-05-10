from app.db.messages.usecases import Interface, SelectInput
from app.db.connector import get_cursor
from app.model.message import Message


class Repo(Interface):
    def __init__(self):
        self.cur = get_cursor()

    def create(self, msg: Message) -> Message:
        return Message(content="sosal")

    def get(self, req: SelectInput) -> list[Message]:
        return [Message(content="sosal")]
