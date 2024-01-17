from aiogram import Dispatcher

from .commands import router as command_router
# from .callbacks import router as callbacks_router

def setup(dp: Dispatcher) -> None:
    dp.include_router(router=command_router)
    # dp.include_router(router=callbacks_router)
