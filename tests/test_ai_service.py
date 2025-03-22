import pytest
from me_ai.core.ai_service import AIService
from me_ai.core.config import settings
from unittest.mock import Mock, patch

@pytest.fixture
def ai_service():
    return AIService()

@pytest.mark.asyncio
async def test_generate_response(ai_service):
    with patch('google.generativeai.GenerativeModel.generate_content') as mock_generate:
        mock_generate.return_value = Mock(text='Test response')
        response = await ai_service.generate_response('Test prompt')
        assert 'Test response' in response

@pytest.mark.asyncio
async def test_generate_with_chat_history(ai_service):
    with patch('google.generativeai.GenerativeModel.start_chat') as mock_chat:
        mock_chat.return_value = Mock(
            send_message=Mock(return_value=Mock(text='Test chat response'))
        )
        messages = [{'role': 'user', 'content': 'Hello'}]
        response = await ai_service.generate_with_chat_history(messages)
        assert response is not None
