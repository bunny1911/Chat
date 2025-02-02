# coding=utf-8

from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from routes.user.schema import ResponseUserSchema
import funcs.user.funcs as funcs
from db.session import get_db


user_router = APIRouter()


@user_router.get(
    "/users/{user_id}",
    response_model=ResponseUserSchema
)
async def get_user(
        user_id: int,
        db_session: AsyncSession = Depends(get_db)
) -> dict:
    """
    API endpoint to get a single user by ID.
    """

    return await funcs.get_user(
        db_session=db_session,
        user_id=user_id
    )


