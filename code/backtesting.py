#Backtesting 
import pandas as pd
import numpy as np 
symbol = input("Enter the stock symbol you want to analyze: ").upper()
data = pd.read_csv(f"saved_data/{symbol}.csv")

#Moving Average
data["20 Day Moving Average"] = data["Close"].rolling(20).mean()
data["100 Day Moving Average"] = data["Close"].rolling(100).mean()
data["1 Year Moving Average"] = data["Close"].rolling(252).mean()
data["5 Year Moving Average"] = data["Close"].rolling(252*5).mean()
#Momentum
data["20 Day Momentum"] = data["Close"].pct_change(20)
data["100 Day Momentum"] = data["Close"].pct_change(100)

#RSI Analysis
data["Price Change"] = data["Close"].diff()
data["Gain"] = data["Price Change"].clip(lower=0)
data["Loss"] = -data["Price Change"].clip(upper=0)
data["Average Gain"] = data["Gain"].rolling(14).mean()
data["Average Loss"] = data["Loss"].rolling(14).mean()

#MACD ANALYSIS
data["12 Day EMA"] = data["Close"].ewm(span=12, adjust=False).mean()
data["26 Day EMA"] = data["Close"].ewm(span=26, adjust=False).mean()
data["MACD"] = data["12 Day EMA"] - data["26 Day EMA"]
data["MACD Signal Line"] = data["MACD"].ewm(span=9, adjust=False).mean()


#Volume Analysis
data["10 Day Average Volume"] = data["Volume"].rolling(10).mean()
data["20 Day Average Volume"] = data["Volume"].rolling(20).mean()
data["50 Day Average Volume"] = data["Volume"].rolling(50).mean()
data["100 Day Average Volume"] = data["Volume"].rolling(100).mean()
data["200 Day Average Volume"] = data["Volume"].rolling(200).mean()
data["1 Year Average Volume"] = data["Volume"].rolling(252).mean()
data["10 Day Volume Standard Deviation"] = data["Volume"].rolling(10).std()
data["20 Day Volume Standard Deviation"] = data["Volume"].rolling(20).std()
data["50 Day Volume Standard Deviation"] = data["Volume"].rolling(50).std()
data["100 Day Volume Standard Deviation"] = data["Volume"].rolling(100).std()
data["200 Day Volume Standard Deviation"] = data["Volume"].rolling(200).std()
data["1 Year Volume Standard Deviation"] = data["Volume"].rolling(252).std()

# List to save the data
backtest_summary = []
backtest_indicators = []

