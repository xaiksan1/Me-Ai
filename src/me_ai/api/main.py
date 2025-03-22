from fastapi import FastAPI
from .endpoints import router

app = FastAPI(
    title='Me-Ai',
    description='An AI-powered personal assistant',
    version='0.1.0'
)

app.include_router(router, prefix='/api/v1')
