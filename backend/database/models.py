"""
DB Model Files
"""
import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Text, Float
from sqlalchemy.orm import relationship, backref

from backend.database.setup import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=False)
    email = Column(String, unique=True, index=True)
    name = Column(String, unique=False, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    context_list = relationship("UserContext", back_populates="user")


class Bike(Base):

    __tablename__ = "bike"

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    active = Column(Boolean)
    description = Column(Boolean)
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)


class BikeSetting(Base):
    __tablename__ = "bike_setting"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    bike_id = Column(Integer, ForeignKey("bike.id"))
    fork_psi = Column(Float, nullable=True, default=0)
    shock_psi = Column(Float, nullable=True, default=0)
    front_wheel_psi = Column(Float, nullable=True, default=0)
    back_wheel_psi = Column(Float, nullable=True, default=0)
    front_wheel_size = Column(Float, nullable=False, default=29)
    rear_wheel_size = Column(Float, nullable=False, default=29)
    fork_travel = Column(Float, nullable=True, default=0)
    shock_travel = Column(Float, nullable=True, default=0)

    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)

    user = relationship("User", back_populates="context_list")
    context_info = relationship("Context", backref=backref("info", lazy="joined"))