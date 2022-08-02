from iso4217 import Currency

with open('iso4217.py', 'w') as f:
    for a, b in enumerate(Currency):
        f.write(f'"{b.value}", ')

