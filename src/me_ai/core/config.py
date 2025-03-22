from pydantic import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str = ''
    MODEL_NAME: str = 'gpt-3.5-turbo'
    MAX_TOKENS: int = 150
    TEMPERATURE: float = 0.7

    class Config:
        env_file = '.env'

settings = Settings()
