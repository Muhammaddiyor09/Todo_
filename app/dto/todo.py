

from app.dto import Base


class Todo(Base):
    title: str
    completed: bool
    user_id: int

class EditCompleted(Base):
    todo_id: int
    edit_completed: bool

