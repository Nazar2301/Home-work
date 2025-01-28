import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from backend.db import engine
from models.user import Base
from routers.user import router as user_router

app = FastAPI()

# Создание всех таблиц
Base.metadata.create_all(bind=engine)

# Подключение маршрутов
app.include_router(user_router, prefix="/users", tags=["users"])
