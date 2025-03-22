from fastapi import APIRouter, HTTPException
from ..models.ai_models import ChatRequest, SinglePromptRequest, AIResponse
from ..core.ai_service import ai_service

router = APIRouter()

@router.post('/chat', response_model=AIResponse)
async def chat_with_history(request: ChatRequest):
    try:
        response = await ai_service.generate_with_chat_history(
            messages=[msg.dict() for msg in request.messages],
            system_prompt=request.system_prompt
        )
        return AIResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/generate', response_model=AIResponse)
async def generate_response(request: SinglePromptRequest):
    try:
        response = await ai_service.generate_response(request.prompt)
        return AIResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
