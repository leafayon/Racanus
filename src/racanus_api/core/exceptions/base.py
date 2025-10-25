class RacanusException(Exception):
    def __init__(
            self,
            status_code: int,
            message: str,
            description: str,
            headers: dict[str, str] | None = None
    ) -> None:
        self.status_code = status_code
        self.message = message
        self.description = description
        self.headers = headers


class ClientException(RacanusException): ...


class ServerException(RacanusException): ...
