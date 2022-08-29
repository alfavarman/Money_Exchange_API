from datetime import date

from external_api_service import get_currency_rate_from_nbp
from models import Currate
from settings import db


class MoneyService:
    def __init__(self, currency_1: str, currency_2: str, amount: str):
        self.currency_1 = currency_1
        self.currency_2 = currency_2
        self.amount = amount

    def get_rate_from_db(self, currency_code: str) -> float:
        rate = (
            db.session.query(Currate.rate)
            .filter((Currate.code == currency_code) & (Currate.date == date.today()))
            .first()
        )
        return rate[0] if rate else None

    def insert_rate_to_db(self, code: str, rate: float) -> None:
        rate_cur = Currate(code=code, rate=rate, date=date.today())
        db.session.add(rate_cur)
        db.session.commit()

    def find_rate(self, currency_code: str) -> float:
        currency_code = currency_code.upper()
        if currency_code == "PLN":
            return 1
        rate = get_currency_rate_from_nbp(currency_code)
        return rate

    def get_rate(self, currency_code: str) -> float:
        rate = self.get_rate_from_db(currency_code)
        if not rate:
            rate = self.find_rate(currency_code)
            self.insert_rate_to_db(code=currency_code, rate=rate)
        return rate

    def get_exchange_rate(self) -> float:
        rate_1 = self.get_rate(self.currency_1)
        rate_2 = self.get_rate(self.currency_2)
        return rate_1 / rate_2

    def get_money_exchange(self) -> float:
        exchange_rate = self.get_exchange_rate()
        result = float(exchange_rate) * float(self.amount)
        return result
