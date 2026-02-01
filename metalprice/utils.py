

def convert_price(price: float, _from: str, to: str , grams: float) -> float:
    troy_ounce = 31.1034768

    if _from == "USD" and to == "INR":
        return ((price / troy_ounce) * grams ) * 91.69

def get_price_in_inr(price_list_per_day: list) -> list[dict]:
    converted_price_list_per_day = []

    for price_per_day in price_list_per_day:
        day = price_per_day.get("day")
        max_price = float(price_per_day.get("max_price"))
        converted_price = convert_price(max_price, "USD", "INR", 10.0)
        converted_price_list_per_day.append({"day" : day, "max_price": converted_price})
    return converted_price_list_per_day
