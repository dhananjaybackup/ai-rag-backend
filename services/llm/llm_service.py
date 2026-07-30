import json

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GROQL_API_KEY")
MODEL = os.getenv("LLM_MODEL")
class LLMService:

    def __init__(self):
         self.client = OpenAI(
                api_key=API_KEY,
                base_url="https://api.groq.com/openai/v1"
            )
        
    def first_call(self, messages, tools=None):
        print("=" * 60)
        print("MODEL:", MODEL)
        # print("=" * 60)
        # print("MESSAGES")
        # print(messages)

        # print("=" * 60)
        # print("TOOLS")
        # print(tools)
        # print("=" * 80)
        # print(json.dumps(tools, indent=2))
        # print("=" * 80)
        return self.client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=tools
            # tool_choice="auto"
        )

    def second_call(self, messages):
        return self.client.chat.completions.create(
            model=MODEL,
            messages=messages
        )