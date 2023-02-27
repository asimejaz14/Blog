from typing import List

from fastapi import FastAPI, Depends, status, HTTPException, Request
from sqlalchemy.orm import Session

from blog import models as BlogModels
from user import models as UserModels
from blog.schemas import BlogSchema, BlogResponseSchema, AllBlogResponseSchema
from user.hashing import Hash

from database import engine, SessionLocal
from user.schemas import UserIn

BlogModels.Base.metadata.create_all(bind=engine)
UserModels.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Blog APIs")


hasher = Hash()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post(
    "/blog", status_code=status.HTTP_201_CREATED, response_model=BlogResponseSchema
)
async def create_blog(request: BlogSchema, db: Session = Depends(get_db)):
    blog = BlogModels.Blog(title=request.title, description=request.description)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


@app.get(
    "/blog",
    status_code=status.HTTP_200_OK,
    response_model=List[AllBlogResponseSchema],
    response_model_exclude_none=True,
)
async def get_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(BlogModels.Blog).all()
    if not blogs:
        raise HTTPException(status_code=404, detail="No blogs found")
    return blogs


@app.get(
    "/blog/{id}",
    status_code=status.HTTP_200_OK,
    response_model=AllBlogResponseSchema,
    response_model_exclude_none=True,
)
async def get_blog_by_id(id, db: Session = Depends(get_db)):
    blog = db.query(BlogModels.Blog).filter(BlogModels.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail=f"Blog with id: {id} not found")
    return blog


@app.put("/blog/{id}", status_code=status.HTTP_200_OK)
async def updated_blog(id, request: BlogSchema, db: Session = Depends(get_db)):
    blog_ = db.query(BlogModels.Blog).filter(BlogModels.Blog.id == id)
    if not blog_.first():
        raise HTTPException(
            status_code=404, detail=f"Blog with id: {id} does not exist"
        )
    blog_.update(request.dict())
    db.commit()
    return blog_.first()


@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog_by_id(id, db: Session = Depends(get_db)):
    blog_ = db.query(BlogModels.Blog).filter(BlogModels.Blog.id == id)
    if not blog_.first():
        raise HTTPException(
            status_code=404, detail=f"Blog with id: {id} does not exist"
        )
    blog_.delete()
    db.commit()

    return


@app.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: UserIn, db: Session = Depends(get_db)):
    user = UserModels.User(**user.dict(), hashed_password=hasher.get_hash_password(user.password))

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@app.post("/check")
async def check_data(user: UserIn, request: Request):
    print(request)
