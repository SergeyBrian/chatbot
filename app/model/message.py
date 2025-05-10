from pydantic import BaseModel


class Message(BaseModel):
    id: int
    dialog_id: int
    sender: int
    content: str
    created_at: int
