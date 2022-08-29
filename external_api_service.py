import json
import requests
import settings


def get_currency_rate_from_nbp(currency_code: str) -> float:
    response = requests.get(f"{settings.CONSTANT1}{currency_code}/")
    if response.status_code != 200:
        raise Exception("Problem with external API")
    rate = json.loads(response.text)["rates"][0]["mid"]
    return rate
