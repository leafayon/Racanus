from .base import ClientException


class UserNotFound(ClientException):
    def __init__(self):
        ClientException.__init__(
            self,
            404,
            "USER_NOT_FOUND",
            "User are not found in the database, impossible to get, update or delete it."
        )


class UserAlreadyExist(ClientException):
    def __init__(self) -> None:
        ClientException.__init__(
            self,
            409,
            "USER_ALREADY_EXIST",
            "Impossible to create or update this user when a user with the same username already exist."
        )
