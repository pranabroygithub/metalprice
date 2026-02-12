from pydantic import BaseModel

class MetalParams(BaseModel):
    timeperiod: str = "1Y"
    currency_type: str = "inr"
    metal_type: str = "XAU"
