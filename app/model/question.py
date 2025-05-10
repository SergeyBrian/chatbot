from pydantic import BaseModel


class Question(BaseModel):
    id: int = 0
    category_id: int = 0
    question: str
    answer: str
