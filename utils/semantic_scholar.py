import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SEMANTIC_SCHOLAR_API_KEY")
HEADERS = {"x-api-key": API_KEY}
BASE_URL = "https://api.semanticscholar.org/graph/v1/paper/search"


def search_papers_by_claim(claim_text, limit=3):
    """Search for papers that support a specific claim"""
    params = {
        "query": claim_text,
        "fields": "title,authors,url,abstract,year",
        "limit": limit
    }
    try:
        res = requests.get(BASE_URL, headers=HEADERS, params=params)
        res.raise_for_status()
        return res.json().get("data", [])
    except Exception as e:
        print(f"[Semantic Scholar Error]: {e}")
        return []
