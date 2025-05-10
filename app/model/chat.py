from pydantic import BaseModel, Field
from typing import Literal


class Chat(BaseModel):
    id: int
    user_id: int
    status: Literal['new', 'in_progress', 'closed'] = Field(default='new')
    started_at: int
    closed_at: int = 0
