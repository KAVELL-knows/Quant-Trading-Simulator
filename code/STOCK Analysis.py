#Stock Analysis 
import numpy as np 
import pandas as pd
from yfinance_downloaded import stocks

symbol = input("Enter the stock symbol of your choice").upper()
data = pd.read_csv(f"saved_data/{symbol}.csv")

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
data["50 Day Volatility"] = data["Daily Return"].rolling(50).std() * (252**0.5)
data["100 Day Volatility"] = data["Daily Return"].rolling(100).std() * (252**0.5)
data["200 Day Volatility"] = data["Daily Return"].rolling(200).std() * (252**0.5)
data["1 Year Volatility"] = data["Daily Return"].rolling(252).std() * (252**0.5)
data["5 Year Volatility"] = data["Daily Return"].rolling(252*5).std() * (252**0.5)
data["10 Year Volatility"] = data["Daily Return"].rolling(252*10).std() * (252**0.5)

data["20 Day Moving Average"] = data["Close"].rolling(20).mean()
data["50 Day Moving Average"] = data["Close"].rolling(50).mean()
data["100 Day Moving Average"] = data["Close"].rolling(100).mean()
data["200 Day Moving Average"] = data["Close"].rolling(200).mean()
data["1 Year Moving Average"] = data["Close"].rolling(252).mean()
data["5 Year Moving Average"] = data["Close"].rolling(1260).mean()
data["10 Year Moving Average"] = data["Close"].rolling(2520).mean()

data["Daily Average Volume"] = data["Volume"].mean()
data["20 Day Average Volume"] = data["Volume"].rolling(20).mean()
data["50 Day Average Volume"] = data["Volume"].rolling(50).mean()
data["100 Day Average Volume"] = data["Volume"].rolling(100).mean()
data["200 Day Average Volume"] = data["Volume"].rolling(200).mean()
data["1 Year Average Volume"] = data["Volume"].rolling(252).mean()
data["5 Year Average Volume"] = data["Volume"].rolling(1260).mean()
data["10 Year Average Volume"] = data["Volume"].rolling(2520).mean()

data["Volume vs 20 Day Average"] = data["Volume"] / data["20 Day Average Volume"]
data["Volume vs 100 Day Average"] = data["Volume"] / data["100 Day Average Volume"]
data["Volume vs 1 Year Average"] = data["Volume"] / data["1 Year Average Volume"]
data["Volume vs 5 year Average"] = data["Volume"] / data["5 Year Average Volume"]

data["All Time High"] = data["Close"].cummax()

data["Drawdown($)"] = data["All Time High"] - data["Close"]

data["Drawdown(%)"] = (1 - (data["Close"] / data["All Time High"]))* 100

data["Max Drawdown($)"] = data["Drawdown($)"].max()
data["Max Drawdown(%)"] = data["Drawdown(%)"].max()


sec_symbol = input("Enter the second stock symbol of your choice to compare data with").upper()
sec_data = pd.read_csv(f"saved_data/{sec_symbol}.csv")

data["Daily Return"] = (data["Close"] / data["Close"].shift(1))-1
sec_data["Daily Return"] = (sec_data["Close"] / sec_data["Close"].shift(1))-1


correlation = data["Daily Return"].corr(sec_data["Daily Return"])
print(f"Correlation between {symbol} and {sec_symbol}: {correlation:.4f}")
print(data.head())

# BETA
market_data = pd.read_csv("saved_data/^GSPC.csv")
market_data["Daily Return"] = (market_data["Close"] / market_data["Close"].shift(1)) - 1
market_returns = market_data["Daily Return"]

aligned_returns = pd.concat([data["Daily Return"], market_returns],axis=1,join="inner")
aligned_returns.columns = [symbol, "Market"]
stock_returns = aligned_returns[symbol]
beta = stock_returns.cov(aligned_returns["Market"]) / aligned_returns["Market"].var()

print(f"Beta of {symbol}: {beta:.3f}")


# CAPM
risk_free_rate = 0.0472
market_daily_return = aligned_returns["Market"].mean()
market_annualized_return = ((1 + market_daily_return) ** 252) - 1
capm_expected_return = (risk_free_rate+ beta * (market_annualized_return - risk_free_rate))
print(f"CAPM Expected Return for {symbol}: "
      f"{capm_expected_return * 100:.2f}%")

# SHARPE RATIO
annualized_return = ((1 + stock_returns.mean()) ** 252) - 1
annualized_volatility = stock_returns.std() * (252 ** 0.5)
excess_return = annualized_return - risk_free_rate
sharpe_ratio = excess_return / annualized_volatility
print(f"Annualized Return: {annualized_return * 100:.2f}%")
print(f"Annualized Volatility: {annualized_volatility * 100:.2f}%")
print(f"Sharpe Ratio: {sharpe_ratio:.3f}")

# VALUE AT RISK
confidence_level = 0.05
var_95 = stock_returns.quantile(confidence_level)
print(f"95% Daily VaR: {var_95 * 100:.2f}%")


#Summary Sheet
current_price = data["Close"].iloc[-1]
one_year_return = data["1 Year Return"].iloc[-1]
five_year_return = data["5 Year Return"].iloc[-1]
all_time_high = data["All Time High"].iloc[-1]
max_drawdown = data["Max Drawdown(%)"].iloc[-1]


print("==+" * 30)
print(f"                                SUMMARY OF {symbol}")
print("==+" * 30)
print()
print()
print("PRICE")
print(f"Current Price: ${current_price:.2f}")
print(f"All Time High:  ${all_time_high:.2f}")
print()
print("RETURNS")
print(f"1 Year Return:  {one_year_return * 100:.2f}%")
print(f"5 Year Return:  {five_year_return * 100:.2f}%")
print()
print("RISK")
print(f"Annualized Volatility:  {annualized_volatility * 100:.2f}%")
print(f"Maximum Drawdown:      {max_drawdown:.2f}%")
print(f"Beta:                   {beta:.3f}")
print(f"95% Daily VaR:          {var_95 * 100:.2f}%")
print()
print("RISK ADJUSTMENT PERFORMANCE")
print(f"Sharpe Ratio:  {sharpe_ratio:.3f}")
print()
print(f"CAPM Expected Return:  {capm_expected_return * 100:.2f}%")
print()
print("COMPARISON")
print(f"Compared With: {sec_symbol}")
print(f"Correlation:   {correlation:.4f}")
print()
