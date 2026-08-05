from market import stocks
from portfolio import display_portfolio, update_balance, update_stock, update_trade_history, save_history
from market import stock_price  
from portfolio import create_account
from portfolio import load_history
from market import update_prices
from portfolio import total_equity
from cipher import encrypt_password
from portfolio import change_password
from portfolio import del_account

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


create_account()

while True:
    print("1. Buy Stock")
    print("2. Sell Stock")
    print("3. View Portfolio")
    print("4. View Market Places")
    print("5. See market prices the next day")
    print("6. Change your password")
    print("7. Exit")
    print("8. Delete your account")
    print("Please select your preferred option:")
    option = input("Enter your preferred option: ")

    while option not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("Invalid option. Please select a valid option.")
        option = input("Enter your preferred option: ")
    if option == "1":
        print("Buy Stock.")
        buy_stock()
        display_portfolio()
    elif option == "2":
        print("Sell Stock.")
        sell_stock()
        display_portfolio()
    elif option == "3":
        print("View your portfolio when option is selected.")
        display_portfolio()
    elif option == "4":
        print("View Market Prices")
        stock_price()
    elif option == "5":
        print("See prices the next day")
        update_prices()
        stock_price()
    elif option == "6":
        change_password()
    elif option == "7":
        print("Exit program.")
    elif option == "8":
        print("Delete your account!")
        del_account()
        break

    