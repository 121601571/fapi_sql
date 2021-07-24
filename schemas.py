from typing import List, Optional

from pydantic import BaseModel
import datetime

class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True



class MyUserBase(BaseModel):
    email: str
    username: str
    is_active: bool
    role: int
    telnum: str


class MyUserCreate(MyUserBase):
    password: str


class MyUser(MyUserBase):
    id: int
    created_on: datetime.datetime
    modified_on: datetime.datetime
    class Config:
        orm_mode = True
