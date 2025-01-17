from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    username: str
    firstname: str
    lastname: str
    age: int
    slug: str

    class Config:
        orm_mode = True

class TaskSchema(BaseModel):
    id: int
    title: str
    content: str
    priority: int
    completed: bool
    user_id: int
    slug: str

    class Config:
        orm_mode = True
