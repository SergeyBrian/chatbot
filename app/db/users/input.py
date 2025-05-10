from typing import Optional
from pydantic import BaseModel


class SelectRequest(BaseModel):
    limit: Optional[int] = 25
    offset: Optional[int] = 0
