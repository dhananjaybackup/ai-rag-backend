from tools.tool_registry import EMPLOYEE_TOOLS, GRATUITY_POLICY_TOOLS, LEAVE_POLICY_TOOLS, LEAVE_TOOLS, TEST_TOOLS

TEST_KEYWORDS = [
    "hello",
    "hi tool",
    "test tool"
]
EMPLOYEE_KEYWORDS = [
    "employee",
    "emp",
    "employee code",
    "employee id",
    "profile",
    "who am i",
    "my details",
    "my code",

    # Manager
    "manager",
    "my manager",
    "manager details",
    "reporting manager",
    "boss",
    "supervisor",
    "report to",
    "lead"
]
LEAVE_KEYWORDS = [
    "leave",
    "leaves",
    "leave balance",
    "my leave",
    "remaining leave",
    "remaining leaves",
    "earned leave",
    "casual leave",
    "sick leave"
]

LEAVE_POLICY_KEYWORDS = [
    "leave policy",
    "leave rule",
    "leave rules",
    "carry forward",
    "encashment",
    "maternity",
    "paternity"
]

GRATUITY_POLICY_KEYWORDS = [
    "gratuity",
    "gratuity policy",
    "continuous service",
    "five years"
]

class ToolRouter:

    def get_tools(self, question):

        question = question.lower()
#  this is for single tool routing, if you want to route to multiple tools then you can use the below code

        # if any(k in question for k in EMPLOYEE_KEYWORDS):
        #     return EMPLOYEE_TOOLS

        # if any(k in question for k in LEAVE_POLICY_KEYWORDS):
        #     return LEAVE_POLICY_TOOLS

        # if any(k in question for k in GRATUITY_POLICY_KEYWORDS):
        #     return GRATUITY_POLICY_TOOLS
        
        # if any(k in question for k in TEST_KEYWORDS):
        #     return TEST_TOOLS
        
        # return None
# for multiple tool routing, if you want to route to single tool then you can use the above code

        tools = []
        if any(k in question for k in EMPLOYEE_KEYWORDS):
            tools.extend(EMPLOYEE_TOOLS)

        if any(k in question for k in LEAVE_KEYWORDS):
            tools.extend(LEAVE_TOOLS)
            
        if any(k in question for k in LEAVE_POLICY_KEYWORDS):
            tools.extend(LEAVE_POLICY_TOOLS)

        if any(k in question for k in GRATUITY_POLICY_KEYWORDS):
            tools.extend(GRATUITY_POLICY_TOOLS)
        
        if any(k in question for k in TEST_KEYWORDS):
            tools.extend(TEST_TOOLS)

        # print("Tools matched:", tools)
        return tools if tools else None
    