#FOR LOOP SET UP
for i in range(252*5, len(data) - 20):
    date = data["Date"].iloc[i]
    current_price = data["Close"].iloc[i]
    moving_average20d = data["20 Day Moving Average"].iloc[i]
    moving_average100d = data["100 Day Moving Average"].iloc[i] 
    moving_average1y = data["1 Year Moving Average"].iloc[i]
    moving_average5y = data["5 Year Moving Average"].iloc[i]
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
    momentum20d = data["20 Day Momentum"].iloc[i]
    momentum100d = data["100 Day Momentum"].iloc[i]
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
    gain_rsi = data["Average Gain"].iloc[i]
    loss_rsi = data["Average Loss"].iloc[i]
    if loss_rsi == 0:
        loss_rsi = 0.0001
        relative_strength_index = gain_rsi / loss_rsi
        rsi = 100 - (100 / (1 + relative_strength_index))
        print(f"RSI: {rsi:.2f}")
        print("RSI_Losss was 0 but to avoid undefined, 0.0001 was used")
    else:
        relative_strength_index = gain_rsi / loss_rsi
        rsi = 100 - (100 / (1 + relative_strength_index))
        if rsi < 30:
            rsi_posneg = "Oversold"
        elif rsi < 45:
            rsi_posneg = "Bearish"
        elif rsi <= 55:
            rsi_posneg = "Neutral"
        elif rsi <= 70:
            rsi_posneg = "Bullish"
        else:
            rsi_posneg = "Overbought"
        print(f"RSI: {rsi:.2f}")
        print(f"RSI Signal: {rsi_posneg}")
    # MACD Analysis
    macd = data["MACD"].iloc[i]
    if macd > 0:
        print("The 12-day EMA is higher than the 26-day EMA. Short-term upward momentum is accelerating faster than the long-term trend.")
    elif macd < 0:
        print("The 12-day EMA is lower than the 26-day EMA. Short-term selling momentum is accelerating downward.")
    else:
        print("MACD is exactly 0.The 12-Day EMA and the 26-Day EMA are perfectly equal. ")
    print(f"MACD: {macd:.2f}")
    bull_bear = data["MACD Signal Line"].iloc[i]
    if macd > bull_bear:
        signal = "Bullish"
    elif macd < bull_bear:
        signal = "Bearish"
    else:
        signal = "Neutral"
    print(f"MACD Signal Line: {bull_bear:.2f}")
    print(f"MACD Signal: {signal}")
    # Volume Analysis
    current_vol = data["Volume"].iloc[i]
    average_vol10d = data["10 Day Average Volume"].iloc[i]
    average_vol20d = data["20 Day Average Volume"].iloc[i]
    average_vol50d = data["50 Day Average Volume"].iloc[i]
    average_vol100d = data["100 Day Average Volume"].iloc[i]
    average_vol200d = data["200 Day Average Volume"].iloc[i]
    average_vol1y = data["1 Year Average Volume"].iloc[i]
    std_vol10d = data["10 Day Volume Standard Deviation"].iloc[i]
    std_vol20d = data["20 Day Volume Standard Deviation"].iloc[i]
    std_vol50d = data["50 Day Volume Standard Deviation"].iloc[i]
    std_vol100d = data["100 Day Volume Standard Deviation"].iloc[i]
    std_vol200d = data["200 Day Volume Standard Deviation"].iloc[i]
    std_vol1y = data["1 Year Volume Standard Deviation"].iloc[i]
    if average_vol10d > 0:
        rvol10d = current_vol / average_vol10d  
    else :
        rvol10d = 0
    if average_vol20d > 0:
        rvol20d = current_vol / average_vol20d  
    else :
        rvol20d = 0
    if average_vol50d > 0:
        rvol50d = current_vol / average_vol50d  
    else :
        rvol50d = 0
    if average_vol100d > 0:
        rvol100d = current_vol / average_vol100d  
    else :
        rvol100d = 0
    if average_vol200d > 0:
        rvol200d = current_vol / average_vol200d  
    else :
        rvol200d = 0
    if average_vol1y > 0:
        rvol1y = current_vol / average_vol1y  
    else :
        rvol1y = 0
    print(f"10 Day Relative Volume: {rvol10d:.2f}")
    print(f"20 Day Relative Volume: {rvol20d:.2f}")
    print(f"50 Day Relative Volume: {rvol50d:.2f}")
    print(f"100 Day Relative Volume: {rvol100d:.2f}")
    print(f"200 Day Relative Volume: {rvol200d:.2f}")
    print(f"1 Year Relative Volume: {rvol1y:.2f}")
    #Volume Confirmation
    if rvol20d >= 2:
        vol_confirm = "Very Strong"
    elif rvol20d >= 1.5:
        vol_confirm = "Strong"
    elif rvol20d >= 0.8:
        vol_confirm = "Normal"
    else:
        vol_confirm = "Weak"
    print(f"20 Day %: {rvol20d * 100:,.0f}%")
    print(f"Volume Confirmation: {vol_confirm}")
    if current_vol > (average_vol10d + (2 * std_vol10d)) and current_vol > average_vol100d:
        vol_signal10d1 = "Institutional Surge (Extremely High)"
    elif current_vol > average_vol10d * 1.5:
        vol_signal10d1 = "High (Relative Volume > 1.5)"
    elif current_vol < average_vol10d * 0.5:
        vol_signal10d1 = "Low (Illiquid / Drying Up)"
    else:
        vol_signal10d1 = "Normal / Average"


    if current_vol > (average_vol20d + (2 * std_vol20d)) and current_vol > average_vol100d:
        vol_signal20d1 = "Institutional Surge (Extremely High)"
    elif current_vol > average_vol20d * 1.5:
        vol_signal20d1 = "High (Relative Volume > 1.5)"
    elif current_vol < average_vol20d * 0.5:
        vol_signal20d1 = "Low (Illiquid / Drying Up)"
    else:
        vol_signal20d1 = "Normal / Average"
    if current_vol > (average_vol50d + (2 * std_vol50d)) and current_vol > average_vol100d:
        vol_signal50d1 = "Institutional Surge (Extremely High)"
    elif current_vol > average_vol50d * 1.5:
        vol_signal50d1 = "High (Relative Volume > 1.5)"
    elif current_vol < average_vol50d * 0.5:
        vol_signal50d1 = "Low (Illiquid / Drying Up)"
    else:
        vol_signal50d1 = "Normal / Average"
    if current_vol > (average_vol100d + (2 * std_vol100d)) and current_vol > average_vol100d:
        vol_signal100d1 = "Institutional Surge (Extremely High)"
    elif current_vol > average_vol100d * 1.5:
        vol_signal100d1 = "High (Relative Volume > 1.5)"
    elif current_vol < average_vol100d * 0.5:
        vol_signal100d1 = "Low (Illiquid / Drying Up)"
    else:
        vol_signal100d1 = "Normal / Average"
    if current_vol > (average_vol200d + (2 * std_vol200d)) and current_vol > average_vol100d:
        vol_signal200d1 = "Institutional Surge (Extremely High)"
    elif current_vol > average_vol200d * 1.5:
        vol_signal200d1 = "High (Relative Volume > 1.5)"
    elif current_vol < average_vol200d * 0.5:
        vol_signal200d1 = "Low (Illiquid / Drying Up)"
    else:
        vol_signal200d1 = "Normal / Average"

    if current_vol > (average_vol1y + (2 * std_vol1y)) and current_vol > average_vol100d:
        vol_signal1y1 = "Institutional Surge (Extremely High)"
    elif current_vol > average_vol1y * 1.5:
        vol_signal1y1 = "High (Relative Volume > 1.5)"
    elif current_vol < average_vol1y * 0.5:
        vol_signal1y1 = "Low (Illiquid / Drying Up)"
    else:
        vol_signal1y1 = "Normal / Average"
    print(f"10 Day Average Volume: {average_vol10d:,.0f}")
    print(f"20 Day Average Volume: {average_vol20d:,.0f}")
    print(f"50 Day Average Volume: {average_vol50d:,.0f}")
    print(f"100 Day Average Volume: {average_vol100d:,.0f}")
    print(f"200 Day Average Volume: {average_vol200d:,.0f}")
    print(f"1 Year Average Volume: {average_vol1y:,.0f}")
    print(f"Volume Signal: {vol_signal10d1}")
    print(f"Volume Signal: {vol_signal20d1}")
    print(f"Volume Signal: {vol_signal50d1}")
    print(f"Volume Signal: {vol_signal100d1}")
    print(f"Volume Signal: {vol_signal200d1}")
    print(f"Volume Signal: {vol_signal1y1}")
    if current_vol > average_vol10d:
        vol_signal10d = "High"
    elif current_vol < average_vol10d:
        vol_signal10d = "Low"
    else:
        vol_signal10d = "Average"
    print(f"Volume Signal: {vol_signal10d}")
    if current_vol > average_vol20d:
        vol_signal20d = "High"
    elif current_vol < average_vol20d:
        vol_signal20d = "Low"
    else:
        vol_signal20d = "Average"
    print(f"Volume Signal: {vol_signal20d}")
    if current_vol > average_vol50d:
        vol_signal50d = "High"
    elif current_vol < average_vol50d:
        vol_signal50d = "Low"
    else:
        vol_signal50d = "Average"
    print(f"Volume Signal: {vol_signal50d}")
    if current_vol > average_vol100d:
        vol_signal100d = "High"
    elif current_vol < average_vol100d:
        vol_signal100d = "Low"
    else:
        vol_signal100d = "Average"
    print(f"Volume Signal: {vol_signal100d}")
    if current_vol > average_vol200d:
        vol_signal200d = "High"
    elif current_vol < average_vol200d:
        vol_signal200d = "Low"
    else:
        vol_signal200d = "Average"
    print(f"Volume Signal: {vol_signal200d}")
    if current_vol > average_vol1y:
        vol_signal1y = "High"
    elif current_vol < average_vol1y:
        vol_signal1y = "Low"
    else:
        vol_signal1y = "Average"
    print(f"Volume Signal: {vol_signal1y}")
    #SCORING STSEM TO GET FINAL SIGNAL 
    signal_score = 0
    if short_trend == "Bullish":
        signal_score += 1
    elif short_trend == "Bearish":
        signal_score -= 1
    if medium_trend == "Bullish":
        signal_score += 2
    elif medium_trend == "Bearish":
        signal_score -= 2
    if long_trend == "Bullish":
        signal_score += 3
    elif long_trend == "Bearish":
        signal_score -= 3
    if vlong_trend == "Bullish":
        signal_score += 2
    elif vlong_trend == "Bearish":
        signal_score -= 2
    if momentum20_posneg == "Positive":
        signal_score += 1
    elif momentum20_posneg == "Negative":
        signal_score -= 1
    if momentum100_posneg == "Positive":
        signal_score += 2
    elif momentum100_posneg == "Negative":
        signal_score -= 2
    #RSI SCROING 
    if rsi_posneg == "Bullish":
        signal_score += 1
    elif rsi_posneg == "Bearish":
        signal_score -= 1
    elif rsi_posneg == "Neutral":
        signal_score += 0
    elif rsi_posneg == "Oversold":
        signal_score += 0
    elif rsi_posneg == "Overbought":
        signal_score += 0
    if signal == "Bullish":
        signal_score += 2
    elif signal == "Bearish":
        signal_score -= 2
    if signal_score >= 8:
        final_signal = "STRONG BUY"
    elif signal_score >= 4 and signal_score < 8:  
        final_signal = "BUY"
    elif signal_score <= -8:
        final_signal = "STRONG SELL"
    elif signal_score <= -4 and signal_score > -8: 
        final_signal = "SELL"
    else:
        final_signal = "HOLD"
    print(f"Technical Score: {signal_score}")
    print(f"Final Signal: {final_signal}")
    #Confirmed Signal 
    if final_signal == "STRONG BUY":
        if vol_confirm == "Very Strong":
            confirmed_signal = "EXTREMELY STRONG BUY CONFIRMED"
        elif vol_confirm == "Strong":
            confirmed_signal = "STRONG BUY CONFIRMED"
        elif vol_confirm == "Normal":
            confirmed_signal = "STRONG BUY (POTENTIALLY)"
        else:
            confirmed_signal = "STRONG BUY (WEAK VOLUME)"
    elif final_signal == "BUY":
        if vol_confirm == "Very Strong":
            confirmed_signal = "EXTREMELY BUY STRONGLY CONFIRMED"
        elif vol_confirm == "Strong":
            confirmed_signal = "BUY CONFIRMED"
        elif vol_confirm == "Normal":
            confirmed_signal = "BUY (POTENTIALLY)"
        else:
            confirmed_signal = "BUY (WEAK VOLUME)"
    elif final_signal == "STRONG SELL":
        if vol_confirm == "Very Strong":
            confirmed_signal = "EXTREMELY STRONG SELL CONFIRMED"
        elif vol_confirm == "Strong":
            confirmed_signal = "STRONG SELL CONFIRMED"
        elif vol_confirm == "Normal":
            confirmed_signal = "STRONG SELL (POTENTIALLY)"
        else:
            confirmed_signal = "STRONG SELL (WEAK VOLUME)"
    elif final_signal == "SELL":
        if vol_confirm == "Very Strong":
            confirmed_signal = "EXTREMELY SELL STRONGLY CONFIRMED"
        elif vol_confirm == "Strong":
            confirmed_signal = "SELL STRONG CONFIRMED"
        elif vol_confirm == "Normal":
            confirmed_signal = "SELL (POTENTIALLY)"
        else:
            confirmed_signal = "SELL (WEAK VOLUME)"
    else:
        confirmed_signal = "HOLD"
    print(f"Confirmed Signal: {confirmed_signal}")
    # CONFLUENCE ANALYSIS USING 8 INDICATORS 
    bullish_signals = 0
    bearish_signals = 0
    # SHORT-TERM TREND
    if short_trend == "Bullish":
        bullish_signals += 1
    elif short_trend == "Bearish":
        bearish_signals += 1
    # MEDIUM-TERM TREND
    if medium_trend == "Bullish":
        bullish_signals += 1
    elif medium_trend == "Bearish":
        bearish_signals += 1
    # LONG-TERM TREND
    if long_trend == "Bullish":
        bullish_signals += 1
    elif long_trend == "Bearish":
        bearish_signals += 1
    # VERY LONG-TERM TREND
    if vlong_trend == "Bullish":
        bullish_signals += 1
    elif vlong_trend == "Bearish":
        bearish_signals += 1
    # 20-DAY MOMENTUM
    if momentum20_posneg == "Positive":
        bullish_signals += 1
    elif momentum20_posneg == "Negative":
        bearish_signals += 1

    # 100-DAY MOMENTUM
    if momentum100_posneg == "Positive":
        bullish_signals += 1
    elif momentum100_posneg == "Negative":
        bearish_signals += 1
    # RSI
    if rsi_posneg == "Bullish":
        bullish_signals += 1
    elif rsi_posneg == "Bearish":
        bearish_signals += 1
    elif rsi_posneg == "Neutral":
        pass
    elif rsi_posneg == "Oversold":
        pass
    elif rsi_posneg == "Overbought":
        pass



    # MACD
    if signal == "Bullish":
        bullish_signals += 1
    elif signal == "Bearish":
        bearish_signals += 1
    total_active_signals = bullish_signals + bearish_signals
    if total_active_signals > 0:
        bullish_directional_agreement = (bullish_signals / total_active_signals) * 100
        bearish_directional_agreement = (bearish_signals / total_active_signals) * 100
    else:
        bullish_directional_agreement = 0
        bearish_directional_agreement = 0
    # % of confluence for bullish and bearish signals
    if bullish_directional_agreement >= 87.5:
        confluence = "Extremely Strong Bullish Agreement"
    elif bullish_directional_agreement >= 75:
        confluence = "Strong Bullish Agreement"
    elif bullish_directional_agreement >= 62.5:
        confluence = "Moderate Bullish Agreement"
    elif bearish_directional_agreement >= 87.5:
        confluence = "Extremely Strong Bearish Agreement"
    elif bearish_directional_agreement >= 75:
        confluence = "Strong Bearish Agreement"
    elif bearish_directional_agreement >= 62.5:
        confluence = "Moderate Bearish Agreement"
    else:
        confluence = "Mixed Signals"
    print("SIGNAL CONFLUENCE")
    print(f"Date: {date}")
    print(f"Bullish Indicators: {bullish_signals}")
    print(f"Bullish Agreement: {bullish_directional_agreement:.3f}%")
    print(f"Bearish Indicators: {bearish_signals}")
    print(f"Bearish Agreement: {bearish_directional_agreement:.3f}%")
    print(f"Total Active Signals: {total_active_signals}")
    print(f"Confluence: {confluence}")
    backtest_indicators.append({"Date": date, "Short-term Trends":short_trend, "Medium Trend": medium_trend,
                                "Long-term Trend": long_trend, "Extremely long-term Trend":vlong_trend,
                                "20 Day Momentum Signal": momentum20_posneg, "20 Day Momentum": momentum20d,
                                "100 Momentum Signal": momentum100_posneg, "100 Day Momentum": momentum100d,
                                "RSI Signal": rsi_posneg, "RSI": rsi, "MACD Signal": signal, "MACD Singal Line": bull_bear,
                                "MACD": macd, "Volume Confirmation":vol_confirm, "Volume 20 Days": rvol20d, 
                                "Bullish Signals": bullish_signals, "Bullish Directional Agreement(%)": bullish_directional_agreement,
                                "Bearish Signals": bearish_signals, "Bearish Directional Agreement": bearish_directional_agreement})
    future_price = data["Close"].iloc[i + 20]
    future_return = (future_price / current_price) - 1
    future_return_percent = future_return * 100
    print(f"Future Return: {future_return:.2f}")
    print(f"Future Return(%): {future_return_percent:.3f}%")
    # BACKTEST RESULT
    if final_signal in ["BUY", "STRONG BUY"]:
        if future_return > 0:
            prediction_result = "Correct"
        else:
            prediction_result = "Incorrect"
    elif final_signal in ["SELL", "STRONG SELL"]:
        if future_return < 0:
            prediction_result = "Correct"
        else:
            prediction_result = "Incorrect"
    else:
        if -1 <= future_return_percent <= 1:
            prediction_result = "Correct"
        else:
            prediction_result = "Incorrect"
    print(f"Prediction Result: {prediction_result}")
    backtest_summary.append({"Date": date, "Current Prices": current_price, "Final Signal": final_signal, 
                     "Technical Score": signal_score, "Future Prices": future_price, 
                     "Future Return (%)": future_return_percent, "Prediction Result": prediction_result})

