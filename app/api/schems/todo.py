from pydantic import BaseModel


class Todo(BaseModel):
    title: str


class EditTodo(Todo):
    todo_id: int


class EditCompleted(BaseModel):
    todo_id: int
    completed: bool
