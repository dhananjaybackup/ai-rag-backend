import sqlite3
def get_employee_by_id(employee_id):
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Employee WHERE Id=?", (employee_id,))
    employee = cursor.fetchone()
    conn.close()
    if employee:
        return {
            "Id": employee[0],
            "Name": employee[1],
            "EmployeeCode": employee[2]
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
            "Id": employee[0],
            "Name": employee[1],
            "EmployeeCode": employee[2],
            "Email": employee[3],
            "Role": employee[5],
            "ManagerId": employee[6]
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
