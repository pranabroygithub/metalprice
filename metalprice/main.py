from get_metal_price import get_gold_price_history
from utils import get_price_in_inr
from dotenv import load_dotenv

from fastapi import FastAPI

app = FastAPI()
load_dotenv()

@app.get("/getgoldpricehistory")
def get_price_history():
    return get_gold_price_history()


@app.get("/getgoldpricehistoryininr")
def get_gold_price_history_in_inr():
    price_list_per_day = get_gold_price_history()
    return get_price_in_inr(price_list_per_day)
