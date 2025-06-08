from sqlmodel import Field

from .objects import MessageBase


class Message(MessageBase, table=True):
    __tablename__ = "messages"

    id: int = Field(primary_key=True)

    user_id: int | None = Field(default=None, foreign_key="users.id")
