# Technical Analysis
import pandas as pd
symbol = input("Enter the stock symbol you want to analyze: ").upper()
data = pd.read_csv(f"saved_data/{symbol}.csv")

data["20 Day Moving Average"] = data["Close"].rolling(20).mean()
data["100 Day Moving Average"] = data["Close"].rolling(100).mean()
data["1 Year Moving Average"] = data["Close"].rolling(252).mean()
data["5 Year Moving Average"] = data["Close"].rolling(252*5).mean()
current_price = data["Close"].iloc[-1]
moving_average20d = data["20 Day Moving Average"].iloc[-1]
moving_average100d = data["100 Day Moving Average"].iloc[-1] 
moving_average1y = data["1 Year Moving Average"].iloc[-1]
moving_average5y = data["5 Year Moving Average"].iloc[-1]
if current_price > moving_average20d:
    print("Price is above the 20 Day Moving Average")
else:
    print("Price is below the 20 Day Moving Average")
if current_price > moving_average100d:
    print("Price is above the 100 Day Moving Average")
else:
    print("Price is below the 100 Day Moving Average")
if current_price > moving_average1y:
    print("Price is above the 1 Year Moving Average")
else:
    print("Price is below the 1 Year Moving Average")
if current_price > moving_average5y:
    print("Price is above the 5 Year Moving Average")
else:
    print("Price is below the 5 Year Moving Average")
#TRENDS
if current_price > moving_average20d:
    short_trend = "Bullish"
else:
    short_trend = "Bearish"
if current_price > moving_average100d:
    medium_trend = "Bullish"
else:
    medium_trend = "Bearish"
print(f"Medium-Term Trend: {medium_trend}")
if current_price > moving_average1y:
    long_trend = "Bullish"
else:
    long_trend = "Bearish"
if current_price > moving_average5y:
    vlong_trend = "Bullish"
else:
    vlong_trend = "Bearish"
print(f"Long-Term Trend: {long_trend}")
print(f"Very Long-Term Trend: {vlong_trend}")
print(f"Short-Term Trend: {short_trend}")
print(f"Short-Term Trend: {short_trend}")

#Momentum Analysis
data["20 Day Momentum"] = data["Close"].pct_change(20)
data["100 Day Momentum"] = data["Close"].pct_change(100)
momentum20d = data["20 Day Momentum"].iloc[-1]
momentum100d = data["100 Day Momentum"].iloc[-1]
print(f"20 Day Momentum: {momentum20d * 100:.2f}%")
print(f"100 Day Momentum: {momentum100d * 100:.2f}%")
if momentum20d > 0:
    momentum20_posneg = "Positive"
else:
    momentum20_posneg = "Negative"

if momentum100d > 0:
    momentum100_posneg = "Positive"
else:
    momentum100_posneg = "Negative"
print(f"20 Day Momentum Signal: {momentum20_posneg}")
print(f"100 Day Momentum Signal: {momentum100_posneg}")


# RSI Analysis
data["Price Change"] = data["Close"].diff()
data["Gain"] = data["Price Change"].clip(lower=0)
data["Loss"] = -data["Price Change"].clip(upper=0)
data["Average Gain"] = data["Gain"].rolling(14).mean()
data["Average Loss"] = data["Loss"].rolling(14).mean()
gain_rsi = data["Average Gain"].iloc[-1]
loss_rsi = data["Average Loss"].iloc[-1]

relative_strength_index = gain_rsi / loss_rsi
rsi = 100 - (100 / (1 + relative_strength_index))
print(f"RSI: {rsi:.2f}")

