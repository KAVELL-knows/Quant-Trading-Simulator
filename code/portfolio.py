#this is my portfolio
import json
import sys
from cipher import encrypt_password
from cipher import new_encrypt_password
starting_balance = 0.0
current_cash = 0.0
equity = 0.0
stock_value = 0.0
current_stock = {}
trade_history = []
encrypt_vrbl = ""
key = ""
name = ""
new_encrypted = ""
login_name = ""

def create_account():
    global starting_balance
    global current_cash
    global name
    global key
    global encrypt_vrbl
    global login_key
    global new_encrypted


    print("1.Create an account")
    print("2.Log into your account")
    print("3.Exit")
    option = input("Please select your preferred option: ")

    if option == "1":
        while True:
            print("Create an account.")
            name = input("Please enter your name: ")
            try:
                 with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                data = {}
            if name in data:
                print("This username has already between taken")
                continue
            password = input("Please enter your password: ")
            new_password = input("Please re-enter your password: ")
            key = input("Enter a cipher key word that you would like to use to encrypt your password: ")
 
            if password != new_password:
                print("Invalid login credentials. Please try again.")
            else:
                encrypt_vrbl = encrypt_password(password, key)
                print("Account created successfully.")
                break

        while True:
            try:
                starting_balance = float(input("Enter the starting balance: "))

                if starting_balance < 0:
                    print("Please enter a positive number.")
                else:
                    break

            except ValueError:
                print("Invalid input! Please enter a number.")

        print(f"Your starting balance is: ${starting_balance:.2f}")
        print(f"Account created for {name}.")
        current_cash = starting_balance
        save_history()
    elif option == "2":
        while True:
            print("Log into your account.")
            login_name = input("Please enter your name: ")
            new_password = input("Please enter your password: ")
            login_key = input("Please enter your login key: ")
            new_encrypted = new_encrypt_password(new_password, login_key)
            if new_encrypted ==  encrypt_vrbl and login_name == name:
                load_history(login_name)
                print("Account logged in successfully.")
                break
            else:
                print("Invalid password. Please try again.")
                return create_account()
                
    elif option == "3":
        print("You have exited!")
        sys.exit()
    else:
        print("Invalid option. Please select a valid option.")
        return 


def change_password():
    global encrypt_vrbl
    global key
    global name
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No accounts found.")
        return
    account_username = input("What is your account name? ")
    if account_username not in data:
        print("Account not found.")
        return
    login_key = input("Enter your cipher key word: ")
    verify_password = input("Your current password: ")
    if new_encrypt_password(verify_password, login_key) != data[account_username].get("Encrytion code"):
        print("Wrong credentials!")
        return
    while True:
        new_password = input("Enter a new password: ")
        confirm_new_password = input("Re-enter your new password: ")
        if new_password != confirm_new_password:
            print("You have entered two different passwords. Please try again.")
        else:
            break
    new_key = input("Enter a cipher key word to encrypt your new password: ")
    encrypt_vrbl = encrypt_password(new_password, new_key)
    key = new_key
    data[account_username]["Encrytion code"] = encrypt_vrbl
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
    if account_username == name:
        key = new_key
    print("Your password has been updated.")

       

def display_portfolio():
    print(f"Starting Balance: ${starting_balance:.2f}")
    print(f"Current Cash: ${current_cash:.2f}")
    print(f"Portfolio Value: ${stock_value:.2f}")
    print(f"Total Equity: ${equity:.2f}")
    print(f"Profit/Loss: ${equity - starting_balance:.2f}")
    print(f"Current Holdings: {current_stock}")
  
    print(f"Trade History: {trade_history}")
    for buy_or_sell, stock, shares, total_cost in trade_history:
        print(f"{buy_or_sell} {shares} shares of {stock} for ${total_cost:.2f}")

def save_history():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    data[name] = {
        "Starting Balance": starting_balance,
        "Current Cash": current_cash,
        "Portfolio Value": stock_value,
        "Total Equity": equity,
        "Current Holdings": current_stock,
        "Trade History": trade_history,
        "User Name": name,
        "Encrytion code": encrypt_vrbl,
    }

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

def load_history(username):
    global starting_balance
    global current_cash
    global stock_value
    global equity
    global current_stock
    global trade_history
    global encrypt_vrbl
    global name
    
    with open("data.json", "r") as file:
        data = json.load(file)

        account = data[username]
        starting_balance = account["Starting Balance"] 
        current_cash = account["Current Cash"]
        stock_value = account["Portfolio Value"]
        equity = account["Total Equity"]
        current_stock = account["Current Holdings"]
        trade_history = account["Trade History"]
        encrypt_vrbl = account["Encrytion code"]
        name = account["User Name"]


def update_balance(buy_or_sell, total_cost):
    global current_cash
    global equity
    if buy_or_sell == "Buy":
        current_cash = float(current_cash - total_cost)
    elif buy_or_sell == "Sell":
        current_cash = float(current_cash + total_cost)

def total_equity():
    global equity
    global stock_value
    from market import stocks
    stock_value = 0.0
    for stock, shares in current_stock.items():
        stock_value += float(shares * stocks[stock])

    equity = float(current_cash + stock_value)

def update_stock(buy_or_sell, stock, shares):
    global current_stock

    if buy_or_sell == "Buy":
        if stock in current_stock:
            current_stock[stock] += shares
        else:
            current_stock[stock] = shares
    elif buy_or_sell == "Sell":
      if stock in current_stock:
            current_stock[stock] -= shares
            if current_stock[stock] == 0:
                del current_stock[stock]

def update_trade_history(buy_or_sell, stock, shares, total_cost):
    trade_history.append((buy_or_sell, stock, shares, total_cost))

def del_account():
    global name
    global encrypt_vrbl
    global key

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No accounts found.")
        return
    account_username = input("What is your account name? ")
    if account_username not in data:
           print("Account not found.")
           return
    login_key = input("Enter your cipher key word: ")
    verify_password = input("Your current password: ")
    if encrypt_password(verify_password, login_key) != data[account_username].get("Encrytion code"):
        print("Wrong credentials!")
        return
    while True:
        print("Are you sure you want to delete your account?")
        confirm = input("Type 'Y' to confirm or 'N' to cancel: ").upper().strip()
        if confirm == "Y":
            del data[account_username]
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
            name = ""
            encrypt_vrbl = ""
            key = ""
            print("Account TERMINATED!")
            break
        else:
            print("Account deletion canceled.")
            break