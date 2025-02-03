# coding=utf-8

from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from routes.user.schema import *
from schemas import RequestPaginationSchema
import funcs.user.funcs as funcs
from db.session import get_db


user_router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@user_router.get(
    "/",
    response_model=ResponseUsersSchema,
    summary="Get paginated list of users"
)
async def get_users(
    db_session: AsyncSession = Depends(get_db),
    pagination: RequestPaginationSchema = Depends()
):
    """
    Returns paginated user records from the database with total count.
    """

    return await funcs.get_users(
        db_session=db_session,
        page=pagination.page,
        on_page=pagination.on_page
    )


@user_router.get(
    "/{user_id}",
    response_model=ResponseUserSchema,
    summary="Get user details"
)
async def get_user(
        user_id: int,
        db_session: AsyncSession = Depends(get_db)
) -> dict:
    """
    Returns a single user record from the database by ID.
    """

    return await funcs.get_user(
        db_session=db_session,
        user_id=user_id
    )
