from pydantic import BaseModel


class QuestionCSV(BaseModel):
    category: str
    question: str
    answer: str
