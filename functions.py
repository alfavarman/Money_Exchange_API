import requests
import json

# base_currency_code = input("Base Currency Code: ").casefold()
# quote_currency_code = input("Quote Currency Code: ").casefold()
#
# response_API_base_currency = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{base_currency_code}/')
# response_API_quote_currency = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{quote_currency_code}/')
#
# amount_to_exchange = float(input(f"Amount to exchange: "))
# base_currency_rate  = json.loads(response_API_base_currency.text)['rates'][0]['mid']
# quote_currency_rate = json.loads(response_API_quote_currency.text)['rates'][0]['mid']
# exchange_rate = base_currency_rate / quote_currency_rate
# exchange_result = amount_to_exchange * exchange_rate
# print(exchange_result)


def money_exchange(base_currency_code: str, quote_currency_code: str) -> float:
    """
    API to exchange given amount_to_exchange of base_currency to quote_currency using API of NBP.pl

    :param base_currency_code: (str) user input of a three-letter currency code (ISO 4217 standard)
    :param quote_currency_code: (str) user input of a three-letter currency code (ISO 4217 standard)
    :param amount_to_exchange: (int or float) user input of amount to exchange
    :return: exchange_result (float) result of exchange
    """
    amount_to_exchange = float(input(f"Amount to exchange: "))
    response_API_base_currency = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{base_currency_code}/')
    response_API_quote_currency = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{quote_currency_code}/')
    base_currency_rate = json.loads(response_API_base_currency.text)['rates'][0]['mid']
    quote_currency_rate = json.loads(response_API_quote_currency.text)['rates'][0]['mid']
    exchange_rate = base_currency_rate / quote_currency_rate
    exchange_result = amount_to_exchange * exchange_rate
    return exchange_result
