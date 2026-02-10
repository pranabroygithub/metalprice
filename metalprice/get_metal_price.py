import requests
import os
from utils import get_time_period
from models import MetalParams
import logging

logger = logging.getLogger("metal_price_logger")

def get_gold_price_history(params: MetalParams) -> list[dict]:
    url = "https://api.gold-api.com/history"
    api_key = os.getenv("API_KEY")

    start_time, end_time = get_time_period(params.timeperiod)
    logger.info(f"start time: {start_time} - end time: {end_time}")
    query_params = {
            "symbol" : "XAU",
            "startTimestamp" : start_time,
            "endTimestamp" : end_time,
            "groupBy" : "day"
        }
    headers = {
            "x-api-key" : api_key
        }

    # call the API
    r = requests.get(url, params=query_params, headers=headers)
    response = r.text
    return response

