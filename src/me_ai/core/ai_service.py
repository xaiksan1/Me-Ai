from ..core.config import settings
import openai

class AIService:
    def __init__(self):
        openai.api_key = settings.OPENAI_API_KEY

    async def generate_response(self, prompt: str) -> str:
        try:
            response = await openai.ChatCompletion.acreate(
                model=settings.MODEL_NAME,
                messages=[
                    {'role': 'system', 'content': 'You are a helpful AI assistant.'},
                    {'role': 'user', 'content': prompt}
                ],
                max_tokens=settings.MAX_TOKENS,
                temperature=settings.TEMPERATURE
            )
            return response.choices[0].message.content
        except Exception as e:
            return f'Error generating response: {str(e)}'

ai_service = AIService()
