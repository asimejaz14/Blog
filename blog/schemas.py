from uuid import uuid4, UUID

from pydantic import BaseModel
from datetime import datetime


class BlogSchema(BaseModel):
    title: str
    description: str

    # class Config:
    #     orm_mode = True


class BlogResponseSchema(BlogSchema):
    created_at: datetime
    # updated_at: datetime
