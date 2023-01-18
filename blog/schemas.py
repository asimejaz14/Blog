from pydantic import BaseModel
from datetime import datetime


class BlogSchema(BaseModel):
    title: str
    description: str


class BlogResponseSchema(BlogSchema):
    created_at: datetime
    updated_at: datetime
