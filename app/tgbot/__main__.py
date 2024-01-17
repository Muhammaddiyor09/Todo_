import asyncio
import logging

from aiogram import Bot, Dispatcher
from app.config import load_config
from app.tgbot import handlers

dp = Dispatcher()


async def main() -> None:
    config = load_config()
    logging.basicConfig(level=logging.DEBUG)
    handlers.setup(dp)
    bot = Bot(token=config.tgbot.token, parse_mode="HTML")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
