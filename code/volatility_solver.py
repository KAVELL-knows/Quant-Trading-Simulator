#Volatility Solver
import math
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime


def volatility_solver_purpose():
    print("PURPOSE")
    print("")
    print("Implied volatility is the volatility value that makes the theoretical Black-Scholes option price equal to the observed market option price.")
    print("")
    print("Instead of calculating an option price from a known volatility, this program works backwards from the market price to estimate volatility.")
    print("")


def volatility_solver_assumptions():
    print("ASSUMPTIONS")
    print("")
    print("1. The option can only be exercised at expiration, not before.")
    print("2. No transaction costs or taxes.")
    print("3. No arbitrage under the model's idealized market assumptions.")
    print("4. The underlying asset can be traded continuously.")
    print("5. Constant risk-free interest rate.")
    print("6. Constant volatility.")
    print("7. Continuously compounded stock returns are normally distributed, making future stock prices lognormally distributed.")
    print("8. No dividends.")

def volatility_solver_method():
    print("METHOD: BISECTION")
    print("")
    print("1. Establish lower and upper volatility estimates.")
    print("2. Calculate the midpoint between the two estimates.")
    print("3. Calculate the theoretical option price using that volatility.")
    print("4. Compare the theoretical price with the observed market price.")
    print("5. Narrow the volatility range according to the price difference.")
    print("6. Repeat until the price difference is sufficiently small.")

def volatility_solver_limitations():
    print("LIMITATIONS")
    print("")
    print("1. Implied volatility is an estimate, not a guarantee of future volatility.")
    print("2. Market option prices may contain bid-ask spreads and pricing noise.")
    print("3. Real markets may violate the model's assumptions.")
    print("4. Volatility can vary with strike price and expiration date.")
    print("5. This implementation does not account for dividends.")
    print("6. A market price outside the model's theoretical bounds cannot produce a valid implied volatility under the specified assumptions.")


def normal_distribution(x):
    return (1 + math.erf(x / math.sqrt(2))) / 2


def black_scholes_price(stock_price, strike_price, time_to_expiration, risk_free_rate, volatility, option_type):
    d1 = (math.log(stock_price / strike_price) + (risk_free_rate + volatility ** 2 / 2) * time_to_expiration) / (volatility * math.sqrt(time_to_expiration))
    d2 = d1 - volatility * math.sqrt(time_to_expiration)

    if option_type == "CALL":
        option_price = (stock_price * normal_distribution(d1) - strike_price * math.exp(-risk_free_rate * time_to_expiration) * normal_distribution(d2))
    elif option_type == "PUT":
        option_price = (
            strike_price * math.exp(-risk_free_rate * time_to_expiration) * normal_distribution(-d2) - stock_price * normal_distribution(-d1))
    else:
        raise ValueError("Option type must be CALL or PUT.")
    return option_price


def calculate_implied_volatility(stock_price, strike_price, time_to_expiration, risk_free_rate, market_option_price, option_type):
    if stock_price <= 0:
        raise ValueError("Stock price must be greater than zero.")
    if strike_price <= 0:
        raise ValueError("Strike price must be greater than zero.")
    if time_to_expiration <= 0:
        raise ValueError("Time to expiration must be greater than zero.")
    if market_option_price < 0:
        raise ValueError("Market option price cannot be negative.")
    option_type = option_type.upper()

    if option_type not in ["CALL", "PUT"]:
        raise ValueError("Option type must be CALL or PUT.")
    discounted_strike_price = strike_price * math.exp(-risk_free_rate * time_to_expiration)

    if option_type == "CALL":
        minimum_option_price = max(stock_price - discounted_strike_price, 0)
        maximum_option_price = stock_price

    else:
        minimum_option_price = max(discounted_strike_price - stock_price, 0)
        maximum_option_price = discounted_strike_price

    if market_option_price < minimum_option_price:
        raise ValueError("Market option price is below the theoretical minimum.")

    if market_option_price > maximum_option_price:
        raise ValueError("Market option price is above the theoretical maximum.")

    if market_option_price == minimum_option_price:
        raise ValueError("The market price is at the theoretical minimum, therefore strictly positive implied volatility may not exist.")

    lower_volatility = 0.00000000000001
    upper_volatility = 1.0

    while upper_volatility < 100:

        theoretical_price = black_scholes_price(stock_price, strike_price, time_to_expiration, risk_free_rate, upper_volatility, option_type)

        if theoretical_price >= market_option_price:
            break

        upper_volatility *= 2
    else:
        raise ValueError("Could not find a suitable volatility range.")

    #Bisection method
    price_tolerance = 0.000001

    for i in range(100):
        middle_volatility = (lower_volatility + upper_volatility) / 2
        theoretical_price = black_scholes_price(stock_price, strike_price, time_to_expiration, risk_free_rate, middle_volatility, option_type)
        price_difference = abs(theoretical_price - market_option_price)

        if price_difference < price_tolerance:
            return middle_volatility
        if theoretical_price < market_option_price:
            lower_volatility = middle_volatility
        else:
            upper_volatility = middle_volatility
    raise ValueError("The solver did not reach the required price tolerance.")

