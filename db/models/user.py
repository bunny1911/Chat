# coding=utf-8

from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.sql import func
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)

from ..base import Base

if TYPE_CHECKING:
    from ..models import Message, Chat


class User(Base):
    """
    Users table for authentication and profile management.

    Attributes:
        id (Integer): Unique user ID.
        first_name (String): User's first name.
        last_name (String): User's last name.
        login (String): Unique username for authentication.
        api_key (String): API key for secure authentication.
        phone_number (String): User's phone number.
        hashed_password (String): Hashed password for security.
        created_at (DateTime): Timestamp when the account was created (UTC).
    """

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    login = Column(String, unique=True, index=True, nullable=False)
    api_key = Column(String, unique=True, nullable=False)
    phone_number = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    messages: Mapped[list["Message"]] = relationship(
        "Message",
        back_populates="sender"
    )
    chats: Mapped[list["Chat"]] = relationship(
        "Chat",
        secondary="chat_user",
        back_populates="users"
    )
