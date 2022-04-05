import datetime
from typing import Optional

from pydantic import BaseModel, constr


class User(BaseModel):
    name: str
    surname: str
    phone: Optional[constr(max_length=10)] = None
    login: str
    password: str
    is_admin: Optional[bool] = False

    class Config:
        orm_mode = True


class Book(BaseModel):
    name: str
    category_id: int
    author_fullname: str
    date: datetime.date

    class Config:
        orm_mode = True
