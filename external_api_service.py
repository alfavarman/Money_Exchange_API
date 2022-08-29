import json

import requests

import settings


def get_currency_rate_from_nbp(currency_code: str) -> float:
    response = requests.get(f"{settings.CONSTANT1}{currency_code}/")
    rate = json.loads(response.text)["rates"][0]["mid"]
    return rate
