from functions import money_exchange

if __name__ == "__main__":
    base_curr_code = input("Base Currency Code: ").casefold()
    quote_curr_code = input("Quote Currency Code: ").casefold()
    print(f'{money_exchange(base_curr_code, quote_curr_code)}{quote_curr_code}')
