import json
from json import JSONDecodeError

import requests

import settings as s
from iso42 import country_codes as codes


class ExternalApiService:
    default_currency = "pln"

    def get_currency_rate(self, currency_code: str) -> float:
        if currency_code.lower() == self.default_currency:
            return 1

        response = requests.get(f"{s.CONSTANT1}{currency_code}/")
        currency_rate = json.loads(response.text)["rates"][0]["mid"]
        return currency_rate


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
        result = float(exchange_rate) * float(self.amount)
        return result


class Validator:
    def __init__(self, currency_1: str, currency_2: str, amount: str):
        self.currency_1 = currency_1
        self.currency_2 = currency_2
        self.amount = amount
        self.error = []

    def is_valid(self) -> bool:
        if self.currency_1.upper() not in codes:
            self.error.append('Wrong Currency1 Code')

        if self.currency_2.upper() not in codes:
            self.error.append('Wrong Currency2 Code')

        if float(self.amount) < 0:
            self.error.append('Amount must be a positive number')

        return len(self.error) == 0
