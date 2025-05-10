from app.db.categories.usecases import Interface, SelectInput
from app.db.connector import get_cursor
from app.model.category import Category


class Repo(Interface):
    def __init__(self):
        self.cur = get_cursor()

    def create(self, msg: Category) -> Category:
        ...

    def get(self, req: SelectInput) -> list[Category]:
        ...
