import unittest
from unittest import TestCase
from unittest.mock import patch

from app import app


class AppTestCase(TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_currency_exchange_api_wrong_parameters(self):
        result = self.client.get("/", query_string={"curr1": "rrr", "curr2": "kkk", "amount": "100"})
        assert result.status_code == 400
        assert result.text == '{"error":"Wrong Currency1 Code, Wrong Currency2 Code"}\n'

    @patch("services.money_service.DatabaseService.get_rate")
    def test_currency_exchange_api_correct_response(self, mocked_get_rate):
        mocked_get_rate.side_effect = [44.21, 7.9]
        result = self.client.get("/", query_string={"curr1": "USD", "curr2": "PLN", "amount": "100"})
        assert result.status_code == 200
        assert result.text.strip() == '{"PLN":559.62}'

    @patch("services.money_service.DatabaseService", return_value="fkp")
    def test_currency_exchange_api_Exception(self, *_):
        result = self.client.get("/", query_string={"curr1": "FKP", "curr2": "PLN", "amount": "100"})
        assert result.text.strip() == """{"error":"'str' object has no attribute 'get_rate'"}"""


if __name__ == "__main__":
    unittest.main()
