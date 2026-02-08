from get_metal_price import get_gold_price_history
from utils import get_price_in_inr
from dotenv import load_dotenv
import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.com",
    "https://localhost.com",
    "http://localhost",
    "http://localhost:5173",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()

@app.get("/getgoldpricehistory")
def get_price_history():
    return get_gold_price_history()


@app.get("/getgoldpricehistoryininr")
def get_gold_price_history_in_inr():
    price_list_per_day = json.loads(get_gold_price_history())
    return get_price_in_inr(price_list_per_day)
