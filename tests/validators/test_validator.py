from unittest import TestCase

from validators.validators import Validator


class TestValidator(TestCase):
    def test_all_valid(self):
        validator = Validator(currency_1="usd", currency_2="gbp", amount=100)
        result = validator.is_valid()
        assert result is True

    def test_currency_1_not_valid(self):
        validator = Validator(currency_1="aaa", currency_2="gbp", amount=100)
        result = validator.is_valid()
        assert result is False

    def test_currency_2_not_valid(self):
        validator = Validator(currency_1="usd", currency_2="bbb", amount=100)
        result = validator.is_valid()
        assert result is False

    def test_amount_not_valid(self):
        validator = Validator(currency_1="usd", currency_2="gbp", amount=-1)
        result = validator.is_valid()
        assert result is False
