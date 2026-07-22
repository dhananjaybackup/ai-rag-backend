from ast import arguments

from tools.test_tools import hello
from tools.policy_tools import search_gratuity_policy, search_leave_policy
from tools.employee_tools import (
    get_employee_by_id,
    get_all_employees
)
from tools.leave_tools import (
    get_leave_balance_by_id,
    get_all_leave_balances
)

class ToolExecutor:

    def execute(self, tool_name, arguments):
        
        # if tool_name == "get_employee_by_id":
        #     return get_employee_by_id(arguments["employee_id"])

        # elif tool_name == "get_all_employees":
        #     return get_all_employees()

        # else:
        #     raise ValueError(f"Unknown tool: {tool_name}")
    
        try:
            if arguments is not None and not isinstance(arguments, dict):
                raise ValueError("Arguments must be a dictionary or None.")
            TOOLS = {
            "hello": hello,
            "get_employee_by_id": get_employee_by_id,
            "get_all_employees": get_all_employees,
            "get_leave_balance_by_id": get_leave_balance_by_id,
            "get_all_leave_balances": get_all_leave_balances,
            "search_leave_policy": search_leave_policy,
            "search_gratuity_policy": search_gratuity_policy
            }
            if tool_name in TOOLS:
                if arguments:
                    return TOOLS[tool_name](**arguments)
                else:
                    return TOOLS[tool_name]()
            else:
                raise ValueError(f"Unknown tool: {tool_name}")
        except Exception as e:
            return f"Error executing tool '{tool_name}': {str(e)}"
    