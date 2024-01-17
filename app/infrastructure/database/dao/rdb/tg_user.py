
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app import dto
from app.infrastructure.database.dao.rdb import BaseDAO
from app.infrastructure.database.models import TgUser


class TgUserDAO(BaseDAO[TgUser]):
    def __init__(self, session: AsyncSession):
        super().__init__(TgUser, session)

    async def add_tg_user(
            self,
            user_id: int,
            tg_id: int,
            phone_num: str
                          ) -> dto.TgUser:
        result = await self.session.execute(
            insert(TgUser).values(
                tg_id=tg_id,
                user_id=user_id,
                phone_num=phone_num
            ).returning(
                TgUser
            )
        )
        await self.session.commit()
        return dto.Todo.from_orm(result.scalar())

    async def get_tg_user(self, tg_user_id: int) -> dto.TgUser:
        result = await self.session.execute(
            select(TgUser).where(
                TgUser.id == tg_user_id
            )
        )
        tguser = result.scalar()
        if TgUser is not None:
            return dto.TgUser.from_orm(tguser)