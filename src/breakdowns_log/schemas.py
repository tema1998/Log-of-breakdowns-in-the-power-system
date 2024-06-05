import datetime
from typing import Optional

from pydantic import BaseModel


class BreakdownInDB(BaseModel):
    """
    Pydantic model for mapping of Breakdown model.
    """
    id: int
    name: str
    electricity_object_id: int
    description: str
    author: Optional[int] = None
    created_at: datetime.datetime
    fixed: bool
    worker_fixed_id: Optional[int] = None
    fixed_at: Optional[datetime.datetime] = None

    class Config:
        orm_mode = True


class BreakdownCreate(BaseModel):
    """
    Pydantic model for creating of Breakdown model.
    """
    name: str
    electricity_object_id: int
    description: str

    class Config:
        orm_mode = True