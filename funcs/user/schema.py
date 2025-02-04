# coding=utf-8

from pydantic import BaseModel, Field
from datetime import datetime


class UserSchema(BaseModel):
    """
    Schema for serializing User model using Pydantic
    """

    id: int | None = Field(
        None,
        description="Unique user ID",
        example=1,
        readOnly=True,
    )
    first_name: str = Field(
        ...,
        description="User's first name",
        example="John"
    )
    last_name: str = Field(
        ...,
        description="User's last name",
        example="Doe"
    )
    login: str = Field(
        ...,
        description="User's login username",
        example="johndoe"
    )
    phone_number: str = Field(
        ...,
        description="User's phone number",
        example="+1234567890"
    )
    created_at: datetime | None = Field(
        None,
        description="Account creation date (UTC)",
        example="2025-02-01T12:00:00Z",
        readOnly=True
    )

    class Config:
        orm_mode = True
