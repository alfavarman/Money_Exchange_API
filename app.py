from flask import jsonify, request

from money_service import MoneyService
from settings import app
from validators import Validator


@app.route("/")
def currency_exchange_api():
    curr1 = request.args.get("curr1")
    curr2 = request.args.get("curr2")
    amount = request.args.get("amount")

    validator = Validator(currency_1=curr1, currency_2=curr2, amount=amount)
    if not validator.is_valid():
        return jsonify({"error": ", ".join(validator.error)})

    try:
        exchange = MoneyService(
            currency_1=curr1,
            currency_2=curr2,
            amount=amount,
        )
        exchange_result = exchange.get_money_exchange()
        payload = {exchange.currency_2: round(exchange_result, 2)}
        return jsonify(payload)
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
