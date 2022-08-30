from unittest import TestCase
from unittest.mock import patch, MagicMock
from services.external_api_service import get_currency_rate_from_nbp


class TestExternalApiService(TestCase):
    @patch("services.external_api_service.requests.get")
    def test_wrong_getresponse(self, mocked_get):
        nbp_resp = MagicMock()
        nbp_resp.status_code = 400
        mocked_get.return_value = nbp_resp
        with self.assertRaises(Exception):
            get_currency_rate_from_nbp(currency_code="GBP")
        assert mocked_get.call_args.args[0] == "http://api.nbp.pl/api/exchangerates/rates/a/GBP/"

    @patch("services.external_api_service.requests.get")
    def test_correct_getresponse(self, mocked_get):
        nbp_resp = MagicMock()
        nbp_resp.status_code = 200
        nbp_resp.text = '{"table":"A","currency":"dolar australijski","code":"AUD","rates":[{"no":"166/A/NBP/2022","effectiveDate":"2022-08-29","mid":3.2757}]}'
        mocked_get.return_value = nbp_resp
        get_currency_rate_from_nbp(currency_code="AUD")
        assert mocked_get.call_args.args[0] == "http://api.nbp.pl/api/exchangerates/rates/a/AUD/"
        assert get_currency_rate_from_nbp(currency_code="AUD") == 3.2757
