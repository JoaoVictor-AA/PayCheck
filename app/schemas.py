from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserOut(BaseModel):
    name: str
    password: str



class CreateUser(BaseModel):
    name: str
    password: str