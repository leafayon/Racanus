from flask import Flask

from ..constants import STATIC_PATH, TEMPLATES_PATH
from .settings import Config


class Application:
    def __init__(self) -> None:
        self.__flask_application = Flask(
            __name__,
            static_folder=STATIC_PATH,
            template_folder=TEMPLATES_PATH
        )

        Config(self.__flask_application)

    def start(self) -> None:
        self.__flask_application.run(load_dotenv=False)
