from uuid import uuid4, UUID

from pydantic import BaseModel
from datetime import datetime


class BlogSchema(BaseModel):
    title: str
    description: str

    class Config:
        schema_extra = {
            "example": {
                "title": "Blog Title 1",
                "description": "Blog description here"
            }
        }


class BlogResponseSchema(BaseModel):
    title: str
    description: str

    class Config:
        schema_extra = {
            "example": {
                "title": "Blog Title 1",
                "description": "Blog description here"
            }
        }
        orm_mode = True


class AllBlogResponseSchema(BlogResponseSchema):
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        schema_extra = {
            "example": {
                "title": "Blog Title 1",
                "description": "Blog description here",
                "created_at": "2023-01-20 10:03:58.153382+00",
                "updated_at": "2023-01-20 10:03:58.153382+00"
            }
        }
        orm_mode = True
