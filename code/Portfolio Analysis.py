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



#VaR
#recall the z score for 95% is 1.645
stock_value = 1000000000000 #TROUBLE SHOOTING NEED THE JSON FILES
var95_parametric = stock_value * ( 1.645 * daily_volatilty - portfolio_return)
print("95% Daily Parametric VaR:", var95_parametric)

portfolio_returns = returns @ equal_weights
var95_historical = portfolio_returns.quantile(0.05)
print("95% Daily Historical VaR(%):", var95_historical,"%")
var95_historical_dollar = stock_value * abs(var95_historical)
print("95% Daily Historical VaR($): $", var95_historical_dollar)

#Sharpe Ratio
risk_free_rate = 0.0472
excess_return = annualized_return - risk_free_rate
sharpe_ratio = excess_return / annualized_volatility
print("Risk Free Rate",risk_free_rate)
print( "Exess return:", excess_return)
print("Sharpe Ratio", sharpe_ratio)

#BETA
market_data = pd.read_csv("saved_data/^GSPC.csv")
market_data["Daily Return"] = (market_data["Close"] / market_data["Close"].shift(1)) - 1
betas = {}
market_returns = market_data["Daily Return"]
aligned_returns = pd.concat([returns, market_returns], axis=1, join="inner")
aligned_returns = aligned_returns.rename(columns={"Daily Return": "Market"})
for symbol in stocks:
    stock_returns = aligned_returns[symbol]
    beta = stock_returns.cov(market_returns)/market_returns.var() 
    betas[symbol] = beta

#CAPM
market_daily_return = market_returns.mean()
market_annualized_return = ((1 + market_daily_return) ** 252) - 1

capm_expected_returns = {}

for symbol in stocks:
    beta = betas[symbol]
    capm_return = (risk_free_rate + beta * (market_annualized_return - risk_free_rate))
    capm_expected_returns[symbol] = capm_return

print("CAPM Analysis")
for symbol in stocks:
    print(f"{symbol}: "
          f"Beta = {betas[symbol]:.3f}, "
          f"CAPM Expected Return = "
          f"{capm_expected_returns[symbol] * 100:.2f}%")