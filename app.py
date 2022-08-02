from flask import Flask, jsonify, request

from functions import MoneyService

app = Flask(__name__)


@app.route("/")
def currency_exchange_api():

    exchange = MoneyService(
        currency_1=request.args.get("curr1"),
        currency_2=request.args.get("curr2"),
        amount=request.args.get("amount"),
    )
    # build validator
    try:
        exchange.get_money_exchange()
    except Exception as e:
        return jsonify({"error": str(e)})
    return jsonify(
        {exchange.currency_2: float("{:.2f}".format(exchange.get_money_exchange()))}
    )


if __name__ == "__main__":
    app.run(debug=True)
