#this is market place and its calculations

from market import stocks
from portfolio import update_balance, update_stock, update_trade_history, save_history
from market import stock_price  
from market import update_prices
from portfolio import total_equity
from trends import data_collected
from market import predict_prices

def buy_stock():
        print("What stock do you want to buy?")
        stock = input("Enter the stock symbol: ").upper().strip()
        if stock in stocks:
            print(f"{stock}: ${stocks[stock]:.2f}")
        else:
            print("404 error stock not found. Please enter a valid stock symbol.")
            while stock not in stocks:
                print("Select a different stock to purchase?")
                stock = input("Enter the stock symbol: ").upper().strip()
        if stock in stocks:
            print(f"{stock}: ${stocks[stock]:.2f}")
            print("How many shares do you want to buy?")
            print(f"1 share is costs ${stocks[stock]:.2f}")

            shares = float(input("Enter the number of shares you want to buy: "))
            if shares <= 0:
                print("Please enter a positive number of shares.")
                while shares <= 0:
                    shares = float(input("Enter the number of shares you want to buy: "))
            from portfolio import current_cash
            total_cost = shares * stocks[stock]
            if total_cost > current_cash:
                print("You do not have enough money.")
                return
            print(f"you have brought {shares} shares of {stock} at ${stocks[stock]:.2f} per share.")
            print(f"The cost of {shares} shares is ${total_cost:.2f}")
            update_balance("Buy", total_cost)
            update_stock("Buy", stock, shares)
            update_trade_history("Buy", stock, shares, total_cost)
            total_equity()
            save_history()

def sell_stock():
        print("What stock do you want to sell?")
        stock = input("Enter the stock symbol: ").upper().strip()
        if stock in stocks:
            print(f"{stock}: ${stocks[stock]:.2f}")
        else:
            print("404 error stock not found. Please enter a valid stock symbol.")
            while stock not in stocks:
                print("Select a different stock to purchase?")
                stock = input("Enter the stock symbol: ").upper().strip()
        if stock in stocks:
            print(f"{stock}: ${stocks[stock]:.2f}")
            print("How many shares do you want to sell?")
            print(f"1 share is worth ${stocks[stock]:.2f}")
            shares = float(input("Enter the number of shares you want to sell: "))
            if shares <= 0:
                print("Please enter a positive number of shares.")
                while shares <= 0:
                    shares = float(input("Enter the number of shares you want to sell: "))
            from portfolio import current_stock
            if stock not in current_stock:
                print("You do not own this stock.")
                return
            if shares > current_stock[stock]:
                print(f"You only own {current_stock[stock]} shares of {stock}.")
                return
            total_cost = shares * stocks[stock]
            print(f"You sold {shares} shares of {stock} at ${stocks[stock]:.2f} per share.")
            print(f"The cost of {shares} shares is ${total_cost:.2f}")
            update_balance("Sell", total_cost)
            update_stock("Sell", stock, shares)
            update_trade_history("Sell", stock, shares, total_cost)
            total_equity()
            save_history()

def short_stock():
    print("Work is to be done in this section!!! COMING SOON")

def market_place_and_calculations():
    while True:
        print("1. See Market Prices")
        print("2. Buy Stock")
        print("3. Sell Stock")
        print("4. Short Stock")
        print("5. See next day stock prices")
        print("6. Return to Main Menu")
        option = input("Please select your preferred option:")
        if option == "1":
            stock_price()
        elif option == "2":
            buy_stock()
        elif option == "3":
            sell_stock()
        elif option == "4":
            short_stock()
        elif option == "5":
            predict_prices()
        elif option == "6":
            return
        else:
            print("Invalid option. Please select a valid option.")
        