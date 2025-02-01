# coding=utf-8

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
)

from db.base import Base


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

    messages = relationship(
        "Message",
        back_populates="chat"
    )
    users = relationship(
        "User",
        secondary="chat_users",
        back_populates="chats"
    )

