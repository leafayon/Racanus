from ...constants import DATABASE_ENGINE
from ...racanus_models.base import BaseTable
from ...racanus_models.user.tables import User


def init_database() -> None:
    BaseTable.metadata.create_all(DATABASE_ENGINE)
