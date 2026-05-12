import requests
import os
from dotenv import load_dotenv
from app.db import init_db, save_company, save_director

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

def load_all_data():
    init_db()
    data = fetch_all_stocks()
    directors = fetch_directors()
    
    for stock in data["stocks"]:
        save_company(
            stock["symbol"],
            stock['company_name'],
            stock["market"],
            stock.get["sector", ""],
            stock.get["closing_price", 0],
            stock["[pe-ratio]", 0]
        )

        for director in directors:
            save_director(
                director["symbol"],
                director["name"],
                director.get["title", ""],
                director.get["director_type", ""]
            )

                
            
    

