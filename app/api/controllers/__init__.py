from fastapi import FastAPI
from .user import router as user_router
from .todo import router as todo_router
from .authentication import router as authentication_router

def setup(app: FastAPI) -> None:
    app.include_router(
        router=authentication_router,
        tags=["authentication"]
    )
    app.include_router(
        router=user_router,
        tags=["user"]
    )
    app.include_router(
        router=todo_router,
        tags=["todo"]
    )

