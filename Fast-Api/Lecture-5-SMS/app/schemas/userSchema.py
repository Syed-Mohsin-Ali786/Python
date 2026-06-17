from pydantic import BaseModel,Field,EmailStr

class UserRegisterSchema(BaseModel):
    name:str=Field(min_length=5,max_length=20,examples=["user"])
    email:EmailStr=Field(examples=["user@gmail.com"])
    password:str=Field(min_length=8,max_length=25,examples=["1234fssdf4wdfk@%"])