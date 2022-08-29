from external_api_service import get_currency_rate_from_nbp
from db import DatabaseService


class MoneyService:
    def __init__(self, currency_1: str, currency_2: str, amount: str):
        self.currency_1 = currency_1
        self.currency_2 = currency_2
        self.amount = amount

    def _find_rate(self, currency_code: str) -> float:
        currency_code = currency_code.upper()
        if currency_code == "PLN":
            return 1
        rate = get_currency_rate_from_nbp(currency_code)
        return rate

    def _get_rate(self, currency_code: str) -> float:
        db_service = DatabaseService(currency_code=currency_code)
        rate = db_service.get_rate_from_db()
        if not rate:
            rate = self._find_rate(currency_code)
            db_service.insert_rate_to_db(rate=rate)
        return rate

    def _get_exchange_rate(self) -> float:
        rate_1 = self._get_rate(self.currency_1)
        rate_2 = self._get_rate(self.currency_2)
        return rate_1 / rate_2

    def get_money_exchange(self) -> float:
        exchange_rate = self._get_exchange_rate()
        result = float(exchange_rate) * float(self.amount)
        return result
