from iso4217 import country_codes as codes


class Validator:
    def __init__(self, currency_1: str, currency_2: str, amount: str):
        self.currency_1 = currency_1
        self.currency_2 = currency_2
        self.amount = amount
        self.error = []

    def is_valid(self) -> bool:
        if self.currency_1.upper() not in codes:
            self.error.append("Wrong Currency1 Code")

        if self.currency_2.upper() not in codes:
            self.error.append("Wrong Currency2 Code")

        if float(self.amount) < 0:
            self.error.append("Amount must be a positive number")

        return len(self.error) == 0