try:
    stock_price = float(input("Enter the current stock price: "))
    strike_price = float(input("Enter the strike price: "))
    time_to_expiration = float(input("Enter the time to expiration in years: "))
    risk_free_rate = float(input("Enter the risk-free interest rate as a decimal (e.g. 0.33 for 33%): "))
    market_option_price = float(input("Enter the market option price: "))
    option_type = input("Enter the option type (CALL or PUT): ").upper()

    implied_volatility = calculate_implied_volatility(stock_price, strike_price, time_to_expiration, risk_free_rate, market_option_price, option_type)

    print("")
    print("-" * 20)
    print("IMPLIED VOLATILITY RESULTS")
    print("-" * 20)
    print(f"Option Type: {option_type}")
    print(f"Market Option Price: ${market_option_price:.2f}")
    print(f"Implied Volatility: {implied_volatility:.2%}")

    volatilities = []
    option_prices = []

    for i in range(1, 101):
        simulated_volatility = i / 100
        theoretical_price = black_scholes_price(stock_price, strike_price, time_to_expiration, risk_free_rate, simulated_volatility, option_type)

        volatilities.append(simulated_volatility * 100)
        option_prices.append(theoretical_price)

    strike_prices = [80, 90, 100, 110, 120]
    market_option_prices = [22.50, 15.20, 10.45, 6.80, 4.10]
    implied_volatilities = []

    for i in range(len(strike_prices)):
        current_strike_price = strike_prices[i]
        current_market_price = market_option_prices[i]

        try:
            volatility = calculate_implied_volatility(stock_price, current_strike_price, time_to_expiration, risk_free_rate, current_market_price, option_type)

            implied_volatilities.append(volatility)

        except ValueError as error:
            print(f"Strike ${current_strike_price}: {error}")
            implied_volatilities.append(None)

    print("")
    print("-" * 40)
    print("IMPLIED VOLATILITY BY STRIKE PRICE")
    print("-" * 40)

    for i in range(len(strike_prices)):
        if implied_volatilities[i] is not None:
            print(f"Strike Price: ${strike_prices[i]:.2f} | "
                f"Implied Volatility: {implied_volatilities[i]:.2%}")

        else:
            print(f"Strike Price: ${strike_prices[i]:.2f} | No valid result")

    plt.figure()
    plt.plot(volatilities, option_prices, label="Black-Scholes Theoretical Price")
    plt.axhline(y=market_option_price, label="Market Option Price", linestyle="--")
    plt.axvline(x=implied_volatility * 100, label="Implied Volatility", linestyle=":")
    plt.scatter(implied_volatility * 100, market_option_price, color="red", s=100, label="Implied Volatility Point", zorder=5)

    plt.annotate(f"Implied Volatility: {implied_volatility:.2%}", (implied_volatility * 100, market_option_price), xytext=(15, 15), textcoords="offset points")

    plt.xlabel("Volatility (%)")
    plt.ylabel("Option Price ($)")
    plt.title("Implied Volatility and Option Price Relationship")
    plt.legend()
    plt.grid(True)
    plt.show()

    valid_strike_prices = []
    valid_implied_volatilities = []

    for i in range(len(strike_prices)):
        if implied_volatilities[i] is not None:
            valid_strike_prices.append(strike_prices[i])
            valid_implied_volatilities.append(implied_volatilities[i] * 100)

    plt.figure()
    plt.plot(valid_strike_prices, valid_implied_volatilities, marker="o", label="Implied Volatility")

    plt.xlabel("Strike Price ($)")
    plt.ylabel("Implied Volatility (%)")
    plt.title("Implied Volatility Smile")
    plt.legend()
    plt.grid(True)
    plt.show()

except ValueError as error:
    print("")
    print("Unable to calculate implied volatility.")
    print(f"Reason: {error}")

#using the real options values
symbol = input("Enter stock symbol: ").upper()
stock = yf.Ticker(symbol)

expiration_dates = stock.options

expiration_date = input("Enter an expiration date: ")
options_chain = stock.option_chain(expiration_date)

calls = options_chain.calls
puts = options_chain.puts

call_strikes = calls["strike"]
call_prices = calls["lastPrice"]
put_prices = puts["lastPrice"]

call_bid = calls["bid"]
call_ask = calls["ask"]

put_bid = puts["bid"]
put_ask = puts["ask"]

call_midpoint = (calls["bid"] + calls["ask"]) / 2
put_midpoint = (puts["bid"] + puts["ask"]) / 2