#end of the loop 
backtest_dataframe_summary = pd.DataFrame(backtest_summary)
backtest_dataframe_indicators = pd.DataFrame(backtest_indicators)
backtest_results = pd.merge(backtest_dataframe_summary, backtest_dataframe_indicators, on="Date")
return_per_signal = (backtest_results.groupby("RSI Signal")["Future Return (%)"].mean())


#accuracy of RSI 
rsi_signal_counts = (backtest_results["RSI Signal"].value_counts())
prediction_counts = backtest_results["Prediction Result"].value_counts()
print(f"Average Future Returns by RSI Signals {return_per_signal}")
print(f"Signal Counts {rsi_signal_counts}")
print(f"Prediction Counts {prediction_counts}")

correct_predictions = (backtest_results["Prediction Result"] == "Correct").sum()
total_predictions = (backtest_results["Prediction Result"].isin(["Correct", "Incorrect"])).sum()
if total_predictions > 0:
    accuracy = (correct_predictions / total_predictions) * 100
    print(f"Prediction Accuracy: {accuracy:.2f}%")
else:
    print("Prediction Accuracy: No valid predictions available.")
print()
print()
return_per_final_signal = (backtest_results.groupby("Final Signal")["Future Return (%)"].mean())
print(f"Average Future Return by Final Technical Signal: {return_per_final_signal}")
final_signal_counts = (backtest_results["Final Signal"].value_counts())
print(f"Number of Times Each Final Signal Appeared: {final_signal_counts}")
print()
print()
print("=" * 50)
print(f"SUMMARY OF {symbol}")
print("=" * 50)
overall_average_return = backtest_results["Future Return (%)"].mean()
print(f"Overall Average: {overall_average_return:.2f}%")
if overall_average_return > 0:
    print(f"Across 20 day periods in the history of {symbol}, there has been an  increase of {overall_average_return:.2f}%")
