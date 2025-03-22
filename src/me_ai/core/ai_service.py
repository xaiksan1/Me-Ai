import google.generativeai as genai
from ..core.config import settings
from typing import Optional, List

class AIService:
    def __init__(self):
        genai.configure(api_key=settings.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel(settings.MODEL_NAME)

    async def generate_response(self, prompt: str) -> str:
        try:
            response = await self._generate(prompt)
            return response
        except Exception as e:
            return f'Error generating response: {str(e)}'

    async def _generate(self, prompt: str) -> str:
        response = self.model.generate_content(
            prompt,
            generation_config={
                'temperature': settings.TEMPERATURE,
                'max_output_tokens': settings.MAX_OUTPUT_TOKENS,
            }
        )
        return response.text

    async def generate_with_chat_history(
        self, 
        messages: List[dict],
        system_prompt: Optional[str] = None
    ) -> str:
        try:
            chat = self.model.start_chat(
                history=[],
                system_prompt=system_prompt or 'You are a helpful AI assistant.'
            )
            
            for message in messages:
                if message['role'] == 'user':
                    response = chat.send_message(message['content'])
            
            return response.text
        except Exception as e:
            return f'Error in chat generation: {str(e)}'

ai_service = AIService()
