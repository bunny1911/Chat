# coding=utf-8

from pydantic import BaseModel
from datetime import datetime


class UserSchema(BaseModel):
    """
    Schema for serializing User model using Pydantic
    """

    id: int
    first_name: str
    last_name: str
    login: str
    phone_number: str
    created_at: datetime

    class Config:
        orm_mode = True
