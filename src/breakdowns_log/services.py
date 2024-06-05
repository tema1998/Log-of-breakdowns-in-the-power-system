from typing import Any

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession


from auth.models import User
from breakdowns_log import schemas, models
from breakdowns_log.models import Breakdown


# class BreakdownService:
#
#     async def add(
#         db: AsyncSession, breakdown: schemas.BreakdownCreate, current_user: User
#     ) -> Any:
#         breakdown_data = breakdown.dict()
#         # # user_data = schemas.User.from_orm(current_user).dict()
#         # # breakdown_data["author_id"] = user_data["id"]
#         # db_breakdown = models.Breakdown(**breakdown_data)
#         # db.add(db_breakdown)
#         # db.commit()
#
#         stmt = insert(Breakdown).values(**breakdown_data)
#         await db.execute(stmt)

async def add(
    db: AsyncSession,
    breakdown: schemas.BreakdownCreate,
    current_user: User
    ) -> Any:

    breakdown_data = breakdown.dict()
    breakdown_data["author_id"] = 1

    query = insert(Breakdown).values(**breakdown_data)
    await db.execute(query)
    await db.commit()
