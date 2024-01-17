
from aiogram.fsm.context import FSMContext

from app.tgbot.states import User

async def new_user(state: FSMContext):
    phone_num = state.get_state(User.phone_number)
