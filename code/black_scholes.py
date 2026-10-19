#Blackscholes Model 
import math
import matplotlib.pyplot as plt
def black_scholes_assumptions():
    print("Below are the Assumptions of the Black Scholes listed")
    print("1. European exercise style: Options can only be exercised on the exact expiration date, not before.")
    print("2. Constant volatility and interest rates: Volatility and the risk-free rate remain steady over the life of the option.")
    print("3. No dividends: The underlying stock does not pay out dividends during the option term (though modified versions adjust for this).")
    print("4. Frictionless market: There are no transaction costs or taxes, and buying/selling fractional shares is allowed.")

def black_scholes_main_uses():
    print("Below are the main uses of the Black ")
    print("'1. Fair value pricing: Traders use it to see if a market option is overvalued or undervalued.")
    print("2. Implied volatility: Traders reverse-engineer the formula using current market prices to find out what volatility the market expects.")
    print("3.  It helps calculate the Option Greeks (like Delta and Gamma) to manage hedging strategies.")


while True:
    try:
        stock_price = float(input("Enter the current stock price: "))
        if not math.isfinite(stock_price):
            print("You enterred an INFINITE VALUE. Please dont!")
            continue
        if stock_price > 0:
            break
        print("Please re-enter a stock price greater than 0")
    except ValueError:
        print("Please re-enter a NUMERICAL VALUE for the stock price that is greater than 0")


while True:
    try:
        strike_price = float(input("Enter the strike price: "))
        if not math.isfinite(strike_price):
            print("You enterred an INFINITE VALUE. Please dont!")
            continue
        if strike_price > 0:
            break
        print("Please re-enter a strike price greater than 0")
    except ValueError:
        print("Please re-enter a NUMERICAL VALUE for the strike price that is greater than 0")

while True:
    try:
        time_to_expiration = float(input("Enter the time to expiration in years: "))
        if not math.isfinite(time_to_expiration):
            print("You enterred an INFINITE VALUE. Please dont!")
            continue
        if time_to_expiration > 0:
            break
        print("Please re-enter a time to expiration price greater than 0")
    except ValueError:
        print("Please re-enter a NUMERICAL VALUE for the time to expiration that is greater than 0")

while True:
    try:
        risk_free_rate = float(input("Enter the risk-free interest rate (e.g. 0.10 for 10%): "))
        if not math.isfinite(risk_free_rate):
            print("You enterred an INFINITE VALUE. Please dont!")
            continue
        if risk_free_rate > -1:
            break
        print("Please re-enter a risk-free interest rate greater than -100%")
    except ValueError:
        print("Please re-enter a NUMERICAL VALUE for the risk-free interest rate that is greater than -100%")
    
while True:
    try:
        volatility = float(input("Enter the volatility (e.g. 0.10 for 10%): "))
        if not math.isfinite(volatility):
            print("You enterred an INFINITE VALUE. Please dont!")
            continue
        if volatility > 0:
            break
        print("Please re-enter a volatility greater than 0")
    except ValueError:
        print("Please re-enter a NUMERICAL VALUE for the volatility that is greater than 0")

d1 = (math.log(stock_price / strike_price) + (risk_free_rate + (volatility ** 2) / 2) * time_to_expiration) / (volatility * math.sqrt(time_to_expiration))
d2 = d1 - (volatility * math.sqrt(time_to_expiration))
print("")
print(f"The Asset Distribution Adjuster (d1):{d1:.4f}")
print(f"The Probability of Exercise (d2): {d2:.4f}")

def normal_distribution(x):
    return (1 + math.erf(x / math.sqrt(2))) / 2

Normal_d1 = normal_distribution(d1)
Normal_d2 = normal_distribution(d2)
print(f"Normally Distributed (d1): {Normal_d1:.4f}")
print(f"Normally Distributed (d2): {Normal_d2:.4f}")

Normal_negd2 = normal_distribution(-d2) 
Normal_negd1 = normal_distribution(-d1)

#C = SN(d1) - K(e^-rT)N(d2)
call_option_pricing = (stock_price * Normal_d1)-(strike_price * math.exp(-risk_free_rate * time_to_expiration) * Normal_d2)
print(f"Theoretical Call Option Price: ${call_option_pricing:.4f}")

#P = K(e^-rT) N(-d2) SN(-d1)
put_option_pricing = (strike_price * math.exp(-risk_free_rate * time_to_expiration)) * Normal_negd2 - (stock_price * Normal_negd1)
print(f"Theoretical Put Option Price: ${put_option_pricing:.4f}")

# Put-Call Parity
parity_left_side = call_option_pricing - put_option_pricing
parity_right_side = stock_price - (strike_price * math.exp(-risk_free_rate * time_to_expiration))
print("Put-Call Parity Verification")
print(f"Left Side: {parity_left_side:.4f}")
print(f"Right Side: {parity_right_side:.4f}")
if math.isclose(parity_left_side, parity_right_side, rel_tol=1e-9):
    print("Put-Call Parity: VERIFIED")
else:
    print("Put-Call Parity: FAILED")

#greek delta option
print("")
call_delta = Normal_d1
put_delta = Normal_d1 - 1
print(f"Call Option Delta: {call_delta:.4f}")
print(f"Put Option Delta: {put_delta:.4f}")
print("")
#Gamma 
def normal_density(x):
    return (math.exp(-0.5 * x ** 2)) / math.sqrt(2 * math.pi)

gamma = normal_density(d1) / (stock_price * volatility * math.sqrt(time_to_expiration))
print(f"Call Gamma: {gamma:.4f}")
print(f"Put Gamma: {gamma:.4f}")

#Call Theta

