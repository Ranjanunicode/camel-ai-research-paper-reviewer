import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

SEMANTIC_SCHOLAR_API_KEY = os.getenv("SEMANTIC_SCHOLAR_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")