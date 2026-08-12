#code/yfinance_downloaded.py

import yfinance as yf

stock = yf.Ticker("GME")

data = stock.history(period="20y")

print(data.head())
data.to_csv("saved_data/GME.csv")

import pandas as pd
data = pd.read_csv("saved_data/GME.csv")

data["Daily Change"] = data["Close"] - data["Close"].shift(1)
data["Daily Return"] = (data["Close"] / data["Close"].shift(1))-1
data["5 Day Return"] = (data["Close"] / data["Close"].shift(5))-1
data["10 Day Return"] = (data["Close"] / data["Close"].shift(10))-1
data["20 Day Return"] = (data["Close"] / data["Close"].shift(20))-1
data["100 Day Return"] = (data["Close"] / data["Close"].shift(100))-1
data["200 Day Return"] = (data["Close"] / data["Close"].shift(200))-1
data["1 Year Return"] = (data["Close"] / data["Close"].shift(252))-1
data["2 Year Return"] = (data["Close"] / data["Close"].shift(504))-1
data["5 Year Return"] = (data["Close"] / data["Close"].shift(1260))-1
data["10 Year Return"] = (data["Close"] / data["Close"].shift(2520))-1

data["Daily Volatility"] = data["Daily Return"].std() * (252**0.5)
data["20 Day Volatility"] = data["Daily Return"].rolling(20).std() * (252**0.5)
data["1 Year Volatility"] = data["Daily Return"].rolling(252).std() * (252**0.5)

data["20 Day Moving Average"] = data["Close"].rolling(20).mean()
data["100 Day Moving Average"] = data["Close"].rolling(100).mean()
data["1 Year Moving Average"] = data["Close"].rolling(252).mean()
data["5 Year Moving Average"] = data["Close"].rolling(1260).mean()
data["10 Year Moving Average"] = data["Close"].rolling(2520).mean()

data["Daily Average Volume"] = data["Volume"].mean()
data["20 Day Average Volume"] = data["Volume"].rolling(20).mean()
data["100 Day Average Volume"] = data["Volume"].rolling(100).mean()
data["1 Year Average Volume"] = data["Volume"].rolling(252).mean()
data["5 Year Average Volume"] = data["Volume"].rolling(1260).mean()
data["10 Year Average Volume"] = data["Volume"].rolling(2520).mean()


print(data.head())
