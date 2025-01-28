from fastapi import FastAPI
from app.routers import task, user
from app.models import Base, User, Task
from app.models.db import engine

# Создание всех таблиц
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)