#add midpint to the calls and puts dataframes
calls["midpoint"] = call_midpoint
puts["midpoint"] = put_midpoint


print(expiration_dates)
print(calls)
print(calls.head())
print(puts)
print(puts.head())
print(calls.columns)
print(call_strikes)
print(call_prices)
print(put_prices)
print(call_midpoint.head())
print(put_midpoint.head())

print(calls[["strike", "bid", "ask", "midpoint"]].head())
print(puts[["strike", "bid", "ask", "midpoint"]].head())

stock_data = stock.history(period="5d")
stock_price = stock_data["Close"].iloc[-1]
print(stock_price)


current_date = datetime.now().date()
expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d").date()

days_to_expiration = (expiration_date - current_date).days
time_to_expiration = days_to_expiration / 365

calls = calls.dropna(subset=["bid", "ask", "strike"])
puts = puts.dropna(subset=["bid", "ask", "strike"])

calls = calls[(calls["bid"] > 0) & (calls["ask"] > 0) & (calls["ask"] >= calls["bid"])].copy()
puts = puts[(puts["bid"] > 0) & (puts["ask"] > 0) & (puts["ask"] >= puts["bid"])].copy()

calls["midpoint"] = (calls["bid"] + calls["ask"]) / 2
puts["midpoint"] = (puts["bid"] + puts["ask"]) / 2

print("Valid call contracts:", len(calls))
print("Valid put contracts:", len(puts))


print(calls[["strike", "bid", "ask", "midpoint"]].head())
print(puts[["strike", "bid", "ask", "midpoint"]].head())


if not calls.empty:

    first_call = calls.iloc[0]

    call_strike_price = float(first_call["strike"])
    call_market_option_price = float(first_call["midpoint"])

    try:
        call_implied_volatility = calculate_implied_volatility(stock_price, call_strike_price, time_to_expiration, risk_free_rate, call_market_option_price, "CALL")
        print("")
        print("FIRST CALL CONTRACT")
        print("-------------------")
        print(f"Strike Price: ${call_strike_price:.2f}")
        print(f"Market Price: ${call_market_option_price:.2f}")
        print(f"Implied Volatility: {call_implied_volatility:.2%}")

    except ValueError as error:
        print(f"Could not calculate implied volatility: {error}")

else:
    print("No valid call contracts available.")

#calc contract for every call
call_implied_volatilities = []

for i, contract in calls.iterrows():

    call_strike_price = float(contract["strike"])
    call_market_option_price = float(contract["midpoint"])

    try:
        implied_volatility = calculate_implied_volatility(stock_price, call_strike_price, time_to_expiration, risk_free_rate, call_market_option_price, "CALL")

    except ValueError:
        implied_volatility = None
    call_implied_volatilities.append(implied_volatility)

calls["calculated_implied_volatility"] = call_implied_volatilities
print("")
print("CALL IMPLIED VOLATILITIES")
print("-------------------------")
print(calls[["strike", "midpoint", "calculated_implied_volatility"]].head(10))


#implied volatility for every put contract
put_implied_volatilities = []

for index, contract in puts.iterrows():

    put_strike_price = float(contract["strike"])
    put_market_option_price = float(contract["midpoint"])

    try:
        implied_volatility = calculate_implied_volatility(stock_price, put_strike_price, time_to_expiration, risk_free_rate, put_market_option_price, "PUT")
    except ValueError:
        implied_volatility = None
    put_implied_volatilities.append(implied_volatility)


puts["calculated_implied_volatility"] = put_implied_volatilities
print("")
print("PUT IMPLIED VOLATILITIES")
print("------------------------")
print(puts[["strike", "midpoint", "calculated_implied_volatility"]].head(10))

#plotting begins
calls_plot = calls.dropna(subset=["calculated_implied_volatility"]).copy()
puts_plot = puts.dropna(subset=["calculated_implied_volatility"]).copy()

calls_plot = calls_plot.sort_values("strike")
puts_plot = puts_plot.sort_values("strike")

plt.figure(figsize=(10, 6))
plt.plot(calls_plot["strike"], calls_plot["calculated_implied_volatility"] * 100, marker="o", label="Call Implied Volatility")

plt.plot(puts_plot["strike"], puts_plot["calculated_implied_volatility"] * 100, marker="o", label="Put Implied Volatility")

plt.xlabel("Strike Price ($)")
plt.ylabel("Implied Volatility (%)")
plt.title("Implied Volatility Smile - " + symbol)

plt.legend()
plt.grid(True)
plt.show()


# Prepare call and put data for plotting
calls_plot = calls.dropna(subset=["calculated_implied_volatility"]).copy()
puts_plot = puts.dropna(subset=["calculated_implied_volatility"]).copy()

