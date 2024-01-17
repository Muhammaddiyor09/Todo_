from aiogram.fsm.context import FSMContext

from app.tgbot.keyboard import tel_raq
from app.tgbot.states import User
from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command(commands=["start"]))
async def on_start(message: types.Message, state: FSMContext) -> None:
    is_registered = False
    if is_registered:
        await message.answer(
            text="salom"
        )
    else:
        await message.answer(
            text="Telefon raqamingizni krting",
            reply_markup=tel_raq(),


        )
        await message.from_user.id

