from uuid import UUID

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from blog import models as BlogModels, models
from blog.schemas import BlogSchema
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


@app.post("/blog")
async def create_blog(request: BlogSchema, db: Session = Depends(get_db)):
    blog = models.Blog(title=request.title, description=request.description)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


class Customer(BaseModel):
    guid: UUID
    name: str
    company: str


@app.post("/api/customer")
async def create_customer(customer: Customer):
    data = customer
    return customer
