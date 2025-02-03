# coding=utf-8

from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.sql import func
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
)

from db.base import Base

if TYPE_CHECKING:
    from ..models import Message, User


class Chat(Base):
    """
    Chats table for storing chat information.

    Attributes:
        id (Integer): Unique chat ID.
        name (String): Chat name (only for group chats).
        is_group (Boolean): Defines whether the chat is a group or private.
        created_at (DateTime): Timestamp when the chat was created (UTC).
    """

    __tablename__ = "chat"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    is_group = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    messages: Mapped[list["Message"]] = relationship(
        "Message",
        back_populates="chat"
    )
    users: Mapped[list["User"]] = relationship(
        "User",
        secondary="chat_user",
        back_populates="chats"
    )