call_theta = (- (stock_price * normal_density(d1) * volatility) / (2 * math.sqrt(time_to_expiration))) - (risk_free_rate * strike_price * math.exp(-risk_free_rate * time_to_expiration) * Normal_d2)
put_theta = (- (stock_price * normal_density(d1) * volatility) / (2 * math.sqrt(time_to_expiration))) + (risk_free_rate * strike_price * math.exp(-risk_free_rate * time_to_expiration) * Normal_negd2)
print(f"Call Theta: {call_theta:.4f}")
print(f"Put Theta: {put_theta:.4f}")
call_daily_theta = call_theta / 365
put_daily_theta = put_theta / 365
print(f"Call Daily Theta: {call_daily_theta:.4f}")
print(f"Put Daily Theta: {put_daily_theta:.4f}")

#Vega
vega = stock_price * normal_density(d1) * math.sqrt(time_to_expiration)
print(f"Call Vega: {vega:.4f}")
print(f"Put Vega: {vega:.4f}")
call_vega_1_percent = vega / 100
put_vega_1_percent = vega / 100
print(f"Call Vega for 1% change in volatility: {call_vega_1_percent:.4f}")
print(f"Put Vega for 1% change in volatility: {put_vega_1_percent:.4f}")

#Rho
call_rho = strike_price * time_to_expiration * math.exp(-risk_free_rate * time_to_expiration) * Normal_d2
put_rho = -strike_price * time_to_expiration * math.exp(-risk_free_rate * time_to_expiration) * Normal_negd2
print(f"Call Rho: {call_rho:.4f}")
print(f"Put Rho: {put_rho:.4f}")

call_rho_1_percent = call_rho / 100
put_rho_1_percent = put_rho / 100
print(f"Call Rho for 1% change in interest rate: {call_rho_1_percent:.4f}")
print(f"Put Rho for 1% change in interest rate: {put_rho_1_percent:.4f}")   


# Greeks Summary
print("")
print("=" * 51)
print("BLACK-SCHOLES GREEKS SUMMARY".center(51))
print("=" * 51)
print(f"{'Greek':<17}{'Call Option':>17}{'Put Option':>17}")
print("-" * 51)
print(f"{'Delta':<17}{call_delta:>17.4f}{put_delta:>17.4f}")
print(f"{'Gamma':<17}{gamma:>17.4f}{gamma:>17.4f}")
print(f"{'Theta':<17}{call_theta:>17.4f}{put_theta:>17.4f}")
print(f"{'Vega (1%)':<17}{call_vega_1_percent:>17.4f}{put_vega_1_percent:>17.4f}")
print(f"{'Rho (1%)':<17}{call_rho_1_percent:>17.4f}{put_rho_1_percent:>17.4f}")
print("-" * 51)


#Option Price Sensitivity Simulator
print("=" * 51)
print("STOCK PRICE SENSITIVITY SIMULATOR".center(51))
print("=" * 51)
print("")
starting_stock_price = float(input("Enter the starting stock price for sensitivity analysis: "))
ending_stock_price = float(input("Enter the ending stock price for sensitivity analysis: "))
price_increment = float(input("Enter the price increment for sensitivity analysis: "))


stock_prices = []
call_prices = []
put_prices = []

call_deltas = []
put_deltas = []
gammas = []
vegas = []
call_thetas = []
put_thetas = []
call_rhos = []
put_rhos = []

for i in range(int(starting_stock_price), int(ending_stock_price) + 1, int(price_increment)):
    simulated_d1 = (math.log(i / strike_price) + (risk_free_rate + (volatility ** 2) / 2) * time_to_expiration) / (volatility * math.sqrt(time_to_expiration))
    simulated_d2 = simulated_d1 - (volatility * math.sqrt(time_to_expiration))
    simulated_Normal_d1 = normal_distribution(simulated_d1)
    simulated_Normal_negd1 = normal_distribution(-simulated_d1)
    simulated_Normal_d2 = normal_distribution(simulated_d2)
    simulated_Normal_negd2 = normal_distribution(-simulated_d2)

    simulated_call_price = (i * simulated_Normal_d1) - (strike_price * math.exp(-risk_free_rate * time_to_expiration) * simulated_Normal_d2)
    simulated_put_price = (strike_price * math.exp(-risk_free_rate * time_to_expiration) * simulated_Normal_negd2) - (i * simulated_Normal_negd1)

    stock_prices.append(i)
    call_prices.append(simulated_call_price)
    put_prices.append(simulated_put_price)


    simulated_call_delta = simulated_Normal_d1
    simulated_put_delta = simulated_Normal_d1 - 1
    simulated_gamma = normal_density(simulated_d1) / (i * volatility * math.sqrt(time_to_expiration))

    simulated_vega = i * normal_density(simulated_d1) * math.sqrt(time_to_expiration)

    simulated_call_theta = (- (i * normal_density(simulated_d1) * volatility) / (2 * math.sqrt(time_to_expiration))) - (risk_free_rate * strike_price * math.exp(-risk_free_rate * time_to_expiration) * simulated_Normal_d2)
    simulated_put_theta = (- (i * normal_density(simulated_d1) * volatility) / (2 * math.sqrt(time_to_expiration))) + (risk_free_rate * strike_price * math.exp(-risk_free_rate * time_to_expiration) * simulated_Normal_negd2)

    simulated_call_rho = strike_price * time_to_expiration * math.exp(-risk_free_rate * time_to_expiration) * simulated_Normal_d2
    simulated_put_rho = -strike_price * time_to_expiration * math.exp(-risk_free_rate * time_to_expiration) * simulated_Normal_negd2

    call_deltas.append(simulated_call_delta)
    put_deltas.append(simulated_put_delta)
    gammas.append(simulated_gamma)
    vegas.append(simulated_vega)
    call_thetas.append(simulated_call_theta)
    put_thetas.append(simulated_put_theta)
    call_rhos.append(simulated_call_rho)
    put_rhos.append(simulated_put_rho)


    print("")
    print("-" * 51)
    print(f"{'Stock Price:':<15} ${i:>10.2f}")
    print("-" * 51)
    print(f"{'Call Price:':<15} ${simulated_call_price:>10.4f} | {'Put Price:':<12} ${simulated_put_price:>10.4f}")
    print("-" * 51)
    print(f"{'Call Delta:':<15} {simulated_call_delta:>10.4f} | {'Put Delta:':<12} {simulated_put_delta:>10.4f}")
    print("-" * 51)
    print(f"{'Gamma:':<15} {simulated_gamma:>10.4f} | {'Vega:':<12} {simulated_vega:>10.4f}")
    print("-" * 51)
    print(f"{'Call Theta:':<15} {simulated_call_theta:>10.4f} | {'Put Theta:':<12} {simulated_put_theta:>10.4f}")
    print("-" * 51)
    print(f"{'Call Rho:':<15} {simulated_call_rho:>10.4f} | {'Put Rho:':<12} {simulated_put_rho:>10.4f}")
    print("-" * 51)

