from pydantic import BaseModel, EmailStr


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

    class Config:
        orm_model = True
