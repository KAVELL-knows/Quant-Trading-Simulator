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
