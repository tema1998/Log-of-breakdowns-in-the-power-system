from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session

router = APIRouter(
    prefix="/breakdowns",
    tags=["Breakdowns"]
)


@router.get('/')
async def get_breakdowns(session: AsyncSession = Depends(get_async_session)):
    return