import sqlite3
def get_leave_balance_by_id(employee_id):
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM LeaveBalance WHERE Id=?", (employee_id,))
    employee = cursor.fetchone()
    conn.close()
    if employee:
        return {
            "Id": employee[0],
            "EarnedLeave": employee[2],
            "CasualLeave": employee[3],
            "SickLeave": employee[4],
        }
    else:
        return None

def get_all_leave_balances():
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM LeaveBalance")
    employees = cursor.fetchall()
    conn.close()
    return employees
