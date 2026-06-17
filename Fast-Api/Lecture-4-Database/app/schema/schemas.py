from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password:str=Field(min_length=8, max_length=25)


class PostSchema(BaseModel):
    title: str = Field(min_length=3, max_length=50)
    description: str = Field(min_length=5, max_length=200)
    category_id:str
    user_id:str