#Stock Price Sensitivity Graph
fig, axes = plt.subplots(3, 2, figsize=(14, 12))

#Graph1 Option Prices
axes[0, 0].plot(stock_prices, call_prices, label="Call Price", color = "blue")
axes[0, 0].plot(stock_prices, put_prices, label="Put Price", color = "green")

axes[0, 0].set_title("Option Prices vs Stock Price")
axes[0, 0].set_xlabel("Stock Price ($)")
axes[0, 0].set_ylabel("Option Price ($)")

axes[0, 0].legend()
axes[0, 0].grid(True)

#Graph2 Delta
axes[0, 1].plot(stock_prices, call_deltas, label="Call Delta", color = "blue")
axes[0, 1].plot(stock_prices, put_deltas, label="Put Delta", color = "red")
axes[0, 1].set_title("Delta vs Stock Price")
axes[0, 1].set_xlabel("Stock Price ($)")
axes[0, 1].set_ylabel("Delta")
axes[0, 1].legend()
axes[0, 1].grid(True)

#Graph3 Gamma
plasma_color = plt.cm.plasma(0.5) 
axes[1, 0].plot(stock_prices, gammas, label="Gamma", color=plasma_color, linewidth=2.5)
axes[1, 0].set_title("Gamma vs Stock Price")
axes[1, 0].set_xlabel("Stock Price ($)")
axes[1, 0].set_ylabel("Gamma")
axes[1, 0].legend()
axes[1, 0].grid(True)

#Graph4 Vega
plasma_purple = plt.cm.plasma(0.1)
axes[1, 1].plot(stock_prices, vegas, label="Vega", color=plasma_purple, linewidth=2)
axes[1, 1].set_title("Vega vs Stock Price")
axes[1, 1].set_xlabel("Stock Price ($)")
axes[1, 1].set_ylabel("Vega")
axes[1, 1].legend()
axes[1, 1].grid(True)

#Graph5 Theta
vibrant_pink = plt.cm.plasma(0.55)
axes[2, 0].plot(stock_prices, call_thetas, label="Call Theta", color=vibrant_pink )
axes[2, 0].plot(stock_prices, put_thetas, label="Put Theta", color = "purple")
axes[2, 0].set_title("Theta vs Stock Price")
axes[2, 0].set_xlabel("Stock Price ($)")
axes[2, 0].set_ylabel("Theta")
axes[2, 0].legend()
axes[2, 0].grid(True)

#Graph6 Rho
axes[2, 1].plot(stock_prices, call_rhos, label="Call Rho", color = "cyan")
axes[2, 1].plot(stock_prices, put_rhos, label="Put Rho", color = "magenta")
axes[2, 1].set_title("Rho vs Stock Price")
axes[2, 1].set_xlabel("Stock Price ($)")
axes[2, 1].set_ylabel("Rho")
axes[2, 1].legend()
axes[2, 1].grid(True)

plt.tight_layout(pad=3.0, h_pad=4.0, w_pad=3.0)
plt.show()




# Volatility Sensitivity Simulator
print("=" * 51)
print("VOLATILITY SENSITIVITY SIMULATOR".center(51))
print("=" * 51)
print("")

starting_volatility = float(input("Enter the starting volatility for sensitivity analysis: "))
ending_volatility = float(input("Enter the ending volatility for sensitivity analysis: "))
volatility_increment = float(input("Enter the volatility increment for sensitivity analysis: "))


volatilities = []
call_prices_volatility = []
put_prices_volatility = []

call_deltas_volatility = []
put_deltas_volatility = []
gammas_volatility = []
vegas_volatility = []
call_thetas_volatility = []
put_thetas_volatility = []
call_rhos_volatility = []
put_rhos_volatility = []

