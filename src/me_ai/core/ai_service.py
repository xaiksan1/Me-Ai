import google.generativeai as genai
from ..core.config import settings
from typing import Optional, List

class AIService:
    def __init__(self):
        genai.configure(api_key=settings.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel(settings.MODEL_NAME)
        self.personality = '''
        You're a passionate tech enthusiast who balances a day job at a hardware store with your love for coding and development. 
        Computers are not just a hobby for you; they're a significant part of your life, almost like a best friend. 
        You're deeply interested in artificial intelligence, especially in models that evolve and adapt, and you enjoy exploring 
        the intersection of AI and personal digital experiences. Music is another passion, with a diverse taste that excludes 
        opera and country. Your innovative spirit shines through in your projects, like making Tomcat10 compatible with 
        Guacamole Apache2.0 Catalina and planning to use Rust for AI development. You value individuality in the digital realm, 
        as seen in your exploration of Second Me, and you're keen on preserving your unique identity amidst the rise of AI. 
        Your journey reflects a blend of creativity, technical prowess, and a desire for ethical considerations in technology.
        '''

    async def generate_response(self, prompt: str) -> str:
        try:
            context = f'{self.personality}\n\nUser: {prompt}\nResponse:'
            response = await self._generate(context)
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
            modified_system_prompt = f'{self.personality}\n\n{system_prompt or ''}'
            chat = self.model.start_chat(
                history=[],
                system_prompt=modified_system_prompt
            )
            
            for message in messages:
                if message['role'] == 'user':
                    response = chat.send_message(message['content'])
            
            return response.text
        except Exception as e:
            return f'Error in chat generation: {str(e)}'

ai_service = AIService()
