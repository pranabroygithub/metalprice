from get_metal_price import get_metal_price_history
from utils import get_price_in_inr
from models import MetalParams
from loggers import LOGGING_CONFIG
from dotenv import load_dotenv
import json
import logging
from fastapi import FastAPI, Query
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
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("metal_price_logger")

@app.get("/getmetalpricehistory")
def get_metal_price_history_in_inr(params: MetalParams = Query())-> list:
    price_list_per_day = json.loads(get_metal_price_history(params))
    if params.currency_type == 'usd':
        return price_list_per_day
    if params.currency_type == 'inr':
        return get_price_in_inr(price_list_per_day)
    return None
