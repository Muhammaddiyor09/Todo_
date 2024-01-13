from fastapi import APIRouter, Query, Path, Depends

from app import dto
from app.api import schems
from app.api.dependencies import dao_provider, get_user
from app.infrastructure.database.dao import HolderDao

router = APIRouter(prefix="/todo")


@router.get(path="/all")
async def get_todos(
        dao: HolderDao = Depends(dao_provider),
        user: dto.User = Depends(get_user)
) -> list[dto.Todo]:
    return await dao.todo.get_todos(user_id=user.id)


@router.get(path="/{todo_id}")
async def get_article(
        todo_id: int,
        dao: HolderDao = Depends(dao_provider),
        user: dto.User = Depends(get_user)
) -> dto.Todo:
    return await dao.todo.get_todo(todo_id=todo_id, user_id=user.id)


@router.post(path="/new")
async def new_todo(
        todo: schems.Todo,
        user: dto.User = Depends(get_user),
        dao: HolderDao = Depends(dao_provider)
) -> dto.Todo:
    return await dao.todo.add_todo(todo=todo, user_id=user.id)


@router.put(path="/edit")
async def edit_todo(
        todo: schems.EditTodo,
        dao: HolderDao = Depends(dao_provider),
        user: dto.User = Depends(get_user)
) -> dto.Todo:
    return await dao.todo.edit_todo(todo=todo, user_id=user.id)


@router.put(path="/completed")
async def edit_completed(
        completed: schems.EditCompleted,
        dao: HolderDao = Depends(dao_provider),
        user: dto.User = Depends(get_user)
) -> dto.Todo:
    return await dao.todo.edit_completed(todo=completed, user_id=user.id)


@router.delete(path="/delete")
async def delete_todo(
        todo_id: int = Query(alias="todoId"),
        dao: HolderDao = Depends(dao_provider),
        user: dto.User = Depends(get_user)
):
    return await dao.todo.delete_todo(todo_id=todo_id, user_id=user.id)
