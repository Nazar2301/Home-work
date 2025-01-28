from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from models.user import User
from models.task import Task
from schemas.user import CreateUser, UpdateUser
from sqlalchemy import select
from slugify import slugify

router = APIRouter()

@router.get("/")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users

@router.get("/{user_id}")
async def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.scalars(select(User).where(User.id == user_id)).first()
    if user:
        return user
    raise HTTPException(status_code=404, detail="User was not found")

@router.get("/{user_id}/tasks")
async def tasks_by_user_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task).where(Task.user_id == user_id)).all()
    return tasks

@router.post("/create")
async def create_user(user: CreateUser, db: Annotated[Session, Depends(get_db)]):
    new_user = User(
        username=user.username,
        firstname=user.firstname,
        lastname=user.lastname,
        age=user.age,
        slug=slugify(user.username)
    )
    db.add(new_user)
    db.commit()
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}

@router.put("/update/{user_id}")
async def update_user(user_id: int, user: UpdateUser, db: Annotated[Session, Depends(get_db)]):
    existing_user = db.scalars(select(User).where(User.id == user_id)).first()
    if existing_user:
        existing_user.firstname = user.firstname
        existing_user.lastname = user.lastname
        existing_user.age = user.age
        db.commit()
        return {"status_code": status.HTTP_200_OK, "transaction": "User update is successful!"}
    raise HTTPException(status_code=404, detail="User was not found")

@router.delete("/delete/{user_id}")
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    existing_user = db.scalars(select(User).where(User.id == user_id)).first()
    if existing_user:
        db.delete(existing_user)
        db.commit()
        return {"status_code": status.HTTP_200_OK, "transaction": "User deletion is successful!"}
    raise HTTPException(status_code=404, detail="User was not found")
