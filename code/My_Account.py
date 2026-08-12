#Your account details
from portfolio import change_password
from portfolio import del_account
import sys
from portfolio import display_portfolio
def my_account():
    while True:
        print("1. View Portfolio")
        print("2. Change Password")
        print("3. Delete Account")
        print("4. See python version")
        print("5. Return to Main Menu")
        option = input("Please select your preferred option:")
        if option == "1":
            display_portfolio()
            print(f"Python version: {sys.version}")
        elif option == "2":
            change_password()
        elif option == "3":
            print("Delete your account!")
            del_account()
        elif option == "4":
            print(f"Python version: {sys.version}")
        elif option == "5":
            return
        else:
            print("Invalid option. Please select a valid option.")