import json

import requests

import settings as s


class ExternalApiService:
    default_currency = "pln"

    def get_currency_rate(self, currency_code: str) -> float:
        if currency_code.lower() == self.default_currency:
            return 1

        response = requests.get(f"{s.CONSTANT1}{currency_code}/")
        currency_rate = json.loads(response.text)["rates"][0]["mid"]
        return currency_rate
