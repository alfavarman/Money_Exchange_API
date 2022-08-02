import json
from json import JSONDecodeError

import requests

import settings as s


class ExternalApiService:
    default_currency = "pln"

    def get_currency_rate(self, currency_code: str) -> float:
        if currency_code.lower() == self.default_currency:
            return 1
        try:
            response = requests.get(f"{s.CONSTANT1}{currency_code}/")
            currency_rate = json.loads(response.text)["rates"][0]["mid"]
            return currency_rate
        except JSONDecodeError:
            raise Exception("Wrong Currency Code, try again")


class MoneyService:
    def __init__(self, currency_1: str, currency_2: str, amount: str):
        self.currency_1 = currency_1
        self.currency_2 = currency_2
        self.amount = amount

    def get_exchange_rate(self) -> float:
        curr_api_service = ExternalApiService()
        rate_1 = curr_api_service.get_currency_rate(self.currency_1)
        rate_2 = curr_api_service.get_currency_rate(self.currency_2)
        return rate_1 / rate_2

    def get_money_exchange(self) -> float:
        exchange_rate = self.get_exchange_rate()
        try:
            result = float(exchange_rate) * float(self.amount)
            return result
        except ValueError:
            raise Exception("amount must be a number")


ex = MoneyService("pln", "usd", 500)

ex2 = MoneyService("aa", "ww", 11)
print(ex.get_money_exchange())
