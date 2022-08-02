from flask import Flask, jsonify, request

from functions import get_money_exchange

app = Flask(__name__)


@app.route("/")
def currency_exchange_api():
    curr1 = request.args.get("curr1")
    curr2 = request.args.get("curr2")
    amount = request.args.get("amount")
    try:
        result = get_money_exchange(
            currency_1=curr1, currency_2=curr2, amount=float(amount)
        )
    except Exception as e:
        return jsonify({'error': str(e)})
    return jsonify({curr2: float("{:.2f}".format(result))})


if __name__ == "__main__":
    app.run(debug=True)
