from pydantic import BaseModel, EmailStr, validator
from app import util

__all__ = ['Login', 'LoginResponse']

class Login(BaseModel):
    username: str
    password: str

    _normalize_nome = validator("username", allow_reuse=True)(util.normalize_lower)


class LoginResponse(BaseModel):
    token: str
    user: str

    class Config:
        orm_mode = True
