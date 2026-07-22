TEST_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "hello",
            "description": "Return hello",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    }
]
EMPLOYEE_TOOLS = [
     {
        "type": "function",
        "function": {
            "name": "get_employee_by_id",
            "description": """
Returns details of the currently logged-in employee.

Use this tool when the user asks:
- Who am I?
- What is my employee code?
- What is my employee ID?
- Show my profile.
- Tell me my details.

The application automatically provides the logged-in employee ID.
Never ask the user for an employee ID.
""",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_all_employees",
            "description": "Get a list of all employees",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    
    
]

LEAVE_TOOLS = [
        {
    "type": "function",
    "function": {
        "name": "get_leave_balance_by_id",
        "description": """
Returns the leave balance of the currently logged-in employee.

Use this tool when the user asks:
- What is my leave balance?
- Show my leave balance.
- How many leaves do I have?
- How many casual leaves do I have?
- How many sick leaves do I have?
- How many earned leaves do I have?
- Do I have any leaves remaining?
- Check my leave balance.

The application automatically provides the logged-in employee ID.
Never ask the user for an employee ID.
Never generate an employee ID.
""",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    }
},
     {
        "type": "function",
        "function": {
            "name": "get_all_leave_balances",
            "description": "Get a list of leave balances for all employees",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
]
LEAVE_POLICY_TOOLS = [
    {
    "type": "function",
    "function": {
        "name": "search_leave_policy",
        "description": """
Search the company's leave policy.

Use this tool ONLY when the user asks about:

- leave policy
- earned leave
- maternity leave
- paternity leave
- leave encashment
- carry forward leave
- casual leave
- sick leave
- work from home policy
- leave rules
""",
        "parameters": {
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": "The user's question about the leave policy"
                }
            },
            "required": ["question"]
        }
    }
}
]
GRATUITY_POLICY_TOOLS = [
   {
        "type": "function",
        "function": {
            "name": "search_gratuity_policy",
            "description": "Search gratuity policy.",
            "parameters": {
                "type": "object",
                "properties": {
                    "question": {
                        "type": "string"
                    }
                },
                "required": ["question"]
            }
        }
    }
]
