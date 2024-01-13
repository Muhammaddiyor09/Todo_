from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.models import BaseModel


class Todo(BaseModel):

    __tablename__ = "todo"

    title: Mapped[str] = mapped_column(String, nullable=False)
    completed: Mapped[str] = mapped_column(Boolean, nullable=True, default=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))

