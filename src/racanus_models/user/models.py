from datetime import datetime

from pydantic import BaseModel, Field

from .enums import UserRoles


class PublicUser(BaseModel):
    class Config:
        from_attributes = True

    id: int = Field()

    username: str = Field(max_length=32)
    display_name: str | None = Field(max_length=32)

    role: UserRoles = Field()

    created_at: datetime = Field()
    updated_at: datetime | None = Field()


class CreateUserPayload(BaseModel):
    username: str = Field(max_length=32)
    display_name: str | None = Field(max_length=32)

    role: UserRoles = Field()

    password: str = Field(max_length=255)


class UpdateUserPayload(BaseModel):
    username: str | None = Field(default=None, max_length=32)
    display_name: str | None = Field(default=None, max_length=32)

    role: UserRoles | None = Field(default=None)
