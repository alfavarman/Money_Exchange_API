from external_api_service import ExternalApiService


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
