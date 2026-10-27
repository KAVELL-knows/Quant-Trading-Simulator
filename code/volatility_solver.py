#Volatility Solver
import math

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
    print("2. No Transaction Costs or Taxes")
    print("3. No Arbitrage - There are no risk-free profit opportunities under the model's idealized market assumptions.")
    print("4. The underlying asset can be traded continuously.")
    print("5. Constant Risk-Free Interest Rate")
    print("6. Constant Volatility")
    print("7. The model assumes continuously compounded stock returns follow a normal distribution, making future stock prices lognormally distributed.")
    print("8. No Dividends")

def volatility_solver_method():
    print("The Bisection Method was used")
    print("")
    print("1. Establish lower and upper volatility estimates.")
    print("2. Calculate the midpoint between the two estimates.")
    print("3. Calculate the theoretical option price using that volatility.")
    print("4. Compare the theoretical price with the observed market price.")
    print("5. Narrow the volatility range according to the price difference.")
    print("6. Repeat until the price difference is sufficiently small.")

def volatility_solver_limitations():
    print("These are the limitations of the Implied Volatility")
    print("")
    print("1. Implied volatility is an estimate, not a guarantee of future volatility.")
    print("2. Market option prices may contain bid-ask spreads and pricing noise.")
    print("3. Real markets may violate the model's assumptions.")
    print("4. Volatility can vary with strike price and expiration date.")
    print("5. The basic implementation does not account for dividends.")
    print("6. A market price outside the model's theoretical bounds cannot produce a valid implied volatility under the specified assumptions.")

def normal_distribution(x):
    return (1 + math.erf(x / math.sqrt(2))) / 2


def black_scholes_price(stock_price, strike_price, time_to_expiration, risk_free_rate, volatility, option_type):

    d1 = ( math.log(stock_price / strike_price) + (risk_free_rate + volatility ** 2 / 2) * time_to_expiration) / (volatility * math.sqrt(time_to_expiration))
    d2 = d1 - volatility * math.sqrt(time_to_expiration)

    if option_type == "CALL":
        option_price = (stock_price * normal_distribution(d1) - strike_price * math.exp(-risk_free_rate * time_to_expiration) * normal_distribution(d2))

    elif option_type == "PUT":
        option_price = ( strike_price * math.exp(-risk_free_rate * time_to_expiration) * normal_distribution(-d2) - stock_price * normal_distribution(-d1))

    else:
        raise ValueError("Option type must be CALL or PUT.")
    return option_price


def calculate_implied_volatility( stock_price, strike_price, time_to_expiration, risk_free_rate,
    market_option_price, option_type):

    lower_volatility = 0.00000000000001
    upper_volatility = 1.0

    
    while upper_volatility < 100:

        theoretical_price = black_scholes_price( stock_price, strike_price, time_to_expiration, risk_free_rate, 
            upper_volatility, option_type )

        if theoretical_price >= market_option_price:
            break

        upper_volatility *= 2
    else:
        raise ValueError("Could not find a suitable volatility range.")


    if theoretical_price < market_option_price:
        print("NO Suitable Volatility Range Found!")
        return None

    for i in range(100):

        middle_volatility = ( lower_volatility + upper_volatility) / 2
        theoretical_price = black_scholes_price(stock_price, strike_price, time_to_expiration, risk_free_rate, middle_volatility, option_type)
        
        if abs(theoretical_price - market_option_price) < 0.000001:
            return middle_volatility

        if theoretical_price < market_option_price:
            lower_volatility = middle_volatility
        else:
            upper_volatility = middle_volatility

    return (lower_volatility + upper_volatility) / 2


def calculate_implied_volatility(stock_price, strike_price, time_to_expiration, risk_free_rate,
    market_option_price, option_type):

    if stock_price <= 0:
        raise ValueError("Stock price must be greater than zero.")

    if strike_price <= 0:
        raise ValueError("Strike price must be greater than zero.")

    if time_to_expiration <= 0:
        raise ValueError("Time to expiration must be greater than zero.")

    if market_option_price < 0:
        raise ValueError("Market option price cannot be negative.")

    if option_type not in ["CALL", "PUT"]:
        raise ValueError("Option type must be CALL or PUT")

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

