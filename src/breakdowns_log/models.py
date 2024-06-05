from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, ForeignKey, Boolean, DateTime, func
from sqlalchemy.orm import DeclarativeBase, relationship, backref

from auth.models import Base


metadata = Base.metadata

worker_object_association = Table(
    'worker_electricity_object',
    metadata,
    Column('worker_id', Integer, ForeignKey('worker.id')),
    Column('object_id', Integer, ForeignKey('electricity_object.id'))
)


class Breakdown(Base):
    __tablename__ = 'breakdown'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    electricity_object_id = Column(Integer, ForeignKey("electricity_object.id"))
    electricity_objects = relationship("ElectricityObject", back_populates="breakdowns")
    description = Column(String, nullable=True)
    author_id = Column(Integer, ForeignKey("worker.id"))
    author = relationship("Worker", back_populates="breakdowns_created", foreign_keys=[author_id])
    created_at = Column(DateTime(timezone=True), default=func.now())
    fixed = Column(Boolean, default=False)
    worker_fixed_id = Column(Integer, ForeignKey("worker.id"))
    worker_fixed = relationship("Worker", back_populates="breakdowns_fixed", foreign_keys=[worker_fixed_id])
    fixed_at = Column(DateTime(timezone=True), nullable=True)


class Worker(Base):
    __tablename__ = 'worker'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", backref=backref("worker", uselist=False))
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    job_title = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    electricity_objects = relationship('ElectricityObject', secondary=worker_object_association, back_populates='workers')
    breakdowns_created = relationship("Breakdown", back_populates="author", foreign_keys=[Breakdown.author_id])
    breakdowns_fixed = relationship("Breakdown", back_populates="worker_fixed", foreign_keys=[Breakdown.worker_fixed_id])


class ElectricityObject(Base):
    __tablename__ = 'electricity_object'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    address = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    workers = relationship('Worker', secondary=worker_object_association, back_populates='electricity_objects')
    breakdowns = relationship("Breakdown", back_populates="electricity_objects")






