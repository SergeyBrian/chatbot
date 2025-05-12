from typing import Protocol, Optional
from app.model.question import Question
from app.model.question_csv import QuestionCSV
from pydantic import BaseModel


class SelectInput(BaseModel):
    limit: Optional[int] = 25
    offset: Optional[int] = 0
    category_id: int = 0
    search: Optional[str] = ""


class Interface(Protocol):
    def create(self, msg: Question) -> Question:
        ...

    def get(self, req: SelectInput) -> list[Question]:
        ...

    def delete(self, id: int) -> int:
        ...

    def get_all_for_export(self) -> list[QuestionCSV]:
        ...

    def import_from_csv(self, questions: list[QuestionCSV]) -> int:
        ...


class Usecases:
    def __init__(self, conn: Interface):
        self.db: Interface = conn

    def create(self, msg: Question) -> Question:
        return self.db.create(msg)

    def get(self, req: SelectInput) -> list[Question]:
        return self.db.get(req=req)

    def delete(self, id: int) -> int:
        return self.db.delete(id=id)

    def get_all_for_export(self) -> list[QuestionCSV]:
        return self.db.get_all_for_export()

    def import_from_csv(self, questions: list[QuestionCSV]) -> int:
        return self.db.import_from_csv(questions)
