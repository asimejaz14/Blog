from typing import List
from uuid import UUID

from fastapi import FastAPI, Depends, status, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

import blog.schemas
from blog import models as BlogModels
from blog.schemas import BlogSchema, BlogResponseSchema, AllBlogResponseSchema
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


@app.post("/blog", status_code=status.HTTP_201_CREATED, response_model=BlogResponseSchema)
async def create_blog(request: BlogSchema, db: Session = Depends(get_db)):
    blog = BlogModels.Blog(title=request.title, description=request.description)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


@app.get("/blog", status_code=status.HTTP_200_OK, response_model=List[AllBlogResponseSchema], response_model_exclude_none=True)
async def get_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(BlogModels.Blog).all()
    if not blogs:
        raise HTTPException(status_code=404, detail="No blogs found")
    return blogs


@app.get("/blog/{id}", status_code=status.HTTP_200_OK, response_model=AllBlogResponseSchema, response_model_exclude_none=True)
async def get_blog_by_id(id, db: Session = Depends(get_db)):
    blog = db.query(BlogModels.Blog).filter(BlogModels.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail=f"Blog with id: {id} not found")
    return blog


@app.put("/blog/{id}", status_code=status.HTTP_200_OK)
async def updated_blog(id, request: BlogSchema, db: Session = Depends(get_db)):
    blog_ = db.query(BlogModels.Blog).filter(BlogModels.Blog.id == id)
    if not blog_.first():
        raise HTTPException(status_code=404, detail=f"Blog with id: {id} does not exist")
    blog_.update(request.dict())
    db.commit()
    return blog_.first()


@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog_by_id(id, db: Session = Depends(get_db)):
    blog_ = db.query(BlogModels.Blog).filter(BlogModels.Blog.id == id)
    if not blog_.first():
        raise HTTPException(status_code=404, detail=f"Blog with id: {id} does not exist")
    blog_.delete()
    db.commit()

    return