for i in range(int(starting_volatility * 100), int(ending_volatility * 100) + 1, int(volatility_increment * 100)):
    simulated_volatility = i / 100
    simulated_d1 = (math.log(stock_price / strike_price) + (risk_free_rate + (simulated_volatility ** 2) / 2) * time_to_expiration) / (simulated_volatility * math.sqrt(time_to_expiration))
    simulated_d2 = simulated_d1 - (simulated_volatility * math.sqrt(time_to_expiration))

    simulated_Normal_d1 = normal_distribution(simulated_d1)
    simulated_Normal_negd1 = normal_distribution(-simulated_d1)
    simulated_Normal_d2 = normal_distribution(simulated_d2)
    simulated_Normal_negd2 = normal_distribution(-simulated_d2)

    simulated_call_price = (stock_price * simulated_Normal_d1) - (strike_price * math.exp(-risk_free_rate * time_to_expiration) * simulated_Normal_d2)
    simulated_put_price = (strike_price * math.exp(-risk_free_rate * time_to_expiration) * simulated_Normal_negd2) - (stock_price * simulated_Normal_negd1)

    volatilities.append(simulated_volatility)
    call_prices_volatility.append(simulated_call_price)
    put_prices_volatility.append(simulated_put_price)

    simulated_call_delta = simulated_Normal_d1
    simulated_put_delta = simulated_Normal_d1 - 1

    simulated_gamma = normal_density(simulated_d1) / (stock_price * simulated_volatility * math.sqrt(time_to_expiration))
    simulated_vega = stock_price * normal_density(simulated_d1) * math.sqrt(time_to_expiration)

    simulated_vega_1_percent = simulated_vega / 100
    
    simulated_call_theta = (-(stock_price * normal_density(simulated_d1) * simulated_volatility) / (2 * math.sqrt(time_to_expiration))) - (risk_free_rate * strike_price * math.exp(-risk_free_rate * time_to_expiration) * simulated_Normal_d2)
    simulated_put_theta = (-(stock_price * normal_density(simulated_d1) * simulated_volatility) / (2 * math.sqrt(time_to_expiration))) + (risk_free_rate * strike_price * math.exp(-risk_free_rate * time_to_expiration) * simulated_Normal_negd2)

    simulated_call_rho = strike_price * time_to_expiration * math.exp(-risk_free_rate * time_to_expiration) * simulated_Normal_d2
    simulated_put_rho = -strike_price * time_to_expiration * math.exp(-risk_free_rate * time_to_expiration) * simulated_Normal_negd2

    simulated_call_rho_1_percent = simulated_call_rho / 100
    simulated_put_rho_1_percent = simulated_put_rho / 100

    call_deltas_volatility.append(simulated_call_delta)
    put_deltas_volatility.append(simulated_put_delta)
    gammas_volatility.append(simulated_gamma)
    vegas_volatility.append(simulated_vega)
    call_thetas_volatility.append(simulated_call_theta)
    put_thetas_volatility.append(simulated_put_theta)
    call_rhos_volatility.append(simulated_call_rho)
    put_rhos_volatility.append(simulated_put_rho)

    print("")
    print("-" * 51)
    print(f"{'Volatility:':<15} {simulated_volatility:>8.2%}")
    print("-" * 51)
    print(f"{'Call Price:':<15} ${simulated_call_price:>10.4f} | {'Put Price:':<12} ${simulated_put_price:>10.4f}")
    print("-" * 51)
    print(f"{'Call Delta:':<15} {simulated_call_delta:>10.4f} | {'Put Delta:':<12} {simulated_put_delta:>10.4f}")
    print("-" * 51)
    print(f"{'Gamma:':<15} {simulated_gamma:>10.4f} | {'Vega:':<12} {simulated_vega:>10.4f}")
    print("-" * 51)
    print(f"{'Call Theta:':<15} {simulated_call_theta:>10.4f} | {'Put Theta:':<12} {simulated_put_theta:>10.4f}")
    print("-" * 51)
    print(f"{'Call Rho:':<15} {simulated_call_rho:>10.4f} | {'Put Rho:':<12} {simulated_put_rho:>10.4f}")
    print("-" * 51)


#Volatility Sensitivity Graph
fig, axes = plt.subplots(3, 2, figsize=(14, 12))

#Graph1 Option Prices
axes[0, 0].plot(volatilities, call_prices_volatility, label="Call Price", color = "blue")
axes[0, 0].plot(volatilities, put_prices_volatility, label="Put Price", color = "green")

axes[0, 0].set_title("Option Prices vs Volatility")
axes[0, 0].set_xlabel("Volatility")
axes[0, 0].set_ylabel("Option Price ($)")

axes[0, 0].legend()
axes[0, 0].grid(True)

#Graph2 Delta
axes[0, 1].plot(volatilities, call_deltas_volatility, label="Call Delta", color = "blue")
axes[0, 1].plot(volatilities, put_deltas_volatility, label="Put Delta", color = "red")
axes[0, 1].set_title("Delta vs Volatility")
axes[0, 1].set_xlabel("Volatility")
axes[0, 1].set_ylabel("Delta")
axes[0, 1].legend()
axes[0, 1].grid(True)

#Graph3 Gamma
plasma_color = plt.cm.plasma(0.5) 
axes[1, 0].plot(volatilities, gammas_volatility, label="Gamma", color=plasma_color, linewidth=2.5)
axes[1, 0].set_title("Gamma vs Volatility")
axes[1, 0].set_xlabel("Volatility")
axes[1, 0].set_ylabel("Gamma")
axes[1, 0].legend()
axes[1, 0].grid(True)

#Graph4 Vega
plasma_purple = plt.cm.plasma(0.1)
axes[1, 1].plot(volatilities, vegas_volatility, label="Vega", color=plasma_purple, linewidth=2)
axes[1, 1].set_title("Vega vs Volatility")
axes[1, 1].set_xlabel("Volatility")
axes[1, 1].set_ylabel("Vega")
axes[1, 1].legend()
axes[1, 1].grid(True)

#Graph5 Theta
vibrant_pink = plt.cm.plasma(0.55)
axes[2, 0].plot(volatilities, call_thetas_volatility, label="Call Theta", color=vibrant_pink )
axes[2, 0].plot(volatilities, put_thetas_volatility, label="Put Theta", color = "purple")
axes[2, 0].set_title("Theta vs Volatility")
axes[2, 0].set_xlabel("Volatility")
axes[2, 0].set_ylabel("Theta")
axes[2, 0].legend()
axes[2, 0].grid(True)

#Graph6 Rho
axes[2, 1].plot(volatilities, call_rhos_volatility, label="Call Rho", color = "cyan")
axes[2, 1].plot(volatilities, put_rhos_volatility, label="Put Rho", color = "magenta")
axes[2, 1].set_title("Rho vs Volatility")
axes[2, 1].set_xlabel("Volatility")
axes[2, 1].set_ylabel("Rho")
axes[2, 1].legend()
axes[2, 1].grid(True)

