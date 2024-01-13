from pydantic import parse_obj_as
from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app import dto
from app.api import schems
from app.infrastructure.database.dao.rdb import BaseDAO
from app.infrastructure.database.models import User


class UserDAO(BaseDAO[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(User, session)

    async def add_user(
            self,
            firstname: str,
            lastname: str,
            email: str,
            password: str
    ) -> dto.User:
        result = await self.session.execute(
            insert(User).values(
                firstname=firstname,
                lastname=lastname,
                email=email,
                password=password
            ).returning(
                User
            )
        )
        await self.session.commit()
        return dto.User.from_orm(result.scalar())

    async def get_user(
            self,
            email: str,
            with_password: bool = False
    ) -> dto.User | dto.UserWithPassword:
        result = await self.session.execute(
            select(User).where(User.email == email)
        )
        user = result.scalar()
        if user is not None:
            if with_password:
                return dto.UserWithPassword.from_orm(user)
            else:
                return dto.User.from_orm(user)

    async def get_users(self) -> list[dto.User]:
        result = await self.session.execute(
            select(User)
        )
        return parse_obj_as(list[dto.User], result.scalars().all())

    # async def edit_user(self, user: schems.EditUser) -> dto.User:
    #     result = await self.session.execute(
    #         update(User).values(
    #             firstname=user.firstname,
    #             lastname=user.lastname,
    #         ).where(User.id == user.user_id).returning(
    #             User
    #         )
    #     )
    #     await self.session.commit()
    #     return dto.User.from_orm(result.scalar())

    async def delete_user(self, user_id: int) -> None:
        await self.session.execute(
            delete(User).where(User.id == user_id)
        )
        await self.session.commit()