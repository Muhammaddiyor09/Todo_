from fastapi import APIRouter, Query, Path, Depends

from app import dto
from app.api import schems
from app.api.dependencies import dao_provider
from app.infrastructure.database.dao import HolderDao

router = APIRouter(prefix="/user")


@router.get(path="/all")
async def get_users(
    dao: HolderDao = Depends(dao_provider)

    ) -> list[dto.User]:
    return await dao.user.get_users()


@router.get(path="/{user_id}")
async def get_article(
    user_id: int,
    dao: HolderDao = Depends(dao_provider)
    ) -> dto.User:
    return await dao.user.get_user(user_id=user_id)


@router.post(path="/new")
async def new_user(
        user: schems.User,
        dao: HolderDao = Depends(dao_provider)
) -> dto.User:
    return await dao.user.add_user(user=user)


# @router.put(path="/edit")
# async def edit_user(
#         user: schems.EditUser,
#         dao: HolderDao = Depends(dao_provider)
# ) -> dto.User:
#     return await dao.user.edit_user(user=user)


@router.delete(path="/delete")
async def delete_user(
        user_id: int = Query(alias="userId"),
        dao: HolderDao = Depends(dao_provider)
):
    return await dao.user.delete_user(user_id=user_id)