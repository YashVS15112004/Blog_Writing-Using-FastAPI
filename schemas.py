from pydantic import BaseModel
from typing import List, Optional


# Base Blog schema
class Blog(BaseModel):
    title: str
    body: str


class BlogExt(Blog):
    class Config:
        orm_mode = True


class CreateBlog(Blog):
    user_id: int  # Needed for creation


# Base User schema
class User(BaseModel):
    name: str
    email: str
    password: str


class UserCreate(User):
    pass


# ↓↓↓ Used inside BlogOut to avoid circular reference
class UserOutBasic(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True


# ↓↓↓ Full UserOut with blogs list
class UserOut(BaseModel):
    name: str
    email: str
    blogs: List[BlogExt]

    class Config:
        orm_mode = True


# ↓↓↓ Blog response with creator info
class BlogOut(Blog):
    creator: Optional[UserOut]

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username : Optional[str] = None