plt.tight_layout(pad=3.0, h_pad=4.0, w_pad=3.0)
plt.show()


# Time-to-Expiration Sensitivity Simulator
print("=" * 51)
print("TIME-TO-EXPIRATION SENSITIVITY SIMULATOR".center(51))
print("=" * 51)
print("")

starting_time = float(input("Enter the starting time to expiration in years: "))
ending_time = float(input("Enter the ending time to expiration in years: "))
time_increment = float(input("Enter the time increment in years: "))

times = []
call_price_time = []
put_price_time = []

call_deltas_time = []
put_deltas_time = []
gammas_time = []
vegas_time = []
call_thetas_time = []
put_thetas_time = []
call_rhos_time = []
put_rhos_time = []

for i in range(int(starting_time * 100), int(ending_time * 100) + 1, int(time_increment * 100)):
    simulated_time = i / 100

    simulated_d1 = (math.log(stock_price / strike_price) + (risk_free_rate + (volatility ** 2) / 2) * simulated_time) / (volatility * math.sqrt(simulated_time))
    simulated_d2 = simulated_d1 - (volatility * math.sqrt(simulated_time))

    simulated_Normal_d1 = normal_distribution(simulated_d1)
    simulated_Normal_negd1 = normal_distribution(-simulated_d1)
    simulated_Normal_d2 = normal_distribution(simulated_d2)
    simulated_Normal_negd2 = normal_distribution(-simulated_d2)

    simulated_call_price = (stock_price * simulated_Normal_d1) - (strike_price * math.exp(-risk_free_rate * simulated_time) * simulated_Normal_d2)
    simulated_put_price = (strike_price * math.exp(-risk_free_rate * simulated_time) * simulated_Normal_negd2) - (stock_price * simulated_Normal_negd1)

    times.append(simulated_time)
    call_price_time.append(simulated_call_price)
    put_price_time.append(simulated_put_price)

    simulated_call_delta = simulated_Normal_d1
    simulated_put_delta = simulated_Normal_d1 - 1

    simulated_gamma = normal_density(simulated_d1) / (stock_price * volatility * math.sqrt(simulated_time))
    simulated_vega = stock_price * normal_density(simulated_d1) * math.sqrt(simulated_time)

    simulated_vega_1_percent = simulated_vega / 100

    simulated_call_theta = (-(stock_price * normal_density(simulated_d1) * volatility) / (2 * math.sqrt(simulated_time))) - (risk_free_rate * strike_price * math.exp(-risk_free_rate * simulated_time) * simulated_Normal_d2)
    simulated_put_theta = (-(stock_price * normal_density(simulated_d1) * volatility) / (2 * math.sqrt(simulated_time))) + (risk_free_rate * strike_price * math.exp(-risk_free_rate * simulated_time) * simulated_Normal_negd2)

    simulated_call_rho = strike_price * simulated_time * math.exp(-risk_free_rate * simulated_time) * simulated_Normal_d2
    simulated_put_rho = -strike_price * simulated_time * math.exp(-risk_free_rate * simulated_time) * simulated_Normal_negd2

    simulated_call_rho_1_percent = simulated_call_rho / 100
    simulated_put_rho_1_percent = simulated_put_rho / 100


    call_deltas_time.append(simulated_call_delta)
    put_deltas_time.append(simulated_put_delta)
    gammas_time.append(simulated_gamma)
    vegas_time.append(simulated_vega)
    call_thetas_time.append(simulated_call_theta)
    put_thetas_time.append(simulated_put_theta)
    call_rhos_time.append(simulated_call_rho)
    put_rhos_time.append(simulated_put_rho)
    
    print("")
    print("-" * 51)
    print(f"{'Time to Expiration:':<22} {simulated_time:>8.2f} years")
    print("-" * 51)
    print(f"{'Call Price:':<15} ${simulated_call_price:>10.4f} | {'Put Price:':<12} ${simulated_put_price:>10.4f}")
    print("-" * 51)
    print(f"{'Call Delta:':<15} {simulated_call_delta:>10.4f} | {'Put Delta:':<12} {simulated_put_delta:>10.4f}")
    print("-" * 51)
    print(f"{'Gamma:':<15} {simulated_gamma:>10.4f} | {'Vega:':<12} {simulated_vega:>10.4f}")
    print("-" * 51)
    print(f"{'Call Theta:':<15} {simulated_call_theta:>10.4f} | {'Put Theta:':<12} {simulated_put_theta:>10.4f}")
    print("-" * 51)
    print(f"{'Call Rho:':<15} {simulated_call_rho:>10.4f} | {'Put Rho:':<12} {simulated_put_rho:>10.4f}")
    print("-" * 51)


#Time Sensitivity Graph
fig, axes = plt.subplots(3, 2, figsize=(14, 12))

#Graph1 Option Prices
axes[0, 0].plot(times, call_price_time, label="Call Price", color = "blue")
axes[0, 0].plot(times, put_price_time, label="Put Price", color = "green")

axes[0, 0].set_title("Option Prices vs Time(Years)")
axes[0, 0].set_xlabel("Time(Years)")
axes[0, 0].set_ylabel("Option Price ($)")

axes[0, 0].legend()
axes[0, 0].grid(True)

#Graph2 Delta
axes[0, 1].plot(times, call_deltas_time, label="Call Delta", color = "blue")
axes[0, 1].plot(times, put_deltas_time, label="Put Delta", color = "red")
axes[0, 1].set_title("Delta vs Time")
axes[0, 1].set_xlabel("Time")
axes[0, 1].set_ylabel("Delta")
axes[0, 1].legend()
axes[0, 1].grid(True)

