from app.db.questions.usecases import Interface, SelectInput
from app.db.connector import get_cursor
from app.model.question import Question


class Repo(Interface):
    def __init__(self):
        self.cur = get_cursor()

    def create(self, msg: Question) -> Question:
        ...

    def get(self, req: SelectInput) -> list[Question]:
        ...
