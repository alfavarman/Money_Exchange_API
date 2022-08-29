from settings import db
from models import Currate
from datetime import date


class DatabaseService:
    def __init__(self, currency_code: str):
        self.currency_code = currency_code

    def get_rate(self) -> float:
        rate = (
            db.session.query(Currate.rate)
            .filter((Currate.code == self.currency_code) & (Currate.date == date.today()))
            .first()
        )
        return rate[0] if rate else None

    def insert_rate(self, rate: float) -> None:
        rate_cur = Currate(currency_code=self.currency_code, rate=rate, date=date.today())
        db.session.add(rate_cur)
        db.session.commit()
        db.session.close()
