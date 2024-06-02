from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from breakdowns_log.models import Breakdown, ElectricityObject
from breakdowns_log.schemas import BreakdownRead
from database import get_async_session

router = APIRouter(
    prefix="/breakdowns",
    tags=["Breakdowns"]
)


@router.get('/', response_model=list[BreakdownRead])
async def get_breakdowns(session: AsyncSession = Depends(get_async_session)):
    query = select(Breakdown)
    result = await session.scalars(query)
    return result.all()
