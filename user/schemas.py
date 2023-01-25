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
    last_name: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_model = True

class UserInDb(BaseModel):
    first_name: str
    last_name: str | None = None
    email: EmailStr
    hashed_password: str

    class Config:
        orm_model = True
