from pydantic import BaseModel, EmailStr
import sqlite3
from sympy import content

from models.employee import Employee
from services.auth.auth import hash_password

class EmployeeService:
    def get_employee_by_email(self, email: str):
        conn = sqlite3.connect("employee.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT Id, Name, EmployeeCode, Email, Password, Role FROM Employee WHERE Email = ?", (email,)
        )
        row = cursor.fetchone()
        conn.close()
        print(f"Retrieved employee: {row}")
        if row:
            return {
                "id": row[0],
                "name": row[1],
                "empcode": row[2],
                "email": row[3],
                "password": row[4],
                "role": row[5]
            }
        return None
    
    def register_employee(self,employee: Employee):
        conn = sqlite3.connect("employee.db")
        cursor = conn.cursor()
        try:
            hashed = hash_password(employee.password)
            print(f"Registering employee: {employee.name}, Email: {employee.email}, Hashed Password: {hashed}") 
            cursor.execute(
                "INSERT INTO Employee (Name, EmployeeCode, Email, Password, Role) VALUES (?, ?, ?, ?, ?)",
                (employee.name, employee.empcode, employee.email, hashed, employee.role),
            )
            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            raise ValueError("Email already registered")
        
        conn.close()