#Graph3 Gamma
plasma_color = plt.cm.plasma(0.5) 
axes[1, 0].plot(times, gammas_time, label="Gamma", color=plasma_color, linewidth=2.5)
axes[1, 0].set_title("Gamma vs Time(Years)")
axes[1, 0].set_xlabel("Time(Years)")
axes[1, 0].set_ylabel("Gamma")
axes[1, 0].legend()
axes[1, 0].grid(True)

#Graph4 Vega
plasma_purple = plt.cm.plasma(0.1)
axes[1, 1].plot(times, vegas_time, label="Vega", color=plasma_purple, linewidth=2)
axes[1, 1].set_title("Vega vs Time")
axes[1, 1].set_xlabel("Time")
axes[1, 1].set_ylabel("Vega")
axes[1, 1].legend()
axes[1, 1].grid(True)

#Graph5 Theta
vibrant_pink = plt.cm.plasma(0.55)
axes[2, 0].plot(times, call_thetas_time, label="Call Theta", color=vibrant_pink )
axes[2, 0].plot(times, put_thetas_time, label="Put Theta", color = "purple")
axes[2, 0].set_title("Theta vs Time(Years)")
axes[2, 0].set_xlabel("Time(Years)")
axes[2, 0].set_ylabel("Theta")
axes[2, 0].legend()
axes[2, 0].grid(True)

#Graph6 Rho
axes[2, 1].plot(times, call_rhos_time, label="Call Rho", color = "cyan")
axes[2, 1].plot(times, put_rhos_time, label="Put Rho", color = "magenta")
axes[2, 1].set_title("Rho vs Time(Years)")
axes[2, 1].set_xlabel("Time(Years)")
axes[2, 1].set_ylabel("Rho")
axes[2, 1].legend()
axes[2, 1].grid(True)

plt.tight_layout(pad=3.0, h_pad=4.0, w_pad=3.0)
plt.show()


# Risk-Free Rate Sensitivity Simulator
print("=" * 51)
print("RISK-FREE RATE SENSITIVITY SIMULATOR".center(51))
print("=" * 51)
print("")

starting_rate = float(input("Enter the starting risk-free rate: "))
ending_rate = float(input("Enter the ending risk-free rate: "))
rate_increment = float(input("Enter the risk-free rate increment: "))


risk_free_rates = []
call_prices_rfr = []
put_prices_rfr = []

call_deltas_rfr = []
put_deltas_rfr = []
gammas_rfr = []
vegas_rfr = []
call_thetas_rfr = []
put_thetas_rfr = []
call_rhos_rfr = []
put_rhos_rfr = []


for i in range(int(starting_rate * 100), int(ending_rate * 100) + 1, int(rate_increment * 100)):
    simulated_rate = i / 100

    simulated_d1 = (math.log(stock_price / strike_price) + (simulated_rate + (volatility ** 2) / 2) * time_to_expiration) / (volatility * math.sqrt(time_to_expiration))
    simulated_d2 = simulated_d1 - (volatility * math.sqrt(time_to_expiration))

    simulated_Normal_d1 = normal_distribution(simulated_d1)
    simulated_Normal_negd1 = normal_distribution(-simulated_d1)
    simulated_Normal_d2 = normal_distribution(simulated_d2)
    simulated_Normal_negd2 = normal_distribution(-simulated_d2)

    simulated_call_price = (stock_price * simulated_Normal_d1) - (strike_price * math.exp(-simulated_rate * time_to_expiration) * simulated_Normal_d2)
    simulated_put_price = (strike_price * math.exp(-simulated_rate * time_to_expiration) * simulated_Normal_negd2) - (stock_price * simulated_Normal_negd1)

    risk_free_rates.append(simulated_rate)
    call_prices_rfr.append(simulated_call_price)
    put_prices_rfr.append(simulated_put_price)

    simulated_call_delta = simulated_Normal_d1
    simulated_put_delta = simulated_Normal_d1 - 1

    simulated_gamma = normal_density(simulated_d1) / (stock_price * volatility * math.sqrt(time_to_expiration))
    simulated_vega = stock_price * normal_density(simulated_d1) * math.sqrt(time_to_expiration)

    simulated_vega_1_percent = simulated_vega / 100

    simulated_call_theta = (-(stock_price * normal_density(simulated_d1) * volatility) / (2 * math.sqrt(time_to_expiration))) - (simulated_rate * strike_price * math.exp(-simulated_rate * time_to_expiration) * simulated_Normal_d2)
    simulated_put_theta = (-(stock_price * normal_density(simulated_d1) * volatility) / (2 * math.sqrt(time_to_expiration))) + (simulated_rate * strike_price * math.exp(-simulated_rate * time_to_expiration) * simulated_Normal_negd2)

    simulated_call_rho = strike_price * time_to_expiration * math.exp(-simulated_rate * time_to_expiration) * simulated_Normal_d2
    simulated_put_rho = -strike_price * time_to_expiration * math.exp(-simulated_rate * time_to_expiration) * simulated_Normal_negd2

    simulated_call_rho_1_percent = simulated_call_rho / 100
    simulated_put_rho_1_percent = simulated_put_rho / 100


    call_deltas_rfr.append(simulated_call_delta)
    put_deltas_rfr.append(simulated_put_delta)
    gammas_rfr.append(simulated_gamma)
    vegas_rfr.append(simulated_vega)
    call_thetas_rfr.append(simulated_call_theta)
    put_thetas_rfr.append(simulated_put_theta)
    call_rhos_rfr.append(simulated_call_rho)
    put_rhos_rfr.append(simulated_put_rho)

    
    print("")
    print("-" * 51)
    print(f"{'Risk-Free Rate:':<22} {simulated_rate:>8.2%}")
    print("-" * 51)
    print(f"{'Call Price:':<15} ${simulated_call_price:>10.4f} | {'Put Price:':<12} ${simulated_put_price:>10.4f}")
    print("-" * 51)
    print(f"{'Call Delta:':<15} {simulated_call_delta:>10.4f} | {'Put Delta:':<12} {simulated_put_delta:>10.4f}")
    print("-" * 51)
    print(f"{'Gamma:':<15} {simulated_gamma:>10.4f} | {'Vega:':<12} {simulated_vega:>10.4f}")
    print("-" * 51)
    print(f"{'Call Theta:':<15} {simulated_call_theta:>10.4f} | {'Put Theta:':<12} {simulated_put_theta:>10.4f}")
    print("-" * 51)
    print(f"{'Call Rho:':<15} {simulated_call_rho:>10.4f} | {'Put Rho:':<12} {simulated_put_rho:>10.4f}")
    print("-" * 51)


