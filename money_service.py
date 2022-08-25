from external_api_service import ExternalApiService
import psycopg2
from datetime import date


class MoneyService(ExternalApiService):
    def __init__(self, currency_1: str, currency_2: str, amount: str):
        self.currency_1 = currency_1
        self.currency_2 = currency_2
        self.amount = amount

    def get_db_rate(self, currency_code) -> float:
        conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="password",
            host="127.0.0.1",
            port="5432",
        )
        conn.autocommit = True
        cursor = conn.cursor()
        # ?? Creating database
        # cursor.execute("CREATE DATABASE IF NOT EXISTS rates ") #TODO deb
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS "
            "currate("
            "code VARCHAR, "
            "rate FLOAT, "
            "date DATE)"
        )

        ratelist = self.get_currency_rate(currency_code.upper())

        select = f"SELECT rate FROM currate WHERE code='{currency_code.upper()}' AND date='{str(date.today())}'"

        cursor.execute(select)
        result = cursor.fetchone()

        if result is None:
            insert = (
                f"INSERT INTO currate VALUES('{currency_code.upper()}', "
                f"'{ratelist[0]}', "
                f"'{ratelist[1]}') ON CONFLICT DO NOTHING"
            )
            cursor.execute(insert)
            return ratelist[1]
        return float(result[0])


    def get_exchange_rate(self) -> float:
        rate_1 = self.get_db_rate(self.currency_1)
        rate_2 = self.get_db_rate(self.currency_2)
        return float(rate_1) / float(rate_2)

    def get_money_exchange(self) -> float:
        exchange_rate = self.get_exchange_rate()
        result = float(exchange_rate) * float(self.amount)
        return result
