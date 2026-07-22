from fastapi import HTTPException
from passlib.context import CryptContext
from services.auth import create_access_token
from services.employee_service import EmployeeService

class AuthService:
    def __init__(self):
        self.employee_service = EmployeeService()
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def login(self, email: str, password: str):
        user = self.employee_service.get_employee_by_email(email)
        print(user)
        if not user or not self.verify_password(password, user["password"]):
            raise HTTPException(status_code=401, detail="Invalid email or password")

        token = create_access_token({"sub": user["email"],"empcode": user["empcode"], "id": user["id"], "role": user["role"]})
        print(f"Generated token for user {user['email']}: {token}")
        return {"token": token, "token_type": "bearer"}
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)
    