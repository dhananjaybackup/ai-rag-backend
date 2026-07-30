from fastapi import APIRouter, HTTPException
from models.chat_models import ChatRequest
from services.chat_service import ChatService

router = APIRouter()
chat_service = ChatService()

@router.post("/chat")
async def chat_endpoint(chat_request: ChatRequest):
    print(f"Received chat request: {chat_request.message}")
    # return chat_service.chat(chat_request)
    return chat_service.chatAgentLoop(chat_request)