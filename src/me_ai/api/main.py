from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .endpoints import router

app = FastAPI(
    title='Me-Ai',
    description='An AI-powered personal assistant using Google Gemini',
    version='0.1.0'
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # For development - update this for production
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/')
async def root():
    return {
        'message': 'Welcome to Me-Ai - Your Personal AI Assistant',
        'docs_url': '/docs',
        'endpoints': {
            'chat': '/api/v1/chat',
            'generate': '/api/v1/generate'
        }
    }

app.include_router(router, prefix='/api/v1')
