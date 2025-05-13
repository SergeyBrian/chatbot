from pydantic import BaseModel


class User(BaseModel):
    id: int = 0
    session_id: int
    name: str
    created_at: int = 0
