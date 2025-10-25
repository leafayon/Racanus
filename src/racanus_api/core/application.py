from datetime import UTC, datetime

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response

from ...settings import Settings
from ..routes.user import UserController
from .database import init_database
from .exceptions.base import RacanusException


class Application:
    def __init__(self) -> None:
        self._application = FastAPI()

        self.settings = Settings()

        self._setup()

    def _setup(self) -> None:
        self._handlers()
        self._routes()

    def _handlers(self) -> None:
        self._application.add_event_handler("startup", lambda: init_database())

        self._application.add_exception_handler(RacanusException, self._exception_handler)

    def _routes(self) -> None:
        self._application.include_router(UserController().router, prefix="/users")

    async def _exception_handler(self, request: Request, exception: RacanusException) -> Response:
        return JSONResponse(
            status_code=exception.status_code,
            headers=exception.headers,
            content={
                "timestamp": datetime.now(UTC).timestamp(),
                "message": exception.message,
                "description": exception.description
            }
        )

    @property
    def application(self) -> FastAPI:
        return self._application
