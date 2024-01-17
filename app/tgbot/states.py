from aiogram.fsm.state import StatesGroup, State


class User(StatesGroup):

    phone_number = State()
    tg_id = State()