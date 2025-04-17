from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_session
from app.services.user_service import user_service
from app.schemas.user_schema import UserRequestSchema, UserSchema


user_roter = APIRouter(prefix='/users')


@user_roter.get('/', response_model=list[UserSchema])
async def all_users(
        session: AsyncSession = Depends(get_session)
) -> list[UserSchema]:
    users = await user_service.get_all_users(session=session)
    return users


@user_roter.post('/', response_model=None)
async def create_user(
        request: UserRequestSchema,
        session: AsyncSession = Depends(get_session)
) -> None:
    await user_service.add_user(session=session, request=request)


@user_roter.get('/{user_id}', response_model=str)
async def get_message(
        user_id: int,
        session: AsyncSession = Depends(get_session)
) -> str:
    message = await user_service.get_message(user_id=user_id, session=session)
    return message