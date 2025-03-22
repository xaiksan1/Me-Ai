import re
from typing import Dict, Any

def sanitize_input(text: str) -> str:
    # Remove any potentially harmful characters
    return re.sub(r'[^\w\s\-.,?!]', '', text)

def format_response(data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        'status': 'success',
        'data': data,
        'timestamp': 'timestamp'
    }
