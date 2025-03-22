from fastapi import APIRouter, HTTPException
from ..models.ai_models import AIRequest, AIResponse
from ..core.ai_service import ai_service

router = APIRouter()

@router.post('/generate', response_model=AIResponse)
async def generate_ai_response(request: AIRequest):
    try:
        response = await ai_service.generate_response(request.prompt)
        return AIResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
