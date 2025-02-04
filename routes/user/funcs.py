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


@user_router.post(
    "/register",
    response_model=ResponseUserSchema,
    summary="Register a new user",
    description="Register a new user"
)
async def register_user(
    user_data: RequestUserSchema,
    db_session: AsyncSession = Depends(get_db)
) -> dict:
    """
    Creates a new user.
    """

    return await funcs.create_user(
        db_session=db_session,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        login=user_data.login,
        phone_number=user_data.phone_number,
        password=user_data.password,
    )


@user_router.get(
    "/",
    response_model=ResponseUsersSchema,
    summary="Get paginated list of users"
)
async def get_users(
    pagination: RequestPaginationSchema,
    db_session: AsyncSession = Depends(get_db),
) -> dict:
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
