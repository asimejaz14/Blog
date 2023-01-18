from uuid import UUID

from fastapi import FastAPI
from pydantic import BaseModel

from blog import models as BlogModels
# from user import models as UserModels
from database import engine, Base, SessionLocal

BlogModels.Base.metadata.create_all(bind=engine)
# UserModels.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/blogs")
async def root():
    return {"message": "Hello World"}


@app.get("/blogs/{blog_title}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


class Customer(BaseModel):
    guid: UUID
    name: str
    company: str


@app.post("/api/customer")
async def create_customer(customer: Customer):
    data = customer
    return customer
