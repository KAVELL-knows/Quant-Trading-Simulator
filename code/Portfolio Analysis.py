import numpy as np 
import pandas as pd
from yfinance_downloaded import stocks

#Below is the calc for Daily Return and Expected Daily Return
returns = {}
for symbol in stocks:
    stock_data = pd.read_csv(f"saved_data/{symbol}.csv")
    stock_data["Daily Return"] = (stock_data["Close"] / stock_data["Close"].shift(1)) - 1
    returns[symbol] = stock_data["Daily Return"]

returns = pd.DataFrame(returns) #creates a table using pandas
average_return = returns.mean()
equal_weights = np.array([1 / len(stocks)] * len(stocks))
portfolio_return = (average_return * equal_weights).sum()
print(f"Portfolio Expected Daily Return: {portfolio_return * 100:.4f}%")

#Below is the calulcation for correlation
average_return = returns.mean()
equal_weights = np.array([1/len(stocks)] * len(stocks))
expected_portfolio_return = ( average_return * equal_weights).sum()
portfolio_return = average_return @ equal_weights
annualized_return = ((1 + expected_portfolio_return)**252) -1
correlation_matrix = returns.corr()
covariance_matrix = returns.cov()

print("daily Return", expected_portfolio_return)
print("Annualized Return", annualized_return)
print(expected_portfolio_return)
print(portfolio_return)
print(correlation_matrix)

daily_variance = equal_weights @ covariance_matrix @ equal_weights
daily_volatilty = daily_variance ** 0.5
annualized_volatility = daily_volatilty * (252 ** 0.5)
print("Daily Volatiltiy", daily_volatilty)
print("Annualized Volatility", annualized_volatility)