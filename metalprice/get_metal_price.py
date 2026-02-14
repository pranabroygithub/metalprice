import requests
import os
from utils import get_time_period
from models import MetalParams
import logging
import json

logger = logging.getLogger("metal_price_logger")

def get_metal_price_history(params: MetalParams) -> list[dict]:
    url = "https://api.gold-api.com/history"
    api_key = os.getenv("API_KEY")

    start_time, end_time = get_time_period(params.timeperiod)
    metal_type = params.metal_type
    logger.info(f"start time: {start_time} - end time: {end_time}")
    query_params = {
            "symbol" : metal_type,
            "startTimestamp" : start_time,
            "endTimestamp" : end_time,
            "groupBy" : "day"
        }
    headers = {
            "x-api-key" : api_key
        }

    # call the API
    r = requests.get(url, params=query_params, headers=headers)
    # converting max_price which are strings into float number
    return list(map(lambda d: {"day" : d.get("day"), "max_price": float(d.get("max_price"))}, json.loads(r.text)))
