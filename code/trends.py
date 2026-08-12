#collecting data

import json
from market import stocks

def data_collected():
    try:
        with open("history_of_prices.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    for stock, price in stocks.items():
        if stock not in data:
            data[stock] = []

        data[stock].append(price)

    with open("history_of_prices.json", "w") as file:
        json.dump(data, file, indent=4)