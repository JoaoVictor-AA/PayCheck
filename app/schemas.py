from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserOut(BaseModel):
    name: str
    id: int


class CreateUser(BaseModel):
    name: str
    password: str
    email: str


class MakeTransaction(BaseModel):
    pass