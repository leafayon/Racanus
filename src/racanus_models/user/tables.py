from datetime import datetime

from sqlalchemy import TIMESTAMP, Enum, String, func
from sqlalchemy.orm import Mapped, mapped_column

from ..base import BaseTable
from .enums import UserRoles


class User(BaseTable):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column(
        String(32),
        unique=True
    )
    display_name: Mapped[str] = mapped_column(
        String(32),
        default=None,
        nullable=True
    )

    role: Mapped[UserRoles] = mapped_column(
        Enum(UserRoles),
        default=UserRoles.MEMBER
    )

    password: Mapped[str] = mapped_column(String(255))

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.current_timestamp()
    )
    updated_at: Mapped[datetime | None] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=None,
        onupdate=func.current_timestamp(),
        nullable=True
    )

    def __repr__(self) -> str:
        return (
            f"User("
            f"id={self.id!r}, "
            f"username={self.username!r}, "
            f"display_name={self.display_name!r}, "
            f"role={self.role!r}, "
            f"created_at={self.created_at}, "
            f"updated_at={self.updated_at}"
            ")"
        )
