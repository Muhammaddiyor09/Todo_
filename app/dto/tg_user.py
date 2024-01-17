from app.dto import Base


class TgUser(Base):
    user_id: int
    tg_id: int
    phone_num: int
