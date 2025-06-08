from sqlmodel import Field

from .objects import UserBase


class User(UserBase, table=True):
    __tablename__ = "users"

    id: int = Field(primary_key=True)

    email: str | None = Field(None, max_length=255, unique=True)
    password: str = Field(max_length=255)
