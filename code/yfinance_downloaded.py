#code/yfinance_downloaded.py

import yfinance as yf
import numpy as np

stocks = ["GME","MPWR", "CLS", "AXON", "TSLA", "PNRG", "AAPL", "MSFT", "NVDA", "ADBE", "AMD", "ORCL", "WLFC", "GOOG", "PLTR", "AVGO", "CVNA", "POWL", "SPOT", "LULU", "HUBS", "ASML", "CRM",
          "WIX", "WING", "TDG", "RBLX", "DUO", "ORLY", "COST", "SONY", "JPM", "V", "LLY", "CVS", "SBUX", "AMZN", "META"]

for symbol in stocks:
    stock = yf.Ticker(symbol)
    data = stock.history(period="20y")
    data.to_csv(f"saved_data/{symbol}.csv")
    print(f"{symbol} downloaded")
    print(data.head())

#bench mark using S and 500
market = yf.Ticker("^GSPC")
market_data = market.history(period="20y")

import pandas as pd
data = pd.read_csv("saved_data/GME.csv")


#NB ALL OF THE ABOVE STAYS IN THIS FILE 


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
market_data["Daily Return"] = (market_data["Close"] / market_data["Close"].shift(1)) - 1



#ALL OF THE ABOVE IS STOCK.ANALYSIS.PY

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

data["Volume vs 20 Day Average"] = data["Volume"] / data["20 Day Average Volume"]
data["Volume vs 100 Day Average"] = data["Volume"] / data["100 Day Average Volume"]
data["Volume vs 1 Year Average"] = data["Volume"] / data["1 Year Average Volume"]
data["Volume vs 5 year Average"] = data["Volume"] / data["5 Year Average Volume"]

data["All Time High"] = data["Close"].cummax()

data["Drawdown($)"] = data["All Time High"] - data["Close"]

data["Drawdown(%)"] = (1 - (data["Close"] / data["All Time High"]))* 100

data["Max Drawdown($)"] = data["Drawdown($)"].max()
data["Max Drawdown(%)"] = data["Drawdown(%)"].max()

gme = pd.read_csv("saved_data/GME.csv")
tdg = pd.read_csv("saved_data/TDG.csv")
gme["Daily Return"] = (gme["Close"] / gme["Close"].shift(1))-1
tdg["Daily Return"] = (tdg["Close"] / tdg["Close"].shift(1))-1
correlation = gme["Daily Return"].corr(tdg["Daily Return"])

print(data.head())
#ALL OF THE ABOVE IS STOCK.ANALYSIS.PY


returns = {}

for symbol in stocks:
    stock_data = pd.read_csv(f"saved_data/{symbol}.csv")
    stock_data["Daily Return"] = (stock_data["Close"] / stock_data["Close"].shift(1))-1
    returns[symbol] = stock_data["Daily Return"]
returns = pd.DataFrame(returns)

#ALL OF THE ABOVE IS PORTFOLIO ANLYSIS.PY



correlation_matrix = returns.corr()
covariance_matrix = returns.cov()
average_return = returns.mean()
equal_weights = np.array([1/len(stocks)] * len(stocks))
expected_portfolio_return = ( average_return * equal_weights).sum()
portfolio_return = average_return @ equal_weights
annualized_return = ((1 + expected_portfolio_return)**252) -1


print("daily Return", expected_portfolio_return)
print("Annualized Return", annualized_return)
print(expected_portfolio_return)
print(portfolio_return)
print(correlation_matrix)
#I put evrythin above int portolfi 
#I think prtoflio return should b anove tis

daily_variance = equal_weights @ covariance_matrix @ equal_weights
daily_volatilty = daily_variance ** 0.5
annualized_volatility = daily_volatilty * (252 ** 0.5)
print("Daily Volatiltiy", daily_volatilty)
print("Annualized Volatility", annualized_volatility)

#VaR
#recall the z score for 95% is 1.645
stock_value = 1000000000000 #TROUBLE SHOOTING NEED THE JSON FILES
var95_parametric = stock_value * ( 1.645 * daily_volatilty - expected_portfolio_return)
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
print( "Exess return:", excess_return,"%")
print("Sharpe Ratio", sharpe_ratio,"%")

#Beta
betas = {}
market_returns = market_data["Daily Return"]
aligned_returns = pd.concat([returns, market_returns], axis=1, join="inner")
aligned_returns = aligned_returns.rename(columns={"Daily Return": "Market"}, inplace=True)
for symbol in stocks:
    stock_returns = aligned_returns[symbol]
    beta = stock_returns.cov(market_returns)/market_returns.var() 
    betas[symbol] = beta


#  CAPM
market_variance = aligned_returns["Market"].var()
market_daily_return = market_returns.mean()
market_annualized_return = ((1 + market_daily_return) ** 252) - 1

capm_expected_returns = {}

for symbol in stocks:
    beta = betas[symbol]
    capm_return = (risk_free_rate + beta * (market_annualized_return - risk_free_rate))
    capm_expected_returns[symbol] = capm_return

print("CAPM Analysis")
for symbol in stocks:
    print(
        f"{symbol}: "
        f"Beta = {betas[symbol]:.3f}, "
        f"CAPM Expected Return = "
        f"{capm_expected_returns[symbol] * 100:.2f}%"
    )

