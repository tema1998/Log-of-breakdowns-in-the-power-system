from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from auth.depends import current_user
from auth.models import User
from breakdowns_log.models import Breakdown, ElectricityObject
from breakdowns_log import schemas
from breakdowns_log.services import add
from database import get_async_session

router = APIRouter(
    prefix="/breakdowns",
    tags=["Breakdowns"]
)


@router.get('/',
            response_model=list[schemas.BreakdownInDB])
async def get_breakdowns(user: User = Depends(current_user), db: AsyncSession = Depends(get_async_session)):
    query = select(Breakdown)
    result = await db.scalars(query)
    return result.all()


@router.post(
    '/',
    status_code=status.HTTP_201_CREATED)
async def add_breakdowns(breakdown: schemas.BreakdownCreate,
                         user: User = Depends(current_user),
                         db: AsyncSession = Depends(get_async_session)):
    result = await add(db=db, breakdown=breakdown, current_user=user)
    return result
