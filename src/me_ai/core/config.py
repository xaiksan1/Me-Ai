from pydantic import BaseSettings

class Settings(BaseSettings):
    GOOGLE_API_KEY: str = ''
    MODEL_NAME: str = 'gemini-pro'
    TEMPERATURE: float = 0.7
    MAX_OUTPUT_TOKENS: int = 150

    class Config:
        env_file = '.env'

settings = Settings()
