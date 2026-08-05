#market.py
import random

stocks = {
    "GME".upper().strip(): 22.51,
    "AXON".upper().strip(): 859.42,
    "MPWR".upper().strip(): 770.01,
    "CLS".upper().strip(): 220.42,
    "TSLA".upper().strip(): 402.54
}

price_history = {
    stock: [price]
    for stock, price in stocks.items()
}

def stock_price():
    print("Current stock prices:")

    for stock, price in stocks.items():
        print(f"{stock}: ${price:.2f}")

def update_prices():
    for stock, price in stocks.items():
        change = random.uniform(-0.045,0.045)
        stocks[stock] = max(0.01, stocks[stock] * (1 + change))
        price_history[stock].append(stocks[stock])