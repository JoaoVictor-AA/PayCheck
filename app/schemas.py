from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class CreateUser(BaseModel):
    name: str
    created_at: datetime