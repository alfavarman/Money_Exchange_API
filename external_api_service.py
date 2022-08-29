import json

import requests

import settings as s


def get_currency_rate(currency_code: str) -> list:
    response = requests.get(f"{s.CONSTANT1}{currency_code}/")
    currency_rate = json.loads(response.text)["rates"][0]["mid"]
    rate_date = json.loads(response.text)["rates"][0]["effectiveDate"]
    rate = [currency_rate, rate_date]
    return rate
