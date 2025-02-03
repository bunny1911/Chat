# coding=utf-8

from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped
from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    UniqueConstraint,
)

from db.base import Base

if TYPE_CHECKING:
    from ..models import Chat, User


class ChatUser(Base):
    """
    Association table between users and chats.

    Attributes:
        user_id (Integer): ID of the user.
        chat_id (Integer): ID of the chat.
    """

    __tablename__ = "chat_user"
    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "chat_id",
            name="uq_chat_user"
        ),
    )

    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), primary_key=True)
    chat_id = Column(Integer, ForeignKey("chat.id", ondelete="CASCADE"), primary_key=True)

    user: Mapped["User"] = relationship(
        "User"
    )
    chat: Mapped["Chat"] = relationship(
        "Chat")
