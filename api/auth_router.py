from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from models.employee import Employee
from services.auth_service import AuthService

router = APIRouter()
auth_service = AuthService()

class LoginPayload(BaseModel):
    email: EmailStr
    password: str

@router.post("/login")
async def login_endpoint(payload: LoginPayload):
    print(f"Login attempt for email: {payload.email}")
    return auth_service.login(payload.email, payload.password)

@router.post("/register")
async def register_endpoint(employee: Employee):
    # Implement registration logic here
    try:
        auth_service.employee_service.register_employee(employee)
        return {"message": "Employee registered successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    