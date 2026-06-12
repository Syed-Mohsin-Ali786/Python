from pydantic import BaseModel, Field, EmailStr,ConfigDict
from typing import List
from datetime import date


class Gender(BaseModel):
    male = "Male"
    female= "Female"


class Address(BaseModel):
    street: str
    city: str = Field(min_length=3)


class Insurance(BaseModel):
    company: str


class BloodGroup(BaseModel):
    a_neg :str= "A-"
    a_pos :str= "A+"


class Patient(BaseModel):
    name: str = (Field(min_length=3, max_length=50, examples=["Qamar"]),)
    email: EmailStr
    phone: str = Field(min_length=10, max_length=15, examples=["0344-3432432"])
    age: int = Field(gt=0, lt=130)
    gender: Gender
    disease: List[str] = Field(min_length=1)
    is_admitted: bool
    date: date
    address: Address
    blood_group: BloodGroup
    model_config:ConfigDict(extra="forbid")

Patient.model_rebuild()