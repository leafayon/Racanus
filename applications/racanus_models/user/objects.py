from datetime import UTC, datetime

from sqlalchemy import Column, DateTime, Enum
from sqlmodel import Field, SQLModel

from .enums import UserRoles


class UserBase(SQLModel):
    username: str = Field(max_length=255, unique=True)
    display_name: str | None = Field(None, max_length=255)

    role: UserRoles = Field(sa_column=Column(Enum(UserRoles)))

    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime | None = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True),
            onupdate=lambda: datetime.now(UTC)
        )
    )
