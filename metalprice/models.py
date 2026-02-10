from pydantic import BaseModel

class MetalParams(BaseModel):
    timeperiod: str = "3Y"
