from datetime import datetime
from typing import List

from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, \
    SQLAlchemyBaseOAuthAccountTable
from sqlalchemy import Integer, String, Boolean, Column, ForeignKey, TIMESTAMP, JSON
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship, mapped_column, declared_attr
from database import get_async_session


class Base(DeclarativeBase):
    pass


class OAuthAccount(SQLAlchemyBaseOAuthAccountTable[int], Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    @declared_attr
    def user_id(cls) -> Mapped[int]:
        return mapped_column(Integer, ForeignKey("user.id", ondelete="cascade"), nullable=False)


class Role(Base):
    __tablename__ = 'role'

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String, nullable=False)
    permissions = Column("permissions", JSON, nullable=False)


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'user'

    id = Column("id", Integer, primary_key=True)
    username = Column("username", String, nullable=False)
    registered_at = Column("registered_at", TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey("role.id"))

    email = Column(
        String(length=320), unique=True, index=True, nullable=False
    )
    hashed_password = Column(
        String(length=1024), nullable=False
    )
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(
        Boolean, default=False, nullable=False
    )
    is_verified = Column(
        Boolean, default=False, nullable=False
    )
    oauth_accounts: Mapped[List[OAuthAccount]] = relationship(
        "OAuthAccount", lazy="joined"
    )


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User, OAuthAccount)