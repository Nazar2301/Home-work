from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int

templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users, "user": None})

@app.get("/user/admin")
def read_admin():
    return "Вы вошли как администратор"

@app.get("/users")
def get_users():
    return users

@app.post("/user/{username}/{age}")
def create_user(username: str, age: int):
    user_id = 1 if not users else users[-1].id + 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user

@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")

@app.get("/user/{user_id}")
def read_user(request: Request, user_id: int):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "users": users, "user": user})
    raise HTTPException(status_code=404, detail="User was not found")
