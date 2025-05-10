from pydantic import BaseModel


class Message(BaseModel):
    id: int = 0
    dialog_id: int = 0
    sender: int = 0
    content: str
    created_at: int = 0
    useful: bool | None = None
