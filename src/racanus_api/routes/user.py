from fastapi import APIRouter, Query
from sqlalchemy import delete, insert, select, update
from sqlalchemy.orm import Session

from ...constants import DATABASE_ENGINE
from ...racanus_models.user.models import CreateUserPayload, PublicUser, UpdateUserPayload
from ...racanus_models.user.tables import User
from ..core.exceptions.user import UserAlreadyExist, UserNotFound


class UserController:
    def __init__(self) -> None:
        self.router = APIRouter()

        self.router.add_api_route("/", self.get_users, methods=["GET"],  response_model=list[PublicUser])
        self.router.add_api_route("/{user_id}", self.get_user, methods=["GET"], response_model=PublicUser)
        self.router.add_api_route("/", self.create_user, methods=["POST"], status_code=201)
        self.router.add_api_route("/{user_id}", self.update_user, methods=["PATCH"])
        self.router.add_api_route("/{user_id}", self.delete_user, methods=["DELETE"])

    def get_users(
            self,
            offset: int = 0,
            limit: int = Query(default=100, le=100)
    ) -> list[PublicUser]:
        with Session(DATABASE_ENGINE) as session:
            users = session.execute(select(User).offset(offset).limit(limit)).all()

            return [PublicUser.model_validate(user[0]) for user in users]

    def get_user(self, user_id: int) -> PublicUser:
        with Session(DATABASE_ENGINE) as session:
            user = session.execute(select(User).where(User.id==user_id)).scalar()

            if user is None: raise UserNotFound()

            return PublicUser.model_validate(user)

    def create_user(self, payload: CreateUserPayload) -> None:
        with Session(DATABASE_ENGINE) as session:
            existing_user = session.execute(select(User).where(User.username == payload.username)).scalar()

            if existing_user: raise UserAlreadyExist()

            session.execute(insert(User).values(id=None, **CreateUserPayload.model_dump(payload)))
            session.commit()

    def update_user(self, user_id: int, payload: UpdateUserPayload) -> None:
        with Session(DATABASE_ENGINE) as session:
            if payload.username is not None:
                existing_user = session.execute(select(User).where(User.username == payload.username)).scalar()

                if existing_user: raise UserAlreadyExist()

            payload = UpdateUserPayload.model_dump(payload, exclude_none=True)

            session.execute(update(User).where(User.id == user_id).values(**payload))
            session.commit()

    def delete_user(self, user_id: int) -> None:
        with Session(DATABASE_ENGINE) as session:
            user = session.execute(select(User).where(User.id == user_id)).scalar()

            if not user: raise UserNotFound()

            session.execute(delete(User))
            session.commit()
