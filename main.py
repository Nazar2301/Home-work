from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.models import Base, User, Task
from sqlalchemy.schema import CreateTable




SQLALCHEMY_DATABASE_URL = "sqlite:///./taskmanager.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)

print(CreateTable(User.__table__))
print(CreateTable(Task.__table__))
