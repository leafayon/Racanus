from os import getenv
from typing import TYPE_CHECKING

from dotenv import load_dotenv

if TYPE_CHECKING:
    from flask import Flask


class Config:
    def __init__(self, flask_application: "Flask") -> None:
        load_dotenv()

        self.__flask_application = flask_application

        self.__flask_application.config["SERVER_NAME"] = f"{getenv("RACANUS_WEB_HOST")}:{getenv("RACANUS_WEB_PORT")}"
        self.__flask_application.config["DEBUG"] = getenv("RACANUS_WEB_DEBUG")

        self.__flask_application.config["DATABASE"] = {}
        self.__flask_application.config["DATABASE"]["HOST"] = getenv("RACANUS_DATABASE_HOST")
        self.__flask_application.config["DATABASE"]["PORT"] = getenv("RACANUS_DATABASE_PORT")
        self.__flask_application.config["DATABASE"]["USER"] = getenv("RACANUS_DATABASE_USER")
        self.__flask_application.config["DATABASE"]["PASSWORD"] = getenv("RACANUS_DATABASE_PASSWORD")
        self.__flask_application.config["DATABASE"]["DB"] = getenv("RACANUS_DATABASE_DB")
