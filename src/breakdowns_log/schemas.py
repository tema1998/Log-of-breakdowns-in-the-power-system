import datetime
from typing import Optional

from pydantic import BaseModel


class BreakdownRead(BaseModel):
    """
    Pydantic model for mapping of Movie model.
    """
    id: int
    name: str
    electricity_object_id: int
    description: str
    created_at: datetime.datetime
    fixed: bool
    worker_fixed_id: Optional[int] = None
    fixed_at: Optional[datetime.datetime] = None

    class Config:
        orm_mode = True