# Remove zero or negative implied volatility values
calls_plot = calls_plot[calls_plot["calculated_implied_volatility"] > 0].copy()
puts_plot = puts_plot[puts_plot["calculated_implied_volatility"] > 0].copy()


# Sort contracts by strike price
calls_plot = calls_plot.sort_values("strike")
puts_plot = puts_plot.sort_values("strike")


# Plot implied volatility smile
plt.figure(figsize=(12, 7))
if not calls_plot.empty:
    plt.plot(calls_plot["strike"], calls_plot["calculated_implied_volatility"] * 100, marker="o", label="Call Implied Volatility")

# Plot put implied volatility
if not puts_plot.empty:
    plt.plot(puts_plot["strike"], puts_plot["calculated_implied_volatility"] * 100, marker="o", label="Put Implied Volatility")

plt.xlabel("Strike Price ($)")
plt.ylabel("Implied Volatility (%)")
plt.title(f"Implied Volatility Smile/Skew - {symbol} - {expiration_date}")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


#REAL OPTIONS IMPLIED VOLATILITY SURFACE
symbol = input("Enter stock symbol: ").upper()
stock = yf.Ticker(symbol)
expiration_dates = stock.options

print("\nAVAILABLE EXPIRATION DATES")
for date in expiration_dates:
    print(date)

selected_expirations = expiration_dates[:8]
print("\nSelected expiration dates:")
print(selected_expirations)

stock_data = stock.history(period="5d")
stock_price = stock_data["Close"].iloc[-1]
risk_free_rate = 0.0472
implied_volatility_data = []

for expiration in selected_expirations:
    print(f"\nAnalysing expiration: {expiration}")
    expiration_date = datetime.strptime(expiration, "%Y-%m-%d").date()
    current_date = datetime.now().date()

    days_to_expiration = (expiration_date - current_date).days
    if days_to_expiration <= 0:
        continue
    time_to_expiration = days_to_expiration / 365
    options_chain = stock.option_chain(expiration)

    calls = options_chain.calls.copy()
    puts = options_chain.puts.copy()

    calls = calls.dropna(subset=["bid", "ask", "strike"])
    puts = puts.dropna(subset=["bid", "ask", "strike"])

    calls = calls[(calls["bid"] > 0) & (calls["ask"] > 0) & (calls["ask"] >= calls["bid"])].copy()
    puts = puts[(puts["bid"] > 0) & (puts["ask"] > 0) & (puts["ask"] >= puts["bid"])].copy()

    calls["midpoint"] = (calls["bid"] + calls["ask"]) / 2
    puts["midpoint"] = (puts["bid"] + puts["ask"]) / 2


    #calculate implied volatility for calls
    for index, contract in calls.iterrows():

        strike_price = float(contract["strike"])
        market_option_price = float(contract["midpoint"])

        try:
            implied_volatility = calculate_implied_volatility(stock_price, strike_price, time_to_expiration, risk_free_rate, market_option_price, "CALL")

            implied_volatility_data.append({"Expiration": expiration, "Days to Expiration": days_to_expiration, "Strike": strike_price, "Option Type": "CALL" "Implied Volatility": implied_volatility})

        except ValueError:
            continue

    for index, contract in puts.iterrows():
        strike_price = float(contract["strike"])
        market_option_price = float(contract["midpoint"])
        try:
            implied_volatility = calculate_implied_volatility(stock_price, strike_price, time_to_expiration, risk_free_rate, market_option_price, "PUT")

            implied_volatility_data.append({"Expiration": expiration, "Days to Expiration": days_to_expiration, "Strike": strike_price, "Option Type": "PUT", "Implied Volatility": implied_volatility})

        except ValueError:
            continue

implied_volatility_surface = pd.DataFrame(implied_volatility_data)
print("\nIMPLIED VOLATILITY SURFACE DATA")
print(implied_volatility_surface.head(20))
print("\nTotal contracts analysed:",
      len(implied_volatility_surface))

surface_data = implied_volatility_surface.groupby(["Days to Expiration", "Strike"])["Implied Volatility"].mean().reset_index()

if len(surface_data) >= 3:
    figure = plt.figure(figsize=(12, 8))
    axis = figure.add_subplot(111, projection="3d")
    surface = axis.plot_trisurf(surface_data["Strike"], surface_data["Days to Expiration"], surface_data["Implied Volatility"] * 100, cmap="viridis", edgecolor="none")

    axis.set_xlabel("Strike Price ($)")
    axis.set_ylabel("Days to Expiration")
    axis.set_zlabel("Implied Volatility (%)")

    axis.set_title(f"Implied Volatility Surface - {symbol}")
    figure.colorbar(surface, ax=axis, label="Implied Volatility (%)", shrink=0.6)

    plt.tight_layout()
    plt.show()
else:
    print("Not enough valid contracts to create the 3D surface.")
