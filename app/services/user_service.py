from sqlalchemy.ext.asyncio import AsyncSession

from app.databases.user_db import user_db
from app.schemas.user_schema import UserRequestSchema, UserSchema
from app.models.user_model import User
from app.core.exceptions import SqlExeptions


class UserService:
    def __init__(self):
        self.repo = user_db

    async def get_all_users(self, session: AsyncSession) -> list[UserSchema]:

        users = await self.repo.get_all(session=session)
        return users

    async def add_user(self, session: AsyncSession, request: UserRequestSchema) -> None:
        user = User(message=request.message)

        try:
            await self.repo.add(user=user, session=session)
        except SqlExeptions as ex:
            raise SqlExeptions(message=str(ex))

    async def get_message(self, session: AsyncSession, user_id: int) -> str:
        message = await self.repo.get_user(user_id=user_id, session=session)
        return message


user_service = UserService()