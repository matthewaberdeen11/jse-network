import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("STACKS_API_KEY")
BASE_URL = "https://stacksja.com/api/v1/public"
HEADERS = {"X-API-Key": API_KEY}

def fetch_all_stocks():
    response = requests.get(f"{BASE_URL}/stocks", headers = HEADERS)
    data = response.json()
    return data

def fetch_directors(symbol):
    response = requests.get(f"{BASE_URL}/stock/{symbol}/directors", headers = HEADERS)
    data = response.json()
    return data