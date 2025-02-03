# coding=utf-8

from fastapi import HTTPException
from passlib.hash import bcrypt

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql import func


from db.models import User


async def create_user(
        db: AsyncSession,
        first_name: str,
        last_name: str,
        login: str,
        password: str,
        phone_number: str,
) -> User:
    """
    Creates a new user in the database.
    """

    # Get user from DB
    user: User = await db.scalar(
        select(
            User
        ).where(
            (
                    User.login == login
            ) | (
                    User.phone_number == phone_number
            )
        )
    )

    if user:
        # Exist
        raise HTTPException(
            status_code=404,
            detail="User with this login or phone number already exists."
        )

    # Generate Api-Key
    api_key = bcrypt.hash(f"{first_name}{last_name}{login}{password}{phone_number}")

    # Hashed password
    hashed_password = bcrypt.hash(password)

    # Create user
    new_user = User(
        User(
            first_name=first_name,
            last_name=last_name,
            login=login,
            api_key=api_key,
            hashed_password=hashed_password,
        )

    )
    db.add(new_user)

    # Save all changes
    await db.commit()
    await db.refresh(new_user)

    return {
        "success": True,
        "result": new_user,
    }


async def get_user(db_session: AsyncSession, user_id: int) -> dict:
    """
    Returns a single user record from the database by ID.

    :param db_session: Async SQLAlchemy session.
    :type db_session: AsyncSession
    :param user_id: The ID of the user to retrieve.
    :type user_id: int
    :return: A dictionary containing the user data.
    :rtype: dict
    """

    user_query = await db_session.execute(
        select(
            User
        ).where(
            User.id == user_id
        )
    )
    user = user_query.scalar_one_or_none()

    if not user:
        # Not found
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "success": True,
        "result": user
    }


async def get_users(
        db_session: AsyncSession,
        page: int = 0,
        on_page: int = 10
) -> list[dict]:
    """
    Returns paginated user records from the database with total count.

    :param db_session: Async SQLAlchemy session.
    :type db_session: AsyncSession
    :param page: The current page number (0-based index).
    :type page: int
    :param on_page: The number of records per page.
    :type on_page: int
    :return: A dictionary containing pagination metadata and user records.
    :rtype: list[dict]
    """

    # Defined 'total' value
    total_query = await db_session.execute(
        select(
            func.count()
        ).select_from(
            select(
                User
            ).subquery()
        )
    )
    total = total_query.scalar() or 0

    # Defined users
    users_query = await db_session.execute(
        select(
            User
        ).limit(
            on_page
        ).offset(
            page * on_page
        )
    )
    users = users_query.scalars().all()

    return {
        "success": True,
        "total": total,
        "page": page,
        "on_page": on_page,
        "next_page": (
            page + 1
            if on_page * (page + 1) < total
            else None
        ),
        "results": users
    }
