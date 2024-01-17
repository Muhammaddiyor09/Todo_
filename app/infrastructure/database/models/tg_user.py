from sqlalchemy import BigInteger,String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.models import BaseModel


class TgUser(BaseModel):

    __tablename__ = "tg_user"

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    tg_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    phone_num: Mapped[str] = mapped_column(String, nullable=False)