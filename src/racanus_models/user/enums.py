from enum import StrEnum


class UserRoles(StrEnum):
    ADMIN = "ADMIN"
    MODERATOR = "MODERATOR"
    AUTHOR = "AUTHOR"
    MEMBER = "MEMBER"
