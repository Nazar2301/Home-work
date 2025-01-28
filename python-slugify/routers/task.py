from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from models.task import Task
from models.user import User
from schemas.task import CreateTask, UpdateTask
from sqlalchemy import select

router = APIRouter()

@router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks

@router.get("/{task_id}")
async def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    task = db.scalars(select(Task).where(Task.id == task_id)).first()
    if task:
        return task
    raise HTTPException(status_code=404, detail="Task was not found")

@router.post("/create")
async def create_task(task: CreateTask, user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.scalars(select(User).where(User.id == user_id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User was not found")
    new_task = Task(
        title=task.title,
        content=task.content,
        priority=task.priority,
        user_id=user_id
    )
    db.add(new_task)
    db.commit()
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}

@router.put("/update/{task_id}")
async def update_task(task_id: int, task: UpdateTask, db: Annotated[Session, Depends(get_db)]):
    existing_task = db.scalars(select(Task).where(Task.id == task_id)).first()
    if existing_task:
        existing_task.title = task.title
        existing_task.content = task.content
        existing_task.priority = task.priority
        db.commit()
        return {"status_code": status.HTTP_200_OK, "transaction": "Task update is successful!"}
    raise HTTPException(status_code=404, detail="Task was not found")

@router.delete("/delete/{task_id}")
async def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    existing_task = db.scalars(select(Task).where(Task.id == task_id)).first()
    if existing_task:
        db.delete(existing_task)
        db.commit()
        return {"status_code": status.HTTP_200_OK, "transaction": "Task deletion is successful!"}
    raise HTTPException(status_code=404, detail="Task was not found")
