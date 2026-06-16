from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    email: EmailStr


class PostSchema(BaseModel):
    title: str = Field(min_length=3, max_length=50)
    description: str = Field(min_length=5, max_length=200)
