from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, Boolean
from sqlalchemy.orm import DeclarativeBase


metadata = MetaData()

worker_object_association = Table(
    'worker_electricity_object',
    metadata,
    Column('worker_id', Integer, ForeignKey('worker.id')),
    Column('object_id', Integer, ForeignKey('electricity_object.id'))
)

worker = Table(
    'worker',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("first_name", String, nullable=False),
    Column("last_name", String, nullable=False),
    Column("job_title", String, nullable=False),
    Column("phone", String, nullable=False),
)

electricity_object = Table(
    'electricity_object',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("description", String, nullable=False),
    Column("address", String, nullable=False),
    Column("workers", TIMESTAMP, default=datetime.utcnow),
)

breakdown = Table(
    'defect',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("address", String, nullable=False),
    Column("description", String, nullable=False),
    Column("fixed", String, default=False),
    Column("who_fixed", String, nullable=True),
)
