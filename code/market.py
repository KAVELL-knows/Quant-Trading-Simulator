#market.py
import pandas as pd
import random


stocks = {}
stock_symbols = ["GME", "AXON", "MPWR", "CLS", "TSLA", "AAPL", "ADBE", "AMD", "AMZN", "ASML", "AVGO", "AXON", "CLS", "COST", "CRM",
                 "CVNA", "CVS", "DUO", "GOOG", "HUBS", "JPM", "LLY", "LULU", "META", "MSFT", "NVDA", "ORCL", "ORLY", "PLTR", "PNRG",
                 "POWL", "RBLX", "SBUX", "SONY", "SPOT", "TDG", "TSLA", "V", "WING", "WIX", "WLFC"]

for symbol in stock_symbols:
    data = pd.read_csv(f"saved_data/{symbol}.csv")
    stocks[symbol] = data["Close"].iloc[-1]

price_history = {stock: [price] for stock, price in stocks.items()}

def stock_price():
    print("Current stock prices:")

    for stock, price in stocks.items():
        print(f"{stock}: ${price:.2f}")

def update_prices():
    for stock, price in stocks.items():
        change = random.uniform(-0.045,0.045)
        stocks[stock] = max(0.01, stocks[stock] * (1 + change))
        price_history[stock].append(stocks[stock])

def predict_prices():
    rows = int(input("Enter the number of days you want to predict: "))
    columns = int(input("Enter the number of stocks you want to predict: "))

    predicted_stocks = []

    for j in range(columns):
        stock = input("Enter the stock symbol you want to predict: ").upper().strip()
        if stock in stocks:
            print(f"{stock}: ${stocks[stock]:.2f}")
        else:
            print("404 error stock not found. Please enter a valid stock symbol.")
        while stock not in stocks:
            stock = input("Enter the stock symbol: ").upper().strip()

        predicted_stocks.append(stock)
        print(predicted_stocks)

    prediction_table = []
    for i in range(1, rows+1):
        update_prices()

        predicted_day = []

        for stock in predicted_stocks:
            predicted_day.append(stocks[stock])
        prediction_table.append(predicted_day)

    print()
    print("       ", end="")

    for stock in predicted_stocks:
        print(f"{stock:>10}", end="")

    print()

    for i, day in enumerate(prediction_table, start=1):
        print(f"Day {i:<3}", end="")

        for price in day:
            print(f"${price:>9.2f}", end="")
        print()