from pydantic import BaseModel, EmailStr


class Employee(BaseModel):
    name: str
    empcode: str
    email: EmailStr
    password: str
    role: str

class LoginRequest(BaseModel):
    email:EmailStr
    password:str

