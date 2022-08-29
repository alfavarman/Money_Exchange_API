from external_api_service import get_currency_rate
from settings import db
from datetime import date
from models import Currate


class MoneyService:
    def __init__(self, currency_1: str, currency_2: str, amount: str):
        self.currency_1 = currency_1
        self.currency_2 = currency_2
        self.amount = amount

    def get_rate_from_db(self, currency_code: str) -> float:
        rate = (
            db.session.query(Currate.rate)
            .filter((Currate.code == currency_code) | (Currate.date == date.today()))
            .first()
        )
        return rate[0] if rate else None

    def insert_rate_to_db(self, currency_code: str) -> float:
        if currency_code == "pln".upper():
            return 1
        else:
            ratelist = get_currency_rate(currency_code.upper())
            rate_cur = Currate(code=currency_code, rate=ratelist[0], date=ratelist[1])
            db.session.add(rate_cur)
            db.session.commit()
            rate = ratelist[0]
            return rate

    def get_rate(self, currency_code: str) -> float:

        rate = self.get_rate_from_db(currency_code)
        if not rate:
            rate = self.insert_rate_to_db(currency_code)
        return rate

    def get_exchange_rate(self) -> float:
        rate_1 = self.get_rate(self.currency_1)
        rate_2 = self.get_rate(self.currency_2)
        return rate_1 / rate_2

    def get_money_exchange(self) -> float:
        exchange_rate = self.get_exchange_rate()
        result = float(exchange_rate) * float(self.amount)
        return result
