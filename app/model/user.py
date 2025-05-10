from pydantic import BaseModel


class User(BaseModel):
    id: int
    session_id: str
    name: str
    created_at: int
