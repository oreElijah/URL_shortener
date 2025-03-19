from typing import Optional
from pydantic import BaseModel

class Url(BaseModel):
    original_url: str
    id: Optional[int] = None