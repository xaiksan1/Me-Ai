from pydantic import BaseModel
from typing import List, Optional

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    system_prompt: Optional[str] = None

class SinglePromptRequest(BaseModel):
    prompt: str

class AIResponse(BaseModel):
    response: str
