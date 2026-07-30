from fastapi import APIRouter, HTTPException
from models.chat_models import ChatRequest
from services.agent.agent_service import AgentService

router = APIRouter()
_service = AgentService()

@router.post("/chat")
async def chat_endpoint(chat_request: ChatRequest):
    print(f"Received chat request: {chat_request.message}")
    # return _service.chat(chat_request)
    return _service.chatAgentLoop(chat_request)