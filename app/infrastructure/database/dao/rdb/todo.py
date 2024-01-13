from pydantic import parse_obj_as
from sqlalchemy import insert, select, update, delete, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app import dto
from app.api import schems
from app.infrastructure.database.dao.rdb import BaseDAO
from app.infrastructure.database.models import Todo


class TodoDAO(BaseDAO[Todo]):
    def __init__(self, session: AsyncSession):
        super().__init__(Todo, session)

    async def add_todo(self, todo: schems.Todo, user_id: int) -> dto.Todo:
        result = await self.session.execute(
            insert(Todo).values(
                title=todo.title,
                user_id=user_id
            ).returning(
                Todo
            )
        )
        await self.session.commit()
        return dto.Todo.from_orm(result.scalar())

    async def get_todo(self, todo_id: int, user_id: int) -> dto.Todo:
        result = await self.session.execute(
            select(Todo).where(
                Todo.id == todo_id,
                user_id=user_id
            )
        )
        todo = result.scalar()
        if Todo is not None:
            return dto.Todo.from_orm(todo)

    async def get_todos(self, user_id: int) -> list[dto.Todo]:
        result = await self.session.execute(
            select(Todo).where(Todo.user_id == user_id)
        )
        return parse_obj_as(list[dto.Todo], result.scalars().all())

    async def edit_todo(self, todo: schems.EditTodo, user_id: int) -> dto.Todo:
        result = await self.session.execute(
            update(Todo).values(
                title=todo.title,
                user_id=user_id
            ).where(Todo.id == todo.todo_id).returning(
                Todo
            )
        )

        await self.session.commit()
        return dto.Todo.from_orm(result.scalar())

    async def edit_completed(self, todo: schems.EditCompleted, user_id:int) -> dto.EditCompleted:
        result = await self.session.execute(
            update(Todo).values(
                completed=todo.completed,
                id=todo.todo_id,
                user_id=user_id
            ).where(Todo.id == todo.todo_id).returning(

                Todo
            )

        )
        await self.session.commit()
        return dto.Todo.from_orm(result.scalar())

    async def delete_todo(self, todo_id: int, user_id: int) -> None:
        await self.session.execute(
            delete(Todo).where(
                and_(
                    Todo.id == todo_id,
                    Todo.user_id == user_id
                )
            )
        )
        await self.session.commit()
