# coding=utf-8

from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.sql import func
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
)

from db.base import Base

if TYPE_CHECKING:
    from ..models import Chat, User


class Message(Base):
    """
    Messages table for storing chat messages.

    Attributes:
        id (Integer): Unique message ID.
        sender_id (Integer): ID of the user who sent the message.
        chat_id (Integer): ID of the chat where the message was sent.
        content (String): Text content of the message.
        created_at (DateTime): Timestamp when the message was created (UTC).
    """

    __tablename__ = "message"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    chat_id = Column(Integer, ForeignKey("chat.id", ondelete="CASCADE"), nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    sender: Mapped["User"] = relationship(
        "User",
        back_populates="messages"
    )
    chat: Mapped["Chat"] = relationship(
        "Chat",
        back_populates="messages"
    )
