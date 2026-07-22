from pydantic import BaseModel
class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    sessionId: str
    employeeId: int
    message: str