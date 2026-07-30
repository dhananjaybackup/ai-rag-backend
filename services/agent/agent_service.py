from ast import arguments
import json
from pyexpat.errors import messages
from xml.parsers.expat import model

from httpcore import request
from openai import models

# from asyncio import tools
from models.chat_models import ChatRequest
from prompts.system_prompt import SYSTEM_PROMPT

from services.llm.llm_service import LLMService
from services.agent.memory_service import MemoryService
from services.agent.tool_executor import ToolExecutor

from services.agent.tool_router import ToolRouter
from tools.employee_tools import get_employee_by_id
from tools.tool_registry import EMPLOYEE_TOOLS, GRATUITY_POLICY_TOOLS, LEAVE_POLICY_TOOLS

class Role:
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"

AUTHENTICATED_TOOLS = {
    "get_employee_by_id",
    "get_leave_balance_by_id",
}

class AgentService:
    def __init__(self):
        self.llm_service = LLMService()
        self.tool_executor = ToolExecutor()
        self.memory_service = MemoryService()
        self.tool_router = ToolRouter()

    def chat1(self, user_message):
        # Process the request using the LLM service
        # response = self.llm_service.first_call(request)
        # return response
        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_message
            }
        ]

        response = self.llm_service.first_call(
            messages,
            EMPLOYEE_TOOLS
        )
        message = response.choices[0].message
        print("LLM Response:", message.content)
    # --------------------------------------------------
    # CASE 1 : No tool required
    # --------------------------------------------------
        if not message.tool_calls:
         print("No tool required")
         return {
            "response": message.content
         }
    # --------------------------------------------------
    # CASE 2 : Tool required
    # --------------------------------------------------
        tool_call = message.tool_calls[0]
        print("Tool Selected:", tool_call.function.name)
        arguments = json.loads(tool_call.function.arguments)
        print("Arguments:", arguments)
        tool_result = self.tool_executor.execute(tool_call.function.name, arguments)
        print("Tool Result:", tool_result)
        messages.append(message)
        messages.append(
        {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": json.dumps(tool_result)
        })


    # --------------------------------------------------
    # Second LLM call
    # --------------------------------------------------
        final_response = self.llm_service.second_call(messages)
        return {
                "response": final_response.choices[0].message.content
            }

        # return {
        #     "response":
        #     tool_result
        # }

    def chat(self, request: ChatRequest):
        messages = [
            {
                "role": Role.SYSTEM,
                "content": SYSTEM_PROMPT
            }
        ]
        # models = self.client.models.list()
        # for model in models.data:
        #     print(model.id)
      
        history = self.memory_service.get_history(
                     request.sessionId
                    )
        
        messages.extend(history)

        messages.append(
            {
                "role":Role.USER,
                "content":request.message
            }
        )
        question = request.message.lower()
        employee_id = request.employeeId
        print(f"Employee ID: {employee_id}, Question: {question}")
        # if "leave policy" in question:
        #     tools = [POLICY_TOOL]

        # elif "leave" in question:
        #     tools = LEAVE_TOOLS

        # elif "employee" in question or "who am i" in question:
        #     tools = EMPLOYEE_TOOLS

        # else:
        #     tools = None
        tools = self.tool_router.get_tools(question)
        response = self.llm_service.first_call(messages, tools)
        assistant_message = response.choices[0].message
        final_answer = ""
        # print("=" * 50)
        # print("Assistant Content:", assistant_message.content)
        # print("Tool Calls:", assistant_message.tool_calls)
        # print("=" * 50)
        # --------------------------------------------------
    # CASE 1 : No tool required
    # --------------------------------------------------
        if not assistant_message.tool_calls:
            final_answer = assistant_message.content
            print("No tool required")
        else:
        #  return {
        #     "response": assistant_message.content
        #  }
    # --------------------------------------------------
    # CASE 2 : Tool required
    # --------------------------------------------------
        # this is for single tool routing, if you want to route to multiple tools then you can use the below code
            # tool_call = assistant_message.tool_calls[0]
       # this code is for multiple tool routing, if you want to route to single tool then you can use the above code
            print("Reached CASE 2")
            messages.append(assistant_message)
            for tool_call in assistant_message.tool_calls:
                raw_arguments = tool_call.function.arguments
                try:
                    arguments = json.loads(raw_arguments) if raw_arguments else {}
                except json.JSONDecodeError:
                    arguments = {}
                arguments = arguments or {}    
                print(f"Selected Tool: {tool_call.function.name}")
                print(f"Arguments from LLM: {arguments}")
                # print("Arguments:", )
                if tool_call.function.name in AUTHENTICATED_TOOLS:
                    arguments["employee_id"] = request.employeeId

                    print("Final Arguments:", arguments)

                tool_result = self.tool_executor.execute(tool_call.function.name, arguments)
                print("Tool Result:", tool_result)
                # messages.append(assistant_message)
                messages.append(
                {
                "role": Role.TOOL,
                "tool_call_id": tool_call.id,
                "content": json.dumps(tool_result)
                })
                # --------------------------------------------------
                # Second LLM call
                # --------------------------------------------------
            final_response = self.llm_service.second_call(messages)
            # return {
            #         "response": final_response.choices[0].message.content
            #     }
            final_answer = final_response.choices[0].message.content

        self.memory_service.save_message(
            request.sessionId,
            Role.USER,
            request.message
        )

        self.memory_service.save_message(
            request.sessionId,
            Role.ASSISTANT,
            final_answer
        )
        return {
    "response": final_answer
    }

    def chatAgentLoop(self, request: ChatRequest):
        messages = [
            {
                "role": Role.SYSTEM,
                "content": SYSTEM_PROMPT
            }
        ]
        history = self.memory_service.get_history(
                     request.sessionId
                    )
        messages.extend(history)
        messages.append(
            {
                "role":Role.USER,
                "content":request.message
            }
        )
        question = request.message.lower()
        employee_id = request.employeeId

        print(f"Employee ID: {employee_id}, Question: {question}")

        tools = self.tool_router.get_tools(question)
        while True:

            response = self.llm_service.first_call(messages, tools)
            assistant_message = response.choices[0].message
            final_answer = ""
            # --------------------------------------------------
            # CASE 1 : No tool required
            # --------------------------------------------------
            if not assistant_message.tool_calls:
                messages.append({
                    "role": Role.ASSISTANT,
                    "content": assistant_message.content
                })
                final_answer = assistant_message.content
                print("No tool required")
                break
            else:
       
                print("Reached CASE 2")
                messages.append(assistant_message)
                for tool_call in assistant_message.tool_calls:
                    raw_arguments = tool_call.function.arguments
                    try:
                        arguments = json.loads(raw_arguments) if raw_arguments else {}
                    except json.JSONDecodeError:
                        arguments = {}
                    arguments = arguments or {}    
                    print(f"Selected Tool: {tool_call.function.name}")
                    print(f"Arguments from LLM: {arguments}")
                    # print("Arguments:", )
                    if tool_call.function.name in AUTHENTICATED_TOOLS:
                        arguments["employee_id"] = request.employeeId

                        print("Final Arguments:", arguments)

                    tool_result = self.tool_executor.execute(tool_call.function.name, arguments)
                    print("Tool Result:", tool_result)
                # messages.append(assistant_message)
                    messages.append(
                    {
                    "role": Role.TOOL,
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(tool_result)
                    })
              
          
            # final_answer = response.choices[0].message.content

        self.memory_service.save_message(
                request.sessionId,
                Role.USER,
                request.message
           )

        self.memory_service.save_message(
                request.sessionId,
                Role.ASSISTANT,
                final_answer
        )
        return {
        "response": final_answer
        }