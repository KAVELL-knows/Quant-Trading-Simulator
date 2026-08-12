from unicodedata import name

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
import sys
from trends import data_collected
from My_Account import my_account
from Market_Place_and_Calculations import market_place_and_calculations

create_account()
while True:
    print(f"Welcome to the stock market simulator, {name}!")
    print("1. My Account")
    print("2. Market")
    print("3. Exit")
    option = input("Enter your preferred option: ")

    while option not in ["1", "2", "3"]:
            print("Invalid option. Please select a valid option.")
            option = input("Enter your preferred option: ")
    if option == "1":
        print("My Account Details")
        my_account()
    elif option == "2":
          print("Welcome to the Market!")
          print("Begin your investment journey today!!")
          market_place_and_calculations()
    elif option == "3":
        print("Exit program.")
        sys.exit()
        break





   

    