import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from backend.db import engine
from models.user import Base as UserBase
from models.task import Base as TaskBase
from routers.user import router as user_router
from routers.task import router as task_router

app = FastAPI()

# Создание всех таблиц
UserBase.metadata.create_all(bind=engine)
TaskBase.metadata.create_all(bind=engine)

# Подключение маршрутов
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(task_router, prefix="/tasks", tags=["tasks"])
