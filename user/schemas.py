from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserIn(BaseModel):
    first_name: str
    last_name: str | None = None
    email: EmailStr
    password: str

    class Config:
        orm_model = True


class UserOut(BaseModel):
    first_name: str
    last_name: str | None = None
    email: EmailStr
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        orm_model = True
