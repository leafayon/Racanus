from .objects import UserBase


class UserGet(UserBase):
    id: int


class UserPost(UserBase):
    id: int
