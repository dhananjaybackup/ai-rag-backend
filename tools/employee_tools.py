import sqlite3
def get_employee_by_id(employee_id):
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Employee WHERE Id=?", (employee_id,))
    employee = cursor.fetchone()
    conn.close()
    if employee:
        return {
            "employee_id": employee[0],
            "name": employee[1],
            "employee_code": employee[2],
            "email": employee[3],
            "role": employee[4],
            "manager_id": employee[6]
        }
    else:
        return None

def get_employee_details(employee_id: int):
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Employee WHERE Id=?", (employee_id,))
    employee = cursor.fetchone()
    conn.close()
    if employee:
        return {
            "employee_id": employee[0],
            "name": employee[1],
            "employee_code": employee[2],
            "email": employee[3],
            "role": employee[4],
            "manager_id": employee[6]
        }
    else:
        return None

def get_all_employees():
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Employee")
    employees = cursor.fetchall()
    conn.close()
    return employees
