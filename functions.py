import json
from json import JSONDecodeError

import requests

import settings as s


def get_currency_rate(currency_code: str) -> float:
    if currency_code.lower() == "pln":
        return 1
    try:
        response = requests.get(f"{s.CONSTANT1}{currency_code}/")
        currency_rate = json.loads(response.text)["rates"][0]["mid"]
        return currency_rate
    except JSONDecodeError:
        raise Exception("Wrong Currency Code, try again")


def get_exchange_rate(currency_1_rate: str, currency_2_rate: str) -> float:
    rate_1 = get_currency_rate(currency_1_rate)
    rate_2 = get_currency_rate(currency_2_rate)
    return rate_1 / rate_2


def get_money_exchange(currency_1: str, currency_2: str, amount: float) -> float:
    exchange_rate = get_exchange_rate(currency_1, currency_2)
    try:
        result = float(exchange_rate) * amount
        return result
    except ValueError:
        raise Exception("amount must be a number")
