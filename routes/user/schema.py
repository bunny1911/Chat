# coding=utf-8

from pydantic import BaseModel

from funcs.user.schema import UserSchema


class ResponseUserSchema(BaseModel):
    """
    Schema for wrapping user response with success status.
    """

    success: bool
    result: UserSchema
