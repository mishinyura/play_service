from abc import ABC
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

from app.models.user_model import User
from app.databases.base_db import BaseDB
from app.schemas.user_schema import UserSchema
from app.core.exceptions import SqlExeptions


class UserDB(BaseDB, ABC):
    async def get_all(self, session: AsyncSession) -> list[UserSchema]:
        """Направляет в БД запрос на получение всех пользователей"""
        result = await session.execute(select(User))
        users = result.scalars().all()
        return [UserSchema.model_validate(user) for user in users]

    async def get_user(self, user_id: int, session: AsyncSession) -> str:
        """Направляет в БД запрос на получение пользователя и возвращает его message"""
        result = await session.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()

        if user is None:
            raise
        else:
            return user.message

    async def add(self, user: User, session: AsyncSession) -> None:
        """Направляет в БД запрос на добавление записи"""
        try:
            session.add(user)
            await session.commit()
        except SQLAlchemyError as ex:
            await session.rollback()
            raise SqlExeptions(message=str(ex))


user_db = UserDB()