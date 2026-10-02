#Blackscholes Model 
import math
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




stock_price = float(input("Enter the current stock price: "))
strike_price = float(input("Enter the strike price: "))
time_to_expiration = float(input("Enter the time to expiration in years: "))
risk_free_rate = float(input("Enter the risk-free interest rate: "))
volatility = float(input("Enter the volatility: "))

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

#