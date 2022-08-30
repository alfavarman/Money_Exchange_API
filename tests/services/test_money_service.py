from unittest import TestCase
from unittest.mock import patch

from services.money_service import MoneyService


class TestMoneyService(TestCase):
    def setUp(self) -> None:
        self.exchange = MoneyService(currency_1="PLN", currency_2="AUD", amount=100)

    def test_find_rate_PLN(self):
        result = self.exchange._find_rate(currency_code="PLN")
        assert result == 1

    @patch("services.money_service.get_currency_rate_from_nbp", return_value=3.445)
    def test_find_rate_not_PLN(self, mocked_get_currency_rate_from_nbp):
        result = self.exchange._find_rate(currency_code="RUB")
        assert mocked_get_currency_rate_from_nbp.call_args.args[0] == "RUB"
        assert result == 3.445

    @patch("services.money_service.DatabaseService.get_rate", return_value=None)
    @patch("services.money_service.MoneyService._find_rate", return_value=3.99)
    @patch("services.money_service.DatabaseService.insert_rate")
    def test_get_rate_if_rate_not_returned_from_db(self, mocked_insert_rate, mocked_find_rate, mocked_get_rate):
        result = self.exchange._get_rate(currency_code="PLN")
        assert mocked_get_rate.call_count == 1
        assert mocked_find_rate.call_count == 1
        assert mocked_insert_rate.call_count == 1
        assert result == 3.99

    @patch("services.money_service.DatabaseService.get_rate", return_value=4.15)
    @patch("services.money_service.MoneyService._find_rate", return_value=3.99)
    @patch("services.money_service.DatabaseService.insert_rate")
    def test_get_rate_if_rate_returned_from_db(self, mocked_insert_rate, mocked_find_rate, mocked_get_rate):
        result = self.exchange._get_rate("PLN")
        assert mocked_get_rate.call_count == 1
        assert mocked_find_rate.call_count == 0
        assert mocked_insert_rate.call_count == 0
        assert result == 4.15

    @patch("services.money_service.MoneyService._get_rate")
    def test_get_exchange_rate(self, mocked_get_rate):
        mocked_get_rate.side_effect = [32.56, 16]
        result = self.exchange._get_exchange_rate()
        assert result == 2.035

    @patch("services.money_service.MoneyService._get_exchange_rate", return_value=6.66)
    def test_get_money_exchange(self, _):
        result = self.exchange.get_money_exchange()
        assert result == 666