#Time Sensitivity Graph
fig, axes = plt.subplots(3, 2, figsize=(14, 12))

#Graph1 Option Prices
axes[0, 0].plot(risk_free_rates, call_prices_rfr, label="Call Price", color = "blue")
axes[0, 0].plot(risk_free_rates, put_prices_rfr, label="Put Price", color = "green")

axes[0, 0].set_title("Option Prices vs Risk Free Rate")
axes[0, 0].set_xlabel("Risk Free Rate")
axes[0, 0].set_ylabel("Option Price ($)")

axes[0, 0].legend()
axes[0, 0].grid(True)

#Graph2 Delta
axes[0, 1].plot(risk_free_rates, call_deltas_rfr, label="Call Delta", color = "blue")
axes[0, 1].plot(risk_free_rates, put_deltas_rfr, label="Put Delta", color = "red")
axes[0, 1].set_title("Delta vs Risk Free Rate")
axes[0, 1].set_xlabel("Risk Free Rate")
axes[0, 1].set_ylabel("Delta")
axes[0, 1].legend()
axes[0, 1].grid(True)

#Graph3 Gamma
plasma_color = plt.cm.plasma(0.5) 
axes[1, 0].plot(risk_free_rates, gammas_rfr, label="Gamma", color=plasma_color, linewidth=2.5)
axes[1, 0].set_title("Gamma vs Risk Free Rate ")
axes[1, 0].set_xlabel("Risk Free Rate")
axes[1, 0].set_ylabel("Gamma")
axes[1, 0].legend()
axes[1, 0].grid(True)

#Graph4 Vega
plasma_purple = plt.cm.plasma(0.1)
axes[1, 1].plot(risk_free_rates, vegas_rfr, label="Vega", color=plasma_purple, linewidth=2)
axes[1, 1].set_title("Vega vs Risk Free Rate")
axes[1, 1].set_xlabel("Risk Free Rate")
axes[1, 1].set_ylabel("Vega")
axes[1, 1].legend()
axes[1, 1].grid(True)

#Graph5 Theta
vibrant_pink = plt.cm.plasma(0.55)
axes[2, 0].plot(risk_free_rates, call_thetas_rfr, label="Call Theta", color=vibrant_pink )
axes[2, 0].plot(risk_free_rates, put_thetas_rfr, label="Put Theta", color = "purple")
axes[2, 0].set_title("Theta vs Risk Free Rate")
axes[2, 0].set_xlabel("Risk Free Rate")
axes[2, 0].set_ylabel("Theta")
axes[2, 0].legend()
axes[2, 0].grid(True)

#Graph6 Rho
axes[2, 1].plot(risk_free_rates, call_rhos_rfr, label="Call Rho", color = "cyan")
axes[2, 1].plot(risk_free_rates, put_rhos_rfr, label="Put Rho", color = "magenta")
axes[2, 1].set_title("Rho vs Risk Free Rate")
axes[2, 1].set_xlabel("Risk Free Rate")
axes[2, 1].set_ylabel("Rho")
axes[2, 1].legend()
axes[2, 1].grid(True)

plt.tight_layout(pad=3.0, h_pad=4.0, w_pad=3.0)
plt.show()


#Strike Price Sensitivity Simulator
print("=" * 51)
print("STRIKE PRICE SENSITIVITY SIMULATOR".center(51))
print("=" * 51)
print("")

starting_strike = float(input("Enter the starting strike price: "))
ending_strike = float(input("Enter the ending strike price: "))
strike_increment = float(input("Enter the strike price increment: "))


strike_prices = []
call_prices_strike = []
put_prices_strike = []

call_deltas_strike = []
put_deltas_strike = []
gammas_strike = []
vegas_strike = []
call_thetas_strike = []
put_thetas_strike = []
call_rhos_strike = []
put_rhos_strike = []


