# Me-Ai: Personal AI Assistant

A modern AI assistant powered by Google's Gemini AI, built with FastAPI and ready for deployment on Vercel.

## Features

- 🤖 Powered by Google's Gemini AI
- 🚀 Fast and efficient API using FastAPI
- 💬 Support for both single prompts and chat conversations
- 🔄 Maintains chat history
- 📚 Full API documentation (available at /docs)

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/xaiksan1/Me-Ai.git
   cd Me-Ai
   ```

2. Set up your environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Create a .env file:
   ```bash
   cp .env.example .env
   # Add your Google API key to the .env file
   ```

4. Run the development server:
   ```bash
   uvicorn me_ai.api.main:app --reload
   ```

## API Endpoints

- `POST /api/v1/generate`: Generate a response for a single prompt
- `POST /api/v1/chat`: Generate a response with chat history

## Deployment

### Deploy to Vercel

1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Deploy:
   ```bash
   vercel
   ```

3. Set up environment variables in Vercel:
   - Go to your project settings
   - Add GOOGLE_API_KEY with your API key

## Development

Run tests:
```bash
pytest
```

## License

MIT License
