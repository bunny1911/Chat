# coding=utf-8

from pydantic import BaseModel

from funcs.user.schema import UserSchema
from schemas import ResponsePaginationSchema


class ResponseUserSchema(BaseModel):
    """
    Schema for wrapping user response with success status.
    """

    success: bool
    result: UserSchema


class ResponseUsersSchema(ResponsePaginationSchema):
    """
    Schema for wrapping user response with success status.
    """

    results: list[UserSchema]

