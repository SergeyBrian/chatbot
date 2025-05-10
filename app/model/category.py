from pydantic import BaseModel


class Category(BaseModel):
    id: int = 0
    name: str