for i in range(int(starting_strike * 100), int(ending_strike * 100) + 1, int(strike_increment * 100)):
    simulated_strike = i / 100

    simulated_d1 = (math.log(stock_price / simulated_strike) + (risk_free_rate + (volatility ** 2) / 2) * time_to_expiration) / (volatility * math.sqrt(time_to_expiration))
    simulated_d2 = simulated_d1 - (volatility * math.sqrt(time_to_expiration))

    simulated_Normal_d1 = normal_distribution(simulated_d1)
    simulated_Normal_negd1 = normal_distribution(-simulated_d1)
    simulated_Normal_d2 = normal_distribution(simulated_d2)
    simulated_Normal_negd2 = normal_distribution(-simulated_d2)

    simulated_call_price = (stock_price * simulated_Normal_d1) - (simulated_strike * math.exp(-risk_free_rate * time_to_expiration) * simulated_Normal_d2)
    simulated_put_price = (simulated_strike * math.exp(-risk_free_rate * time_to_expiration) * simulated_Normal_negd2) - (stock_price * simulated_Normal_negd1)

    strike_prices.append(simulated_strike)
    call_prices_strike.append(simulated_call_price)
    put_prices_strike.append(simulated_put_price)

    simulated_call_delta = simulated_Normal_d1
    simulated_put_delta = simulated_Normal_d1 - 1

    simulated_gamma = normal_density(simulated_d1) / (stock_price * volatility * math.sqrt(time_to_expiration))
    simulated_vega = stock_price * normal_density(simulated_d1) * math.sqrt(time_to_expiration)

    simulated_vega_1_percent = simulated_vega / 100

    simulated_call_theta = (-(stock_price * normal_density(simulated_d1) * volatility) / (2 * math.sqrt(time_to_expiration))) - (risk_free_rate * simulated_strike * math.exp(-risk_free_rate * time_to_expiration) * simulated_Normal_d2)
    simulated_put_theta = (-(stock_price * normal_density(simulated_d1) * volatility) / (2 * math.sqrt(time_to_expiration))) + (risk_free_rate * simulated_strike * math.exp(-risk_free_rate * time_to_expiration) * simulated_Normal_negd2)

    simulated_call_rho = simulated_strike * time_to_expiration * math.exp(-risk_free_rate * time_to_expiration) * simulated_Normal_d2
    simulated_put_rho = -simulated_strike * time_to_expiration * math.exp(-risk_free_rate * time_to_expiration) * simulated_Normal_negd2

    simulated_call_rho_1_percent = simulated_call_rho / 100
    simulated_put_rho_1_percent = simulated_put_rho / 100


    call_deltas_strike.append(simulated_call_delta)
    put_deltas_strike.append(simulated_put_delta)
    gammas_strike.append(simulated_gamma)
    vegas_strike.append(simulated_vega)
    call_thetas_strike.append(simulated_call_theta)
    put_thetas_strike.append(simulated_put_theta)
    call_rhos_strike.append(simulated_call_rho)
    put_rhos_strike.append(simulated_put_rho)


    print("")
    print("-" * 51)
    print(f"{'Strike Price:':<22} ${simulated_strike:>8.2f}")
    print("-" * 51)
    print(f"{'Call Price:':<15} ${simulated_call_price:>10.4f} | {'Put Price:':<12} ${simulated_put_price:>10.4f}")
    print("-" * 51)
    print(f"{'Call Delta:':<15} {simulated_call_delta:>10.4f} | {'Put Delta:':<12} {simulated_put_delta:>10.4f}")
    print("-" * 51)
    print(f"{'Gamma:':<15} {simulated_gamma:>10.4f} | {'Vega:':<12} {simulated_vega:>10.4f}")
    print("-" * 51)
    print(f"{'Call Theta:':<15} {simulated_call_theta:>10.4f} | {'Put Theta:':<12} {simulated_put_theta:>10.4f}")
    print("-" * 51)
    print(f"{'Call Rho:':<15} {simulated_call_rho:>10.4f} | {'Put Rho:':<12} {simulated_put_rho:>10.4f}")
    print("-" * 51)


#Strike Price Sensitivity Graph
fig, axes = plt.subplots(3, 2, figsize=(14, 12))

#Graph1 Option Prices
axes[0, 0].plot(strike_prices, call_prices_strike, label="Call Price", color = "blue")
axes[0, 0].plot(strike_prices, put_prices_strike, label="Put Price", color = "green")

axes[0, 0].set_title("Option Prices vs Strike Price")
axes[0, 0].set_xlabel("Strike Price")
axes[0, 0].set_ylabel("Option Price ($)")

axes[0, 0].legend()
axes[0, 0].grid(True)

#Graph2 Delta
axes[0, 1].plot(strike_prices, call_deltas_strike, label="Call Delta", color = "blue")
axes[0, 1].plot(strike_prices, put_deltas_strike, label="Put Delta", color = "red")
axes[0, 1].set_title("Delta vs Strike Price")
axes[0, 1].set_xlabel("Strike Price")
axes[0, 1].set_ylabel("Delta")
axes[0, 1].legend()
axes[0, 1].grid(True)

#Graph3 Gamma
plasma_color = plt.cm.plasma(0.5) 
axes[1, 0].plot(strike_prices, gammas_strike, label="Gamma", color=plasma_color, linewidth=2.5)
axes[1, 0].set_title("Gamma vs Strike Price ")
axes[1, 0].set_xlabel("Strike Price")
axes[1, 0].set_ylabel("Gamma")
axes[1, 0].legend()
axes[1, 0].grid(True)

#Graph4 Vega
plasma_purple = plt.cm.plasma(0.1)
axes[1, 1].plot(strike_prices, vegas_strike, label="Vega", color=plasma_purple, linewidth=2)
axes[1, 1].set_title("Vega vs Strike Price")
axes[1, 1].set_xlabel("Strike Price")
axes[1, 1].set_ylabel("Vega")
axes[1, 1].legend()
axes[1, 1].grid(True)

#Graph5 Theta
vibrant_pink = plt.cm.plasma(0.55)
axes[2, 0].plot(strike_prices, call_thetas_strike, label="Call Theta", color=vibrant_pink )
axes[2, 0].plot(strike_prices, put_thetas_strike, label="Put Theta", color = "purple")
axes[2, 0].set_title("Theta vs Strike Price")
axes[2, 0].set_xlabel("Strike Price")
axes[2, 0].set_ylabel("Theta")
axes[2, 0].legend()
axes[2, 0].grid(True)

#Graph6 Rho
axes[2, 1].plot(strike_prices, call_rhos_strike, label="Call Rho", color = "cyan")
axes[2, 1].plot(strike_prices, put_rhos_strike, label="Put Rho", color = "magenta")
axes[2, 1].set_title("Rho vs Strike Price")
axes[2, 1].set_xlabel("Strike Price")
axes[2, 1].set_ylabel("Rho")
axes[2, 1].legend()
axes[2, 1].grid(True)

plt.tight_layout(pad=3.0, h_pad=4.0, w_pad=3.0)
plt.show()
