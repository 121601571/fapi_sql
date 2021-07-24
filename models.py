from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime,func
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

class MyUser(Base):
    __tablename__ = "myuser"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password =  Column(String) # should be hashed..
    email = Column(String, unique=True, index=True)
    telnum = Column(String)
    created_on = Column(DateTime, server_default=func.current_timestamp())
    modified_on = Column(DateTime, default=func.current_timestamp(),
                         onupdate=func.current_timestamp())
    is_active = Column(Boolean, default=True)
    role = Column(Integer, default=1)