elif overall_average_return < 0:
    print(f"Across 20 day periods in the history of {symbol}, there has been a decrease of {overall_average_return:.2f}%")
else:
    print(f"Across 20 day periods in the history of {symbol}, it has remained around the same price moving only {overall_average_return:.2f}%")
print()
signal_comparison = (return_per_final_signal - overall_average_return)
print(f"Signal Comparison: {signal_comparison}")
print()
final_signal_performance = backtest_results.groupby("Final Signal")["Future Return (%)"].agg(["mean", "count"])
print(f"Final Signal Performance: {final_signal_performance}")
print()   
winrate_by_final_signal = backtest_results.groupby("Final Signal")["Prediction Result"].apply(lambda x: (x == "Correct").mean() * 100)
print(f"Win Rate by Final Signal: {winrate_by_final_signal}")
print()

backtest_results["Strategy Return (%)"] = np.where(backtest_results["Final Signal"].str.contains("BUY"),
backtest_results["Future Return (%)"], np.where(backtest_results["Final Signal"].str.contains("SELL"),
-backtest_results["Future Return (%)"], 0 ))
backtest_results["Cumulative Strategy Return (%)"] = ((1 + backtest_results["Strategy Return (%)"] / 100).cumprod() - 1) * 100
print(f"Cumulative Strategy Return: {backtest_results['Cumulative Strategy Return (%)'].iloc[-1]:.2f}%")

backtest_results["Strategy Return (%)"] = (backtest_results["Cumulative Strategy Return (%)"].cummax())
backtest_results["Drawdown (%)"] = (backtest_results["Cumulative Strategy Return (%)"]- backtest_results["Strategy Peak (%)"])
print(f"Maximum Drawdown: {backtest_results['Drawdown (%)'].min():.2f}%")