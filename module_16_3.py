from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/")
def read_root():
    return "Главная страница"

@app.get("/user/admin")
def read_admin():
    return "Вы вошли как администратор"

@app.get("/users")
def get_users():
    return users

@app.post("/user/{username}/{age}")
def create_user(
    username: Annotated[str, Path(title="Enter username", min_length=5, max_length=20, examples={"example": "UrbanUser"})],
    age: Annotated[int, Path(title="Enter age", ge=18, le=120, examples={"example": 24})]
):
    user_id = str(max(map(int, users.keys())) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
def update_user(
    user_id: Annotated[int, Path(title="Enter User ID", ge=1, le=100, examples={"example": 1})],
    username: Annotated[str, Path(title="Enter username", min_length=5, max_length=20, examples={"example": "UrbanProfi"})],
    age: Annotated[int, Path(title="Enter age", ge=18, le=120, examples={"example": 28})]
):
    user_id = str(user_id)
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"The user {user_id} is updated"
    else:
        return f"User {user_id} not found"

@app.delete("/user/{user_id}")
def delete_user(user_id: Annotated[int, Path(title="Enter User ID", ge=1, le=100, examples={"example": 2})]):
    user_id = str(user_id)
    if user_id in users:
        del users[user_id]
        return f"User {user_id} has been deleted"
    else:
        return f"User {user_id} not found"
