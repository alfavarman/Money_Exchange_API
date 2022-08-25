import json

import requests

import settings as s


class ExternalApiService:
    default_currency = "pln"

    def get_currency_rate(self, currency_code: str) -> list:
        if currency_code.lower() == self.default_currency:
            lista = [1]
            return lista

        response = requests.get(f"{s.CONSTANT1}{currency_code}/")
        currency_rate = json.loads(response.text)["rates"][0]["mid"]
        rate_date = json.loads(response.text)["rates"][0]["effectiveDate"]
        rate = [currency_rate, rate_date]
        return rate
