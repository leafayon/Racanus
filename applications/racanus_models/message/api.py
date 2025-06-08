from .objects import MessageBase


class MessageGet(MessageBase):
    id: int
    user_id: int


class MessagePost(MessageBase):
    id: int
