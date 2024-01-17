from app.dto import Base


class User(Base):

    firstname: str
    lastname: str
    email: str
    phone_num: int

class UserWithPassword(User):

    password: str