June 30, 2026

Today I:
- Started my passion project. My first project will be a Quant Trading Simulator. 
-Firstly, I downloaded Python, Visual Studio Code, and Git.
-Also, I created my Quant Trading Simulator project folder, which contains notes, code and screenshots as well as Read Development Log and Me

What I learned:
- I did not know about ReadMe.md and Development_log.md

Next goal:
- I want to set up Python, Git, and Visual Studio Code and start to understand better what each piece of software does.



Day 2
July 2nd 2026
Python was installed and set up, and also Visual Studio 
I did learn that widows + R opens the Run dialog. When I typed cmd, I got "Command Prompt".

The next thing I did was in Visual Studio, under Python, by using the simple code that is print() to output

So the code was 
print("Hello, Waterloo!")
print("My name is Kaveri.")
print("Today I officially started my coding journey.")
print("Future goal: Computer Science + Mathematics.")


To run it, I would go to the terminal, then open a new terminal, and finally type python code/ ( the name of the code ) 

DAY 3 08/07/27
git init - a means of tracking history, it creates a hidden folder .git that stores the info on something called commit ( its like a book ) 

git status - what is happening in the project right now, which files its tracking and which ones are new 

git add .
git means use git
add means track files
. add everything 

git commit -m "Initial project setup and first Python program"
git means use Git
commit means save a checkpoint
-m means attach a message
"Initial project setup and first Python program" describes what was saved

git config --global user.name "Kavel"
git config --global user.email "kavel.lalla2@gmail.com"

git config --global --list  this would give you user name and email
git branch lists all your local branches

git branch 
git branch -M main
now it shows *main   since  renames the current branch (master) to main


git remote add origin https://github.com/KAVELL-knows/Quant-Trading-Simulator.git
git remote add origin URL 
remote - remote is simply a saved address of another Git repository
add Create a new remote connection.

origin gives a label to the link 
origin = https://github.com/KAVELL-knows/Quant-Trading-Simulator.git
Short cut to typing the full URL every time.

.git tells a git to end 


git remote -v
means to show saved connections

v stands for verbose
-v  showed
origin https://github.com/KAVELL-knows/Quant-Trading-Simulator.git (fetch)
origin https://github.com/KAVELL-knows/Quant-Trading-Simulator.git (push)

git push -u remote_name branch_name
so in thise case rmeote_name would be origin
branh name is main 

push sends local commits to anothe repository 
-u means --set-upstream - that is used to remember the connection bteween my local main branch to GitHub main branch 

its useful because in the future instead of saying "git push origin main" i can just say "git push"


OKAY FIRST OBJECTIVE
1. Stock data simulation
main.py The program controller so like menu buy sell
market.py  price changes 
portfolio.py deals with shares and cash the investment 

SO HOW TO EDIT FILE NAMES
Rename-Item -Path code\(name of the file you want to chnage) -NewName main.py

dir code
so within the file named code it would show all the directory 

HOW TO ADD FILES
so we want to add the file under code
New-Item code\(name of the file you want) -ItemType File


SO NOW WE ARE GOING TO BEGIN WORK ON THE MARKET.PY this would contain stocks, their values how they change over time. 

# means comment. ( the code itself wont run this)

= means something is contained in it. if im assinging a varible i would use = 
== its literally equilvalent to something so 3==3

so now we start store = 
store by it self means nothing but store = makes a variable
now store = {...} means that within the variable store = there is ... so rather than just saying ... over and over i would say store = to save time

so i want to put some popular stocks within my variable so i would use A stock name and i would put its price 

okay so now within the variable i can put a name or label(called a key) with ".."
so lets say i want to name some stock say MPWR then stock = {"MPWR"}
no that i have the name lets say i want to assign a price to it a value i can use :
the : maps the name to a value 
so stock = {"MPWR": 770}

now i want to have multiple stock just separate it by comma so lets add POWL
stocks = {"MPWR": 770, "POWL": 220} 

NB: spaces dont matter however at the beginning of a line dont put spaces it might cause an indentation error 

you would use the function def to define/ create functions 
you would create functions to make it easier/ faster 
to create a new function say a function for stock prices
def "name of the function i want to create"():
the () so there is no external input
: shows thats the end of the line
so functions/ loops/ decision always end in colons everything else doesnt end in :

so now that we have def show_prices():
we want to the assign a tast to the function.. tell the function what to do 
so in this case i want the function to show to the user current stock prices
so 
def show_prices():
    print("Current stock prices:")

How to set up a FOR loop
for "key_variable", "value_variable" in dictionary_name.items():
basically type for then in this case we want the items inside of the stocks variable we set up so 
we had MPWR ( a stock ) and then the price next to it 
so simply by putting for "stocks","price" in stocks.items():

it could be 
for "potato","tomato" in stocks.items():
the recognize stock at what comes first and price as what came after the comma

NB if its just a letter like
for x,y in stocks.items():
since the computer it recognizes x and y as variables

the point of the loop it self 
would show stock then price and repeat for the next set so show the next stock and the next price underneath 

NOW TO ACTUALLY GET IT TO SHOW THAT 
print(f"{stock}: ${price}")

the f is for f string it lets python know the stock is the variable stock rather than the actual word stock and the vsriable for price rather than the actual word for price

when using f string variables go in {}

so something like print(f"{...}:${...}")
the " lets its know that entitre output goes on 1 line else it would show up on 2 lines

and as for : $ that is literally printed we can get something like
{stock} : ${price}

finally
def stock_price():
    print("Current stock prices:")

    for stock, price in stocks.items():
        print(f"{stock}: ${price}")

        the indentation is important to show that all the functions are under the def

09/07/26
Day 4
        so the main.py is really the control the program so that would mean like menus and stuff so when you go through the like software you want to be able to click buttont to access the stocks so as you traverse on main.py you should beable to get access to market.py its in different files so im thinking thre might be a way in code to like evrytime you want to access the stocks rather than just like typing over the stock code you just say something like use the code from the market.py in 1 line you know

        so in that case...
        in the main.py we can type
        from market import stock_price

       if you want to do more than one just seprate by comma 
       so 
       from market import stock_prices, "..." 


       the goal to do main.py which the area with the controls is to do like a menu on top 
       then give it options to buy sell exit check profits etc
       now to do this we can print and in that print assign a number to each options

       that way we can that ask the user input the choice which they want
       and we will called the choice which they have select the variable choice
       choice = input("choose")

       once the person chosen what they want we can set up the if else statement 
       to do this  
       the first statement would begin with if all proceeding with elif and the final line for incase all the above fail else

       so lets say we want to go buy if 1 is chosen
       if choice == "1": 
       print("buy")

       lets say we want for if sell where sell is = 2
       elif choice == "2":
       print("sell")
       finally in the even none of the above is selected 
       else is used 
       so 
       else print("the choice is not valid")

       DAY 5
       10/07/2026

       so the goal for today is i want to make the Buy Sell Exit and View portfolio buttins functional

       The idea is create a new function so if the user inputs 1 the function will allow the user to type the stock name from there i want to be able to ask for the shares and calculate it

       so the new function will be called buy_stock
       def buy_stock():

       once the user inputs the stock name ( which belongs to the stocks variable ) the stock would be stored as a variable which is known as stock 
       so it would show the cost of share 

       so actually show the value of the selected stock
       stocks[stock]
       meaning go to the variable stocks and within that dictonary there is the stock.
       [stock] means to give the number of the stock rather than the stock name
       so if we wanted to show "the prices of 1 share of tesla stock is x dollars

       print(f"The price of 1 share of {stock} is : ${stocks[stock]}")

       NB : always use {}  inside an f-string, like f"{variable}"

       next thing is to ask for number of shares the user wants
       so for this i used float so i can have like 5.5 shares rather than int
       and this was stored as a variable shares

       we cant have negative shares so i set up an if statement where 
       if shares <= 0 
       print "(invalid input")

       also i set up a while loop so as long as the user kept inputting invalid numbers it would loop back and prompt to user to do it again

       to set up a while loop simply type
       while
       the previous function so shares <= 0
       ask them to redo the same prompt from ealier so assign a value to the shares variable

       WHILE LOOP - it just keeps asking for input as long as the condition is true
                     so as long as invalid stock is enterred it will keep asking

       after all that finally its time to calculate a total so to do this
float(shares)*stocks[stock]

and i assigned that a variable total_cost

okay so now i want to account for an option where a while loop is used if an invalid stock is enterred which i forgot to check for before.

okay the issue is now resolved i added a while loop 

another problem is i want tsla TSLA tSla to all be the same
so im thinking go to market.py and add it .strip() to the end of all the names


.strip() means spacing dont matter
.upper() means the casing dont matter

i want to combine both so i would use at the end of the stocks variables .upper().strip()   the order does not matter

also everytime i assign a value to stock variable the sentence would end with the .upper().strip()

the option 2 (sell ) is straight forward define a new function...just copy over the code and change buy to sell

11/07/26
DAY6

Today i want to start up portflio.io
Starting/Your in your account
Equity..%
Proftis/Losses
Current Trades
Trade History

okay so now when the person chooses the view portfolio they get the option to put a user name and password and money they want to enter after that can see the portfolio. 

so  i learnt if you are assigning a value to a varaible which is subject to change in a defined function you must use global varible_name
also to get dollars form aka 2 decicmal places just end the sentences in :.2f
so ${price:.2f}  so i updated all previous costs

the code is gettign confusing and messy
i am currently have an error with circular import
my import functions are messy and confused causing it crash on the last step so i need to tryto understand that better and how to get around it tomorrow.

12/07/2026
Day 7

From what i gathered i going from main to portfolio back to main and back to portfolio but because of this its causing it to crash since it keep cirlcing back so to fix this i would use main.py as my central hub meaning i use main.py to get to portfolio.py and market.py so i should NOT  import from main.py

Okay do to get around it i realized i can update the value from main.py into portfolio.py
so rather than reuse their variable i just take that number

so in the case of the total cost i wanted 
all i have to do is something like update_balance(total_cost)
and now im free to use it

also for like starting balance and current cash 
in portolfio.py i would start off just giving them arbitary values so current cash = 0.0

from there u can use current cash later down

something interesting i learnt in logic is that if you want to calculate the current value you would take away total cost from current value rather than from total cost from starting balance.. which does make sense ... since second purchase would not be able to use the starting salary
to do this you would have to let current cash = starting balance

the last thing i did was i made it so you have to confirm you password when creating an account so to do this used a while statement while password != new password you have to reenter... if it is equivlanet its fine and a break is needed

so as long as it is  true if they are not the same they would run forver but when they are the same it is false so the else statement is actvivated which creates the break which allows it to move onto the next part of the code 

13/07/26
DAY 8

okay so the goal for today would be to just add a few while loops in to allow to program to flow smoothly and well as set up the trade hsitory which should be fairly simple

A loop was added for if someone tried to make a portolfio with money < 0 or inputted letters

while true:
    try:
        starting_balance =float(input("Input your starting balance"))
        if starting_balance < 0
        print"invalid"
        else:
            break
    except ValueError
        print("enter a number")

    so basically because we dont want to code to work when letters are enterred we will use ValueError
    Value error recevices an object or string but is flagged if that string cant be converted into a VALUE
    eg if you have xyz it would read the string xyz but it cant convert that into a number so it  goes off

    it needs to be paried with try: because try is incase of the event the code fails, value errors occur when the code failes

    because we dont want our code to fail when something like xyz is flagged we would put the excpet ValueError.. if ValueError alone is written the code will just shut off.

NB: I thought it was going to be easy but i struggle alot!!!
    For trade histroy we would introduce the variable trade_history. We want this variable to show us buy/sell, stock, share and price
    so we will update_trade_histroy(buy_or_sell, stock, share, total_cost)
        since we wnat the trade history to actually show if it was buy or sell i had to go back to def() buy and def() sell and and change it to "buy" for def buy() and "sell" for def sell()
        so that the variable i introduced buy_or_sell would pick it up Buy for def buy() and sell for def()sell
   
    since we want out trade history to how us 
as for the variable trade_history this exists in main.py and to get access to it we do 
global trade_history
            
also i wanted this to be a list 
so on the top i used trade_history = [] rather than trade_history = {} since 
{} the text is over written but in [] it is listed 
in {} the key wont repeat so TSLA wont show up more than once but in [] it can show up more than once

also to get them to be on individual lines i used a for loop under trade histroy


This is where i got stuck
so in the line 

def update_trade_history(buy_or_sell, stock, shares, total_cost):
    trade_history.append((buy_or_sell, stock, shares, total_cost))

    i didnt know about .append

so what .append does is within your list.. to add a new line in the list of items you need .append to do this
so when using [] to list also note .append is needed

DAY 9
14/07/2026
At this point basically everything  works so i want to test all possibilities and refine
 
1) Okay the first bit of refining done is in the update_stock
in even of sell i wnat to subtract shares rather than add shares so my logic was off here

to get around it i intoruced the buy_or_sell variable here 
and added an if buy and if sell

2) logic error again... 
as it would turn out when you 
buy a stock.. current cash decreases... current cash = starting balance - total_cost
sell a stock... current cash increases.. current cash = starting balance + total_cost

3) one other error im getting is equity isnt calculated properly but tomorrow i will have to research how to get around it!

4) another error im looking into but fixed is if you tried to buy a stock but dont have enough money
so basically if current cash < total_cash ( aka the cost of a stock ) then it would go into a loop

DAY 10
15/072026

Today's goal is going to be to get menu loop set up.

the loop took a while to put in but eventually i figured where it should go so 
the loop goes after create_account() so we arent ask to make an account over and over again
also i moved the menu lower and under the functions i defined since the functions do not need to be defined within the loop.
lastly i put a break after the elif statement for exit

so basically the code will work repeated and break when 4 is pressed.
Everything works fine excpet the view profile button which the 3 is not reigstering i dont know why but i will have to research more on it tomorrow.

DAY 11
16/07/2026

Today i want to get the equity to work
that would be the total current cash in ones account + sum of all(shares x value)

to get the sum of all previous trasactions and current ones i would run a FOR loop so for all the stocks and shares that i have it would be shares x stock

since i dont want the new iteration to over write the previous iteration i used +=

so basically 

for stock,shares in current_stock.items
    stock_value += (shares * stock[stocks])

equity = stock_value + current_cash

The next goal would be to learn file handling to keep memory of all the times the code is ran.

DAY 12
17/07/2026

File Handling
im using JSON since it supports numbrs dictionaries and lists

we defined a function save_history necause when we run the code we do not need to repeat all the json code instead it already all stored in save_history

I created a dictionary under the variable name "data" with all th information i want to save after the code shut down so this would include starting_balance, current_cash, equity, trade_history etc

with open("data.json", "w") as file:

the with is important because it tells pythogn to automatically in one go open the file, store the data snd close to while without me having to type of th code

so without withing with open.. i would have to write this 

file = open("data.json", "w")
json.dump(data, file)
file.close()

open mean to literally open the file data.json
then "w" means write mode and it tells python to write the data into this file

as file:
means to give the data which python just wrote into data.json a variable called file

FILE MODES
"r"  = read - read the information from the file
"w"  = write - 
"a"  = append - to add infomration to the file without  replacing what is already there

json.dump(data, file, indent=4)
json.dumb means take python data and write it into a file
(data, file)
data means we want python to store the data from the variable known as data
file is the name of the file where we want to save it since we said as file

indent = 4 means i want all the stored data to be :
1 indented on separate lines
2 there are 4 spaces before the line is written
( it is a common convention for progammers to use indent = 4 because its easy to read but = 8 = 2 is fine)

import json 
it allows the json module to us JSON data

General format for file handling
TO CONVERT PYTHON TO JSON
import json ( at top of the file )
    with open("file_name", "mode") as file:
         json.dump("data to be saved", file, indent=4)

TO READ the text / CONVERT PYTHON TO JSON
import json (at the top of the file)
    with open("file name", "r") as file:
         data = json.load(file)

dump puts data into the file
load takes data out of the file

to get the data actually save i added save_history under def_buy() and def_sell() so the history is saved as soon as the data is changed

DAY 13 
18/07/2026
I want to load the histoey
restore the data
and use it in my portfolio

in order to load the json file we must actually read it so
 open with("data.json","r") as file:
  data = json.load(file)

  since we are updating/ changing these variables we would have to global all of them
  THIS IS BECAUSE LOADING DATA MEANS CHANGING DATA

  usually when we save a variable into the dictionary 
  we would do 
  dictionary_name =   {"letters:" x_y_x }

  however to take them out from the dictionary and load them

  x_y_z = dictionary_name["letters"] 

DAY 14
19/07/2026
The goal for today is the work on security 
so when the person enters username and password.. it allows them to access their account called ( exception handling)

To do this 
we will try to load the data.json if the information is there then we proceed if it not no file containing the data is found
try = to attempt
excpet =if it fails, do something else

general format
try:
    the test 

except:
    if the test is failed


    in this case to do the password 

    try:
        the test ( could be some function sure as to load history)
        print("xyz")
    excpet FileNotFoundError:


    NB Key word error
    this error tell you, you made a typo/ spelling error and the line to go to fix it.



DAY 15
20/07/2026

Rather than hard coding its time to make the markets realistic
so i want to make the numbers random first (custom stock market)
later with the real values (live stock market)
therefore people can select which option they want.

to make the numbers random 
in market.py i imported random

        change = random.uniform(-10,10)
        uniform generates a random number with 2 deciaml places
        -10 and 10 are the lowest and maximim amount the number can change by

          stocks[stock] = stocks[stock] + change
          so the updated price change is added to the stock

DAY 16
21/07/2026
The goal today is the test and look for errors and make adjustments

1) I want to delete a stock from my dictionary if it = 0
so if i bought 8 tsls and then sold 8 tsla i dont want it to show up as 0 owned it want it removed
to this is i used the del command
so if current_stock[stock] == 0:
    del current_stock[stock]

2) i want me portfolio to update when the market changes.
Saving (json.dump): Tuples convert to lists.
Loading (json.load): Everything stays a list

3) for stock prices, I made it so that a stock can never be worth less then $0.01
to do this i made it so that in the variable stocks[stock] = max(0.01, stocks[stock] + change)

DAY 17
22/07/2026
Time to make price hsitory be saved

DAY 18
23/07/2026
I want to implement to improve the log in and password. Today, im going to spend time formalizing and learning about ciphers. I made a Ceasar Cipher in the harvard CS50 so i did some reading on types of ciphers. AES, RSA, Vigenere/Polyalphabetic and caesar. I want to build a Vigenere Cipher

To explain how Vigenere Cipher works it basically uses a key word and adds that value of that number to the value of your password
so if my password is Kav6#7 my jey word could be STOCKS
STOCKS has values like S-18, T-19, O-14, C-2, K-10, S-18
and KAV6#7 would be  K-10, A-0, V-21, 6-32 #-36 7-33
so    S is paired with K so thats 18 + 10 = 28
If we did the MOD 26 a standard alphabet with 26 characters, there are 26 letters so its just 28-26 = 2. which would have become = C

Now in this case, where i use a MOD36  i want to assingemnt values to numbers and #
so A... Z is like 0...25 and 0...9 is 26....35 and # is 36
so MOD 37 meaning 37 different symbols
formula = (password + keyword)MOD37

I am thinking to make the key word a variable in which the user can select their own key word
i want to pair the keyword to the password such that
KAV6#712% would have a keyword STOCKSSTO

Rather than doing liek 37 if statements i want to try to do like an array so a long string

it should be put in the 
english password ---> save the encrptyed ---> when logging in compare the saved encptyted password to the the login in password ( which will become enrptyed). If both passwords have the same encyption the log in is successful

DAY 19
24/07/2026

To go about this i created a 4th module called cipher.py

so to create the MOD37 alphabet, a string 
ALPHABET = [ABCDEFGFGHIJKLMNOPQRSTUVWXYZ]
KEY = any word so ask to user to input a lesson

since we want to load the old password instead of prompting for it just put password variable within the password




def encrypt_password(password):
    password = password.upper()
    encrypted_password = ""

"" = string

    for j in range(len(password)):

    len() - is length 
    len(password) - so this measures the length of the password variable
    range(5) - means 0 1 2 3 4. IT IS FOR HOW MANY TIME A LOOP RUNS

    so the range of the password says how many times you want to for loop to be done its good because it adjusts to the password 

    password_alphanumeric = password[j]
this creates the variable password_alphanumeric and [] tells it to go the respected potions in th string to create an index. [] is used to create an index 
so KAV67 = K-0 A-1 V-2 6-3 7-4

so the range tells the loop to do it how many times
on the first loop
j = k = 0
k = a = 1 etc 

        key_alphanumeric = KEY[j % len(KEY)]

key_alphanumberic is the variable
% is MOD so the remainder after division

so if the j%6
lets say j =  0 
so 0/6 = 0 rem 0
7/6 = 1 rem 1 

Simulatenously index numbers given to these numbers . like if the key word was BATMAN
B = 0  A = 1 etc
so j%len(KEY)

would literally take the 0th loop and divide it by the length of the key in this case 6
0/6 = 0
when it reaches the 10th for eg
10/6 = rem 4 = M

the because you want to do each letter in the word key would do KEY[j % len(KEY)]

        password_number = ALPHABET.index(password_alphanumeric)

        .index  goes to ALPHABETMOD37 variable and so it assigned a number to each component within the list in a sequential order
        so A - 0  B - 1

        basically the letter enterred is converted to a value

     key_number = ALPHABET.index(key_alphanumeric)
     this just converts the key values in numebrs too

    encrypted_number = ( password_number + key_number) % len(ALPHABET)
        this is the formulae i wanted to do use to do the code... add the 2 numbers and divide by the MOD of the length of the alphabet
        
        
        encrypted_character = ALPHABET[encrypted_number]

    number that we have this string of numbers we want to convert it to characters 
    so simply do ALPHABET[encrypted_number]

alphabet.index[]   -   is like letters to numbers
and alphabet[] would be numbers to alphabet assuming LETTERS  are in alphabet

encrypted_password += encrypted_character 

this just means 
encrypted_password = encrypted_password + encrypted_number2character 

    return encrypted_password
    NB IN A FUNCTION BEING DEFINED SINCE THE VALUES WERE ALTERED BY CALCULATION RETURN IS NEEDED. IF NO VALUES WERE CHNAGED NO RETURN NEEDED 

DAY 20
25/07/2026
I added to variable i created into the create an account spot

NB when trying to run to code i was getting and error.... it turned out i forgot to press ctrl + s on cipher.py

i prompted to user ot enter a key cipher when creating an account
in cipher.py 

encrypt_password(password, key)

    password, key = password.upper(), key.upper()
    and
    password = password.upper()
    key = key.upper()

    I also updated the save_history function and load_history
    to do this i created the variables are the top and since they are TEXT which will not be chnaged i used ""
    so name = "" key = ""


    since they are within the function as well global key etc

    Tomorrow i want to start to develop the login function. 
    So recall the encyrption of the old password and compare it to the new password

    Day 21
    26/07/26

Within Cipher.py
    so i created a new function for when the new password is enterred.
    Within this function i used a key and password to create the new encrytion

    from here i created new_enctrypted_password

Within Porfolio.py
    i prompted when logging in to ask for name, password and key

    so when i finally got the new_encrypted password from here I use an OR gate

    so if new_name != name OR encrypted_password != new_encrpyted_password 

    if one of the options were wrong.. the user would not have been let into the system
    if both options were equivalent the user was let into the system 

Improvement:
    in the save_history and load_history, I decided to only save and load the user name and encryption code. That way someone can go open json files and see the saved Password and Key

Goal for tomorrow.
Store mulitple accounts.

    DAY 22
    27/08/26
In order to add accounts i editted the save_histroy
 try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    data[name] = {

        data[] = allows theres to be an array of mutliple accounts under multiple names
        so first the json files are read to look for existing accounts
        and this would be loaded 
        UNLESS no matching accounts are found then there is a FileNotFoundError

        Day 23 
        28/07/2026
I want to put in a code to give an error if someone creates an account with an existing name.

This error would be flagged under the create section
simply call upon the json history
if the user name already exists. Invlaid
if its not it would continue 

NB : Continue checks if the statement inside agrees. If the statements agree the loop is redone.If they dont agree the loop is exitted. So 4 < 56 this is agreeing so the loop will ne re done.

Features to be added.
Logging out
Deleting an account
Changing a password

added in a 3rd option to exit the program 


okay so i added an options to change password
form you i defined a function for changing the password

first i read all the data from the json files

next prompted to re enter to current user name, old key and old password

if those were equilvent when the comparison was made the user is then allowed to input the new data

this then written over in the json files using json.dump ie the data is updated 


Day 24 
29/07/2026

Today i want to work on deleting an account 

My plan is the introduce another option into the main.py so the user can choose to delete his account.

from here i will define a function in porfolio.py
i want to prompt to enter username, password and cipher then run a comparision test. if they match up print. are you sure you want to delete your account if yes is confirmed. del json file 

to delete the json will just write over the data with blank

NB when prompting for things like username which are local variables meaning their exist within only the function its fine to re use them in different functions

however if the veriable is globalized, you cant do this.

del mean  to delete so del data[account_username]
is the delete all data under that name

also the vairables delcared ealier should be reset 
so write over them with json files with
name = ""
encrypt_vrbl = ""
key = ""

DAY 25 
30/07/2026
The goal for today is to try to save all prices across several days on data.json
Day 1 GME = 22.43
DAY 2 GME = 22.34
that way we can see the trend across multiple days and eventually use Pandas to perform calculations

I am thinking to make it its own section so like we can call it 
trends.py and from here i feel like we can run that code to see next day prices
and record all the prices

i want to be in main.py when you select see trends
you get options to view charts, run calcs, see next day predicitons.
Highest price, lowest average median , variance, sd etc

To do this i feel we need to first create the data from future days so as the user loads it form there read it all and save it to trends.py

I will have to create a new json file too 
so there will be one for accounts and another for market prices.



First would be read that data put onto history_of_prices
        with open("history_of_prices.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
( An empty dictionary is created if the file is not found)

Then from there set up an array so go through each stock and prices one at a time in a loop so 
    for stock, price in stocks.items():
        if stock not in data:
            
If the stick doesnt exist an empty file is created  - data[stock] = []
        data[stock].append(price)

Writes over everything into the json file
    with open("history_of_prices.json", "w") as file:
        json.dump(data, file, indent=4)

DAY 26
31/07/2026

So i fixed a bug with the exit on creating an account
i imported sys
so i can use the sys.exit() to exit safely

it also has the print(sys.version) feature to show the python version

I fixed a problem where the user would be stock in an infinite loop if they didnt remember their password. I simple ran the create_account function within the create account funciton. 


DAY 27
1/08/2026
Doing testing today.

When i create an account im askined to log in again.
Delete account works
The  login feature works
Exit works
Create account works
In see next day prices its updating but its not what i invissioned 
Right now for the see next day prices it dosntshow them next 2 each other in an arry it just shows one price at a time not a line .
I want to create this section where you type in the stock you want and from there you access data on the stock.

DAY 28 
2/08/2026
I want to do some front end development to amek everything look better.

PROBLEM : Eeverytime the code run you are them brought back to this large menu with 8 different option taking up the entire screen. I want to group them so it look like youre going another page on the website:

My plan:
Main Menu
Account - delete account, change your password, return to main menu, portfolio
Market - View market prices, buy, sell, see prices next day, charts, calculations
Exit 

if option = 1 Account 
create own module

Okay i did all the code by myself and everything worked just the way I wanted it.
I put in while loops, transferred code, group them up.

Future Plans i decided to add in a Short Stock Section also a place to input more money in your account, as well as withdraw

Tomorrow i want to Get the see next day prices to look better. If i could get a table potential to show Day and Price

DAY 29 
3/08/2026

 I want to do fix up the see next day into a clean table with all the data layed like you type day 1 2 3 4 5 6 7 all line up next 2 one.

We could do this with like a matrix kinda of set up i feel with like row and column displaying in index nation so like [0][0] , [0][1] 
I dont want to hard code 5 stocks for the columns. The user should input the stocks they want to compare and across how many days.

I was able to code in the columns and rows and go through each one by theuse of a for loop but curret it still isnt doing what I want it to do so tomorrow I will add in a table function

Day 30
04/08/26

I have gotten to code to do what I wanted it to do so here is a run through of it:

firstly we ask for how many stocks the user wants to compare we call this the column
as also ask for how many days the user wants to predict - rows

we create an empty array for the stocks so predicted_stocks = []

then we prompt the user to enter the names of the stock that they want to enter 
in a for loop which ranges from the "number of columns entered"

everytime the the loop is ran and the user inputs the stock they program searches to see if that stock exists, if it isnt the code is re ran if not, and a valid is enterred the stock is added into the empty array we set up earlier

ie predicted_stocks(stock).append
recall : .append allows us to add something new to the end of a list

Now that we have set up the number of stocks its time to set up the number of days

so i created an empty array predicted_day = []

and the same process is ran here except we are running the for loop for rows
from range(1 to rows+1) the reason for this is because 
we need to specify firstly that day 1 is starting at 1 and since the for loop always stop 1 iteration before what the stop should be we need to do rows + 1

unlike for i in range(columns) the number of columns is not not listed so it is not
necessary to give a start and a finish but in Days they are lablled Day 1 Day 2 Day3 

Everytime to for loop for the number of days is ran, we update the prices using the update prices function which I previously developed

everytime the price is updated within this there is now another for loop the for loop which checks every stock inside the predicted stock array 
and then assigned the updated value to the specific stock using

predicted_day.append(stocks[stock])

DAY 31
05/08/2026

Now that we have the rows and columns sorted out we need to put this into a table format 
Okay so the make the day it should like something like this

STOCK  GME  TSLA MPWR
DAY 1    #   #    #
DAY 2
DAY 2

so to set this up we need to have the prices updated within the inside 
so firstly 
do print()
so skip a line and not over write the line with STOCK GME TSLA MPWR
next we dont want to write over DAY so we are going to leave space 
so print("       " =end"") so we leave 7 blank spaces to not interrupt DAY # 
=end means dont go to the next line
so 
print("hi"=end"")
print("bro")
outputs hibro

 Now that this is set up 
  for stock in predicted_stocks:
        print(f"{stock:>10}", end="")
this prints the stock which were chosen to be predicted
:>10  means to right allign in a space which is 10 characters wide so it allows all Stocks to displayed nicely space and easy to read

enumerate - it is used to track index number and the item at the same time

it goes through 
 for i, day in enumerate(prediction_table, start=1):
        print(f"Day {i:<3}", end="")
    This prints the day number for the ith iteration and it is left alliged with 3 wide space
        for price in day:
            print(f"${price:>9.2f}", end="")
    :>9 is used to make sure each price takes up 9 spaces

        print()


DAY 32
06/08/2026
Today I want to start getting to that point where we do some advanced calculations so 

The idea:
Create a new module called Advanced Calculations
Within this there will be an option to see historical prices AND also and options to do many different calculations
On top of all this to get historical prices i want to download real data. To do this i will use data from yahoo finance.

I would ideally like to download 5 years of data for 100 stocks

The data i want to download includes
Date, Ticker, Open, High, Low, Close, Volume, Daily Change, Change %, 5-Day Change, 20-Day Change

To do this I am going to use yfinance

to install this we are going to type "pip install yfinance" into the terminal

Got an error using that so instead I am going to use python -m pip install yfinance

I created a new file called yfinance_downloaded
Within it I ran this code:
import yfinance as yf - from now one i ca njust type yf instead of yfinance

stock = yf.Ticker("GME") - I want information from GME

data = stock.history(period="20y")
.history - request information from past market history
period="20y" mean its installing data from the last 20 years

print(data.head())
shows all the data python  has gathered
.head gives the information from the first few days of trading so since i did period = 20y it would be data from 2006
.tail would give recent data

python code/yfinance_downloaded.py
loaded the data from 20 years ago 

The next step is to save the data into a CSV file

to do this I created a folder called saved_data and added 
data.to_csv("saved_data/GME.csv") to my code 

data.to_csv("saved_data/GME.csv") - takes the DataFrame stored in data and save it as a CSV file called GME.csv inside the data folder.

I now have 5333 lines of GME data saved on my computer 

DAY 33
07/08/2026
I installed 'Rainbow CSV'

Currently, the GME files i downloaded display Date,Open,High,Low,Close,Volume,Dividends,Stock Splits

To use this information we must first read the GME.csv file

import pandas as pd 
data = pd.read_csv("saved_data/GME.csv")  all the pandas read from the GME.csv file in saved_data folder is stored as a variable data 

print(data.head())

1. Daily Change
I want to create an option for daily change
data["Daily_Change"] = data["Close"] - data["Close"].shift(1)

It works on the principal of subtracting the current closing price from the previous day's price

data["Daily_Change"] - creates a new column inside the GME.csv called Daily_Change because the variable data was used to save the data in GME.csv

.shift(1) shifts off the values down by 1 row
eg
Close    Shift Close
  2         -
  56        2
  43        56
            43
so to get the daily change we do close - the shifted close 

Now I want to create daily return, and return for 5 days 20 days 100 days 365 days, and also volume return

2. Daily Return
To create daily return = current (close - previous close)/previous close
this code was straight forward 
data["Daily Return"] = (data["Close"] / data["Close"].shift(1))-1

3. 5 Day Return
for this you would do (current close - 5 days ago close)/5 days ago close
so my thought process is to shift the close down by 5 rows to get the 5 days ago

data["5 Day Return"] = (data["Close"] / data["Close"].shift(5))-1

4. Repeating for 10 days
5. Repeating for 20 days
6. Repeating for 100 days
7. Repeating for 200 days
8. Repeating for  1 year NB the stock market has 252 days of trading per year
9. Repeating for 2 years ie 504 days
10. Repeating for 5 years
11. Repeating for 10 years

DAY 34
08/08/2026

Today I want to build the volatility 

volatility  = Standard Deviation(R) x sqrtN where N = 252 trading days
I am implemnting 
1. Daily Volatiltiy N would be 252
2. 20 days  
3. 1 year

data["20 Day Volatility"] = data["Daily Return"].rolling(20).std() * (252**0.5)

.std - calculates the standard deviation of the values
.rolling - allows us to say how many rows we want to specify the data from
so .rolling(20) - takes data from 20 rows. It maybe start at Day 1 and end at Day 20and then after that Start on Day 2 and end on Day 21 ( This is formally called moving window)

next I am going to do Moving Average ( This is the average Stock prices across a period of time)
20 day moving average
100 day moving average 
1 year moving average
5 year moving average 
10 year moving average

data["20 Day Moving Average"] = data["Close"].rolling(20).mean()

.mean - calculates the average of the values

Next I am going to add one Volume Averages 

Volume average is the numebr of shares moved that day (sold or bought)
It is quite useful when it comes to figuring out how active the market is that particular day

I want to do the volume average for :
1 day
20 days
1 year
5 years
10 years
data["20 Day Average Volume"] = data["Volume"].rolling(20).mean()

DAY 35
09/08/2026

Today I want to do Volume vs Day Average

Volume vs average = Volume / Average Volume
1. Volume vs 20 Day avg = data["Volume"] / data["20 Day Average Volume"]
2. Volume vs 100 Day avg
3. Volume vs 1 Year avg
4. Volume vs 5 Year avg

All time High 
1. All time high = data["Close"].cummax()

.cummax() - highest point reache so far

Drawdown Dollar

.max() - finds the highest value anywhere in the data 
1. Drawdown Dollar = Peak Value - Current Value
Drawdown % 
2. Drawdown Percentage = ((Peak Value - Current Value) / Peak Value ) * 100
Max Drawdown $
3. max drawdown dollar = data["Drawdown $"].max()
Max Drawdown %
4. max drawdown percentage = data["Drawdown %"].max()

DAY 36 
10/08/2026

I want to get started with correlation so to do this I will have to  download more stocks 

I downloaded a few of the stocks I like... stocks = ["GME","MPWR", "CLS", "AXON", "TSLA", "PNRG", "AAPL", "MSFT", "NVDA", "ADBE", "AMD", "ORCL", " WLFC", "GOOG", "PLTR", "AVGO", "CVNA", "POWL", "SPOT", "LULU", "HUBS", "ASML", "CRM",
          "WIX", "WING", "TDG", "RBLX", "DUO", "ORLY", "COST", "SONY", "JPM", "V", "LLY", "CVS", "SBUX", "AMZN", "META"]

DAY 37 11/09/2026
.corr() - two sets of numbers and calculates correlation

so in this case to get the correlation I want to get the correlation between the daily return so I would 
calc te daily return for two different stocks and then do 

gme["Daily Return"].corr(tdg["Daily Return"])


So I want to get the correlation between GME and TDG so 
firstly I will read the information from GME and TDG
gme = pd.read_csv("saved_data/GME.csv")
tdg = pd.read_csv("saved_data/TDG.csv")

Next ill calculate the daily return for both
gme["Daily Return"] = (gme["Close"] / gme["Close"].shift(1))-1
tdg["Daily Return"] = (tdg["Close"] / tdg["Close"].shift(1))-1

Finally the correlation
correlation = gme["Daily Return"].corr(tdg["Daily Return"])

to get the value of the correlation we are going to do 
print(f"GME vs TDG Correlation: {correlation:.6f}")
.6f does 6 decimal places. 


Now  I want to be able to do this for every stock 
returns = {}
returns is now an empty dictionary


i used a for loop to help me with this so all the stock symbols are enterred into a returns dictionary 
for symbol in stocks:
    stock_data = pd.read_csv(f"saved_data/stock_data.csv") #NB: the f loads a different stock on each iteration 
    stock_data["Daily Return"] = (stock_data["Close"] / stock_data["Close"].shift(1))-1
    returns[symbol] = stock_data["Daily Return"]


pd.DataFrame is a panda function which creates a table of data so its taking the data from each stock enterred and giving it data
returns = pd.DataFrame(returns)


1. correlation_matrix = returns.corr()

i then found the correlation between all the data in the return dictionary 

print(correlation_matrix)
i outpted the correlation calculated. 

DAY 38
12/09/2026

Today its time to calculate the covariance.
so all i have to do is use .cov()

1. covariance_matrix = returns.cov()

Next, I want to get the overall returns of my portfolio
1. The expected returns would be the dot product of the equal weight and average return 

1. Average return = average_returns = returns.mean()

to do weights ( weight tell us where each % of money is invested)

1. weights = [1/len(stocks)] * len(stocks)
this creates equally weighted portfolio. 

Now to do the actual dot product. To find dot product you use @
average_return[:] @ equal_weights

1. Calculate the Annualized Return

the formula for Annualized return = (1 + Daily Return)^252 -1

Tomorrow I want to do portfolio risks.
DAY 39
13/09/2026

1. To get the volatilty, we can tak square root of portfolio variance

2. recall : portfolio variance = vector of weight * transposed weight vector * covariance matrix 

3. annulized volatility = daily volality x square of number of trading days (252)

Next, is the VaR - Value at Risk which is how much the portfolio can lose over a certain time period given a certain confidence interval . 

4. recall : Parametric VaR = porfolio return * ( z score * daily volatiltiy  - expected return) 

5. Historical VaR(%) = 5% percentile of the dot product between returns and equal weights
6. HistoricalVaR($) = portfolio value * abs(Historical VaR(%))

.quantile(0.05) - calculates the 5th percentile of the data set 

DAY 40 
14/09/2026  

7. Sharpe Ratio
Sharpe Ratio = (Expected return of the portfolio or asset - Risk-free rate of return)/ Standard deviation of the portfolio's excess return

8. Excess return = annualized return - risk free return
Set Risk_free_return to anything for now* so I am using 
I am using 4.72 as thats 10 year treasury note yield in US. 

9. Beta
Beta is given by the Covariance between the returns of the asset and the returns of the market divided by the the Variance of the market's returns

the code for that would be 
aligned_returns = pd.concat([returns, market_returns], axis=1, join="inner")
aligned_returns = aligned_returns.rename(columns={"Daily Return": "Market"}, inplace=True)

concat() is contentate and it combines data frames
right now we have 2 datasets the data set with all the stocks listed WLFC TSLA etc and then we have the benchmark S&P500
we combine them with concat()

to combine them we can put the coloumnsto right axes = 1 or axes = 0 for rows below

join="inner" is used so that the rows allign by index values this is important so that dates arent mis-matched.


aligned_returns.rename(columns={"Daily Return": "Market"}, inplace=True)

.rename is used to change the name of the columns only and this is only done for alligned returns 



DAY 40 14/08/2026
I want to implement the CAPM now that I have beta estabilished 

10. CAPM

For CAPM we need to a bench mark. So I am going to use the S%P500 
in python under yfinance library the S&P500 symbol is given by ^GSPC

Capital Asset Pricing Model (CAPM) calculates the expected return of an asset based on its systematic risk (Beta) and the expected return of the market

CAPM = Risk-free rate of return +  Beta of the asset * (Expected return -  Market Risk Premium (MRP))

DAY 41 15/08/2026
Very confused very lost
introduced numpy today

made equal weights into numpy 
average_return is still panda
ORGANIZATION
Okay so all the calculation need to get re done into separate modules. 
1. Market Data
    Historical Data

2. Stock Analysis
    Return
    Drawn down
    Voltaility
    Volume
    Moving Averages

3. Portfolio Analysis
    Sharpe Ratio
    Portfolio variance
    Portfolio volatility 
    Portfolio weights
    Portfolio weights

4. Risk Analysis
    VaR
    Monte Carlo
    Risk Distrubtions 

5. Asset Pricing 
    CAPM
    Black Scholes

6. Visualizaiton
    Charts
    Web UI

Now that i have it mapped out, today I started work on the Portfolio anlysis

I introduced numpy
numpy is a library used for large mathematical calcs involing matrices etc 

equal_weights = np.array([1/len(stocks)] * len(stocks))
equal weight now uses numpy becuase it makes the caluclation faster and it equal weight is an array calculation 

we will be using equal weight in matrix calc such as equal_weights @ covariance_matrix @ equal_weights to get dot product and find the total portfolio variance 

to create a numpy array we can use
np.array()

I moved expected portfolio returns to Portfolio anlysis but i am having problems importing. 
I do not want to import from yfinance_donwloaded as that would mean re downloadeding all 40 files which is inefficient. 

DAY 41
16/08/2026
I fixed the problem 

I want to my calculation to be inside th Portfolio Analysis so what that means is i can import the stock from yfinance into Portfolio Analysis just as I did when I was creating the yfinance_downloaded file.

I am just transfering the calculation from yfinance_downloaded to this next file Portfolio Anlysis.

To this the first few lines like i said would be the exact same as what was in the yfinance file

import numpy as np 
import pandas as pd

I am importing stocks because the yfinance folder should just store data for the 20 years. All other files like Portfolio Analysis just read that data using pd.read_csv(f"saved_data/s{symbol}.csv")


from yfinance_downloaded import stocks


returns = {}
for symbol in stocks:
    stock_data = pd.read_csv(f"saved_data/{symbol}.csv")
    stock_data["Daily Return"] = (stock_data["Close"] / stock_data["Close"].shift(1)) - 1
    returns[symbol] = stock_data["Daily Return"]

So for the selected stock we are going read that data which is stored in the yfinance file. We will use that data to calulcate the 

daily return, average return, weight, expected portfolio return. 

Everytime we calculate the Daily Return for some symbol that is stored in an array "returns = {}"

Next we want to turn the data in return = {} INTO  very nice neat organized table

to do this we usitlise panadas 

returns = pd.DataFrame(returns)

this creates a table of data so we can now perform calculations

average_return = returns.mean()

once again we use np.array (using number py for the array ) because weights is an matrix calculation and numpy makes matrix calculations faster. 

equal_weights = np.array([1 / len(stocks)] * len(stocks))
portfolio_return = (average_return * equal_weights).sum()
print(f"Portfolio Expected Daily Return: {portfolio_return * 100:.4f}%")

The point of all this is 
1. We have the data more orgnized by putting it into its own file 
2. By the use of using seprate files we can use numpy py to make the numberical calcs and matricies faster and pandas for tables 

DAY 42
17/08/2026

Today I am going to go through all the calculation in the yfinance_downloaded file and put comments on everyhting for where they are going to go and then i will copy and paste them into their respective sections after. 

Copy and pasted the covariance maxtrix into portfolio anlysis

I transferred
daily returns
average returns
equal weights
expected portfolio return
correlation matrix
covariance matrix
portfolio variance
daily volatility
annualized volatility

Tomorrow I want to complete this file.

DAY 43 18/08/2026

I added to portfolio anlysis.py 
1 VaR
2 Sharpe Ratio

for the beta it uses 
market = yf.Ticker("^GSPC")
market_data = market.history(period="20y")

so that data itself is already stored in yfinance_downloaded
All we have to do is read it in portfolio anlysis

so market_data = pd.read_csv("saved_data/^GSPC.csv")
I trasnferred Beta

I transferred CAPM in from yfinance file

Tomorrow i begin wrok on the stock analysis. 

DAY 44 19/08/2026
I want stock anlysis to contain
A way to input a stock of your choice:
1. returns (Daily, yearly etc)
2. volatility
3. moving averages
4. volume
5. drawdowns
6. correlation(comparasion in which we input a second stock)
7. Beta
8. CAPM
9. Sharpe Ratio
10. VaR
11. Summary Page

To begin we wnat to read data from the 20 year from in yfinance 
so 
symbol = input("Enter the stock symbol of your choice").upper()
data = pd.read_csv(f"saved_data/{symbol}.csv")

Then one we choose that stock
I pasted in the Daily return formula and editted it to be for {symbol}

I then pasted in the calcs for volatility, moving average, volum and draw downs

Tomorrow i want to do correlation:

DAY 45 20/08/2026
Today i want to do correlation and Beta

So for correlation i want to compare to specific stocks so i would prompt for input of a second stock
hence sec_stock
I then transferred all the previous code i had for correation and editted the names 

Next for Beta i started by copying over the code from yfinance, including the data which read the S%P500
i prompted to choose a specifc stock calculate allign returns
aligned_returns.columns = [symbol, "Market"]
stock_returns = aligned_returns[symbol]

and the rest of the beta was transfered from what was in yfinance


DAY 46 
21/08/2026
Today i want to hoepfully complete stock analysis

For the CAPM
I did the same thing i did with beta, i removed the for loop and instead prompted for a stock of the user choice, all further calculations where just transferred. 

For SHARPE RATIO
Most of the code remained the same here too 
excess_return = annualized_return - risk_free_rate
sharpe_ratio = excess_return / annualized_volatility

However i editted the calc for annualized return and annualized volatility so it would be for the s
specific stock enterred rather than the entire portfolio.
annualized_return = ((1 + stock_returns.mean()) ** 252) - 1
annualized_volatility = stock_returns.std() * (252 ** 0.5)

For VALUE AT RISK
It is basically the same just i changed dollar value to % value
confidence_level = 0.05
var_95 = stock_returns.quantile(confidence_level)
print(f"95% Daily VaR: {var_95 * 100:.2f}%")

Tomorrow ill do the last part of stock analysis
DAY 47
22/08/2026

Today I am going to work on a summary page for the stock anlysis section to end it off 

Okay so the summary sheet will display this data:
Current Price
All time high 
Previous Close

RETURNS
Monthly return
yearly return
5 year return

RISK
volatiltiy 
draw down 
beta
95% VaR

Risk Adjustment
CAPM
Sharpe 

CAPM expcted return

COMAPRSION
correlation


To print a banner like a aheader i can do a pattern of ==+==+==+==+==+==+==+==+==+==+==+==+==+==+
print("==+") * 30

to get the current price we want to use the last closing value so 
we would go into the data,  specific the column for close and we would use iloc to access the last row 
so current_price = data["Close"].iloc[-1]
iloc[-1] is  a panda which gives the last positon 


DAY 48
23/08/2026
So today I wnat to start working on the technical anlysis.
It will contain:
1. Moving Average
2. Volume Analysis
3. Trend
4. Momentum
5. RSI signals, MACD
6. Bullish or Bearish 

I created a file called technical anlysis.py and read the data for stock
once the user inputs the symbol they want they then get to analyze the data

to get the moving.. just like I did the stock anlysis... I recalculated the data rather than trying to import it for time purposes dont have ot redownload all the files. 

The first Feature I want to implement is the test whether the current prices is above or below to moving average. To do this, I wrote code for the moving average and current price 

Its pretty simple. if the current price is more than moving average then it is above, is it less, then it is below. 

DAY 49
24/08/2026

Today I finished the trends section. So its the calculte bullish or bearish. I did this for long term and Short term.

Shorter term is less than 1 year
Long term is 1 year or more

DAY 50
25/08/2026

Today I am going to create the momentum analysis
Momentum Analysis is much has the stock's price changed compared with x trading days ago

in the pandas library use pct_change() is used to calculate the percentage growth or drop between the current element and the prior one

data["20 Day Momentum"] = data["Close"].pct_change(20)

to get 20 day moment we do pct_changes starting from present date to 20 years.

I then did signal to show if the momentum was + or - 
if momentum20d > 0:
    momentum20_posneg = "Positive"
else:
    momentum20_posneg = "Negative"

DAY 51
26/08/2026

What is RSI?
The relative strength index is is a momentum oscillator used in technical analysis to measure the speed and change of price movements.

to calculate it RSI:

Relative strength = average gain/ average loss

RSI = 100 - (100/1+RS)

data["Price Change"] = data["Close"].diff()
.diff() calculates the difference between current close and previous close. 

.diff() exists only within the pandas library
.clip() exists only within the pandas library and its use is to set LIMITS

for examples .clip(lower=0) means the number can be less than 0 and can be infinitely larger than 0 
.clip(upper=0) means the number can be more than 0 and can be infinitely small than 0 
this number will be negative 

to get around this we would just muliplty by -1 since loss it self is postive

data["Average Gain"] = data["Gain"].rolling(14).mean()
the data is collected from the last 14 days ( Relative Strength Index (RSI) is calculated over a standard default period of 14)

relative_strength_index = gain_rsi / loss_rsi

rsi = 100 - (100 / (1 + relative_strength_index))

DAY 52
27/08/2026
RSI is over bought if it is > 70 and under bought if it is less than 30 
so i coded this using simple if statements 

#MACD - Moving Average Convergence Divergence is a trend-following momentum indicator that shows the relationship between two moving averages of an asset’s price.

The MACD is actually made up of three separate lines:
1. MACD LINE
    = 12 period EMA - 26 period EMA

2. Signal Line 
    = 9 period EMA of the MACD line

3. Historgram
    = MACD line - Signal Line


MACD = 12 DAY EMA - 26 DAY EMA

To calculate MACD line
to get the 12 period EMA 
data["12 Day EMA"] = data["Close"].ewm(span=12, adjust=False).mean()
.ewm() is used to calc the exponentially weight moving
span means it check its across 12 periods of trading days
ajudtstment = False ..  In pandas this is used to calc the recursive EMA method.

EMA:
Recent days get more importance
Older days get less importance

I thing calculated the 26 day EMA and found the difference ( that is the MAC) 

When the MACD is positive (above 0): The 12-day EMA is higher than the 26-day EMA.
 This means short-term upward momentum is accelerating faster than the long-term trend.
 
 When the MACD is negative (below 0): The 12-day EMA is lower than the 26-day EMA. 
 This means short-term selling momentum is accelerating downward.

MACD is exactly 0, it means that the 12-Day EMA and the 26-Day EMA are perfectly equal.
the value only becomes zero when those two moving averages cross paths and hit the exact same price.

Tomorrow i want to set up the SIGNAL line and as well as the options for Buy Sell HOLD

DAY 53
28/08/2026
Today I want to Add in the Volume Analysis
IN PANDAS 
 data["Volume"].rolling(10).mean() is the same as 
 data["Volume"].rolling(window = 10).mean()

Relative Volume (RVOL) = Current Volume / Average Volume

1. Institutional Surge
a Z-score greater than 2 and is backed by long-term liquidity.
to get a z score greater than 2 we do nu + 2 sd

long term liquid is if volume is greater than 100 days 

2. High Volume
Volume is > than 1.5 * mu

3. Low Volume (Illiquid / Drying Up)
Volume is < than 0.5 * mu

4. Normal / Average Volume
Volume is 0.5*mu < V < 1.5*mu

I did the vol analysis for 10 days 
Tomorrow I want to complete the Volume Analysis and include more days


DAY 54
29/08/2026
Today  I upgraded to Volume Analysis

I am adding a second signal for comparing
1. current vol > avg vol == high
2. current vol < avg vol == low
3. current vol == avg vol == average
I then spent time copying code and adding in 
 20 day 50 day 100 day 200day and 1 year

DAY 55
30/08/2026

Okay so for the BUY SELL HOLD, we will use a point system 
The point system should be out of 14.
+8 to +14  == Strong buy
 +4 to  +7  == Buy
 -3 to  +3  == Hold
 -4 to  -97  == Sell
-8 to -14  == Strong sell
Short   = 1
Medium  = 2
Long    = 3
Very Long  =2
20 Day Momentum = 1
100 Day Momentum = 2
RSI = 1
MACD = 2

Implemneted using if statments 

DAY 56
31/08/2026

Today I want to do testing and maintence to make sure everything works fine. 

for RSI, i added more possible outcomes to the if statement

RSI SIGNAL
Over sold < 30
Bearish < 45 
Neutral <= 55
Bullish <= 70
over bought  > 
 
I then updated this in the scoring system.

Everything works fine. 

I introduced Volume confirmation

AI Mode conversation: no eplxain the code the like financ ena f fomula behind it

#Volume Confirmation
if rvol20d >= 2:
    vol_confirm = "Very Strong"
elif rvol20d >= 1.5:
    vol_confirm = "Strong"
elif rvol20d >= 0.8:
    vol_confirm = "Normal"
else:
    vol_confirm = "Weak"
print(f"Volume Confirmation: {vol_confirm}")no eplxain the code the like financ ena f fomula behind it

#Volume Confirmation
If the assest is trading at more than 200% of its 20 day average volume,  then the relative volume RVOL
would be very strong and >= 2
Strong >= 1.5 so 150 - 199%
Normal is >= 0.8 so 80% to 149%
Weak < 0.8 so less than 80% 

i also multiplied rvol * 100 to get the %. 

DAY 57
1/08/2026
Today I am going to implement the confirmed signal

this is done by combining the final signal and the volume signal 

if the final signal from the scoring board is 
"x" 

x = strong buy, strong sell, hold, buy , sell

1. then its very strong volume means extremely strong x confirmed 

2. then it strong volume means strong x confirmed 

3. normal = strong x ( potentially )

4. weak = strong x ( weak volume)

DAY 58
02/08/2026
Today I want to complete the technical analysis by adding in the confluence 

 confluence occurs when multiple independent technical indicators or analysis tools point to the same market direction at the same time

 so in this case, I am getting data from 8 indicators 
1.  Short term trend
2. Medium term trend
3. Long term trend
4. Very long term trend
5. 20 day momentum
6. 100 day momentum 
7. MACD
8. relative strength indicator (RSI)


Agreement(%) = ( directional signal / total active signal ) * 100
Possible outcomes
Extremely Strong Agreement >= 87.5%
Strong Agreement >= 75%
Moderate Agreement >= 62.5%
Mixed Signals < 62.5%
bullish_signals = 0
bearish_signals = 0

The rule of thumb here to get the total directional would be to sum the total brearish + bullish 
bullish agreement would be the bullish/total 
bearish agreement would be the bearish/total

for each item + 1 if they occur 
SHORT-TERM TREND
Bullish = 1
Bearish = 1

MEDIUMmTERM TREND
Bullish = 1
Bearish = 1

LONG TERM TREND
Bullish = 1
Bearish = 1

VERY LONG TERM TREND
Bullish = 1
Bearish = 1

20 DAY MOMENTUM
Positive ( Bullish )= 1
Negative ( Bearish ) = 1

100 DAY MOMENTUM
Positive ( Bullish )= 1
Negative ( Bearish ) = 1

RSI
Bullish = 1
Bearish = 1

MACD
Bullish = 1
Bearish = 1

DAY 59
03/08/2026
Making final touches to techncial anlysis testing everything out

Changes made: 
I updated the scoring system in the RSI section

for the RSI section i introudced over bought and over sold. Mathemtically, this makes no difference
the reason being that it simples adds 0 to the score

elif rsi_posneg == "Oversold":
    signal_score += 0
elif rsi_posneg == "Overbought":
    signal_score += 0

The reason for the change that is +0 is because, over bought indicates a very fast and therefore
the asset is technically "cheap" and due for a bounceor 
for bearish assets stay oversold as panic selling continues
the assest's value is dropped very fast so  


Simply put over bought is too dangerous to put bullish and over sold is too bearish to put bearish 


Addtionally, i updated the Confluence as well although, mathematically, it makes no  differene. In that case
of over sold or under bought it would imply just pass 

elif rsi_posneg == "Oversold":
    pass
elif rsi_posneg == "Overbought":
    pass

DAY 60
04/08/2026
Today I am going to implement backtesting

Backtesting in a quantitative trading simulator is the process of testing a trading strategy or algorithm using historical market data to see how it would have performed in the past.

It work using input rules, historical runs, performance metrics. 

I spent today mostly planning and trying to figure how I would go about implementing back testing

okay so from what i get I have gathered. I need to recalculate the TECHNICAl indicators but with past stocks and i want to see how the out come is in the past and compare it to a potential result in the future. For exmaple if past stocks gave me buliish and it was right. I would compare and test how reliable those results wereand use it to Make a prediction. 

Back testing is its own section so I created backtesting.py 

It is basic repition of what I previously coded in the technical anlysis 

today I spent time 

importing numpy, pandas, reading the file for the stock information. 

I then pasted back in the Moving Averages and Momentum as a start.
Overall it is really simple. All I had to do was change 
current_price = data["Close"].iloc[-1]
to 
current_price = data["Close"].iloc[i]

for every line in which .loc[] was used we change that -1 to i. The reason is that it allows us to set up a
for loop which can used to look at the data given across different dates. 


Tomorrow Ill finish up the transferring. 


DAY 61
04/08/2026

I finished back testing today. 
I transfered Volume, RSI, MACD, Volality 
The rest of the code form technical analysis such as the scoring system is the exact same since
it is using data from the indicators which we used above. 

DAY 62
05/08/2026

Today I began the for loop set up. 

For the for loop itself I used : for i in range(252*5, len(data) - 20):

Since the oldest indicator we used was 5 years, it only made sense to use data from 5 years ago.

Len(data) is just how many rows are in the Panda Data frame. Alternativley i would just use 5332 as that covers the 20 years of data I have downloaded. Len(data) is more suitable incase I increase the amount of data Downloaded. 


DAY 63
06/08/2026

I then had to split up the data which I downloaded. 
As for the intialization of  the data such a recalling the columns date and value ( eg 20 Day movoing average), I moved that into a section above the loop.

I moved the data for Moving Average, Momentum, RSI, Volume, MACD. 

After added the pieces with loc[i] into the loop for the Moving average and the Momentum. 

Tomorrow I will complete this. 

DAY 64
07/08/2026

I moved MACD RSI, Volume and  Momentum, Scoring System and Confluence into the for loop. 
I alo decided from today I want to push everything to my Git and update it regularly.  


DAY 65 
08/08/2026
Today, I added in the newest part of the backtesting. That would be to get the predicated future value.
From here I would compare it to the actual future value and see how accurate it actaully was. 

Future prices = (new prices - current prices)/current_price

To get the future return i would need the new price(later date) and the current prices( the value of i)

so to get the new prices( all I have to do is choose an arbitary number for how far ahead i want the calculation to be for and add that to i). In this case i chose 20 days ahead I did i + 20 

future_price = data["Close"].iloc[i + 20]
future_return = (future_price / current_price) - 1
future_return_percent = future_return * 100

I implemented the if statements 
    if its Buy or Strong buy then check if the future price return > 0. That would mean its correct.

    if its Sell or Strong sell then check if the future price return > 0. That would mean its correct.

    else: 
        Hold

DAY 66 
09/08/2026

Today I want to work on saving the results which are attained. To do this i need to create a list.

So i introduced the list backtesting_summary and i appended all the data to the list. This data includes all the techncial indictors so Current Prices, Final Singal, Technical Score, Future Prices, Future Return(%) and Prediction Result

Similarly the i added all the indictors to a list in backtest_list the reason. That would include
Volume, MACD, RSI, Trends, Signals and Directional Agreement. 

Lastly i wrote code to give the name of the date, we we can know from when the data came from. This was easy all I had to do was 

To create the list i appended a simple string so  for exmaple "Date": date

    date = data["DATE"].iloc[i]


    Tomorrow I want to sort of the testing phase where we try different things and see how well they work. 


DAY 67 
10/08/2026

Testing the backtesting data and comparing them to how accurate they are. 

I put the back_test summary into a data frame and i also added the back test indicator to a data frame
backtest_dataframe_summary = pd.DataFrame(backtest_summary)
backtest_dataframe_indicators = pd.DataFrame(backtest_indicators)

I then merged these 2 data frames
now that they are in table format it is easy to perform calculations between the 2. 

backtest_results = pd.merge(backtest_dataframe_summary, backtest_dataframe_indicators,on="Date")

pd.merge - used ot merge 2 dataframes
on="Date" = this alligns the rows according to date so all the data macthes up 

For my first comparision:
We group all the rows according to RSI Signal
We then look at the future return for each signal and calculate the return. 
return_per_rsi_signal = backtest_results.groupby("RSI Signal")["Future Return(%)"].mean()
print(return_per_rsi_signal)

Day 68
11/08/2026

So my plan is to 

RSI performance — whether RSI signals were useful.
Prediction accuracy — compare the predictions to the future return direction
Final signal performance — did the technical-analysis system worked better for BUY, SELL etc. 

.groupby("RSI Signal") - This sorts all rows into groups based on the RSI Signal so if it is Over Bought, Under Bought etc

DAY 69
12/08/2026

Today I evalulated the accuracy of the RSI signal. To do this all i have to do is 

.value_counts() - this total ups the unique values in the data set

rsi_signal_counts = (backtest_results["RSI Signal"].value_counts())

what we are doing is we access the back test results datafram e and we are looking specifically at 
the RSI Signals Column, and we are counting all the Unqiue times we got the value appearing.

I also did  this with the Prediction Result Column

correct_predictions = (backtest_results["Prediction Result"] == "Correct").sum()

.sin() - It check for if the row is correct or incorrect, else it returns false. 
the accuracy is given correct predictions / total prediction 

DAY 70 
13/09/2026

I implemnted an if statement to only calc the accuracy if the total predicition was more than 0, else
an error is given . 

I am confused with the panda tables and I spent today trying to understand it thoroughly 


return_per_final_signal = (backtest_results.groupby("Final Singal")["Future Return (%)"].mean())


So we have a table like this 

Date      Stratergy Signal     Final Siganl       Future Return(%)


we what we are do is we access the back test dataframe 
from the final signal column we want to then group it so grouping according to Buy Sell Hold

so that what we call grouping them into buckets. We now have 3 buckets, buy sell and hold

Now that it is grouped by final signals
("Final Signal")["Future Return(%)] usilitzes data from the Future Return Column only, it forgets
Dates Stratgergy Signals and leaves just NUMERICAL Values beloning to Future Returns 

.mean()
would find the mean of each of the 3 buckets

so for example we found the mean of the Buy bucket. once we do this it is in the variable return_per_final_signal 


Ideally what we want to do is used the future return for 20 days and compare what it actuallly was 20 days down the road and see how accurate it was. 


final_signal_counts = (backtest_results["Final Singal"].value_counts())

This line now displays the list ["Buy", "Hold", "Buy", "Sell"]
and what it is doing is counting each on 
so we are count the number of Buys the number of Sell and the number of Holds

so it just gives us a better idea on the accuracy with numbers

DAY 71 
14/09/2026

BUY or STRONG BUY is correct if the future return is positive.
SELL or STRONG SELL is correct if the future return is negative.
HOLD is correct if the return is approximately flat.

I implemented an if else statement into the future retrn (%) higher up in my code.
so that the HOLD is correct if its includivse of 1 but incorrect otherwise. 

I now did some test to run the code and the terminal gave me 200 lines of code. It accurately showed the count for each buy sell etc, also it gave an accuracy prediction. Right now it is around 50%

DAY 72 
15/09/2026
Today I did a summary sheet for the the backtesting.

So i followed the same concept i used for when i did the last summary where i used the "=" * 50
to create a boarder from there
within the summary sheet i wrote some code for the overage all average.

Which would just be the average/ mean of the fuutre return column 
( Note that within the future column, each value is formed from the mean of the 20 days period)

The overall average of the future column(%) gives us a percentage idea
how the stock has moved within the histroy of the last  20 years. 

So i then wrote some if statement to explain this for people for who dont understand finance
for exmaple if the overal future average is more than 0 then it increased
if it less than 0 then it has decreased
if it is the same then it hasnt changed

The next thing i tried to do is write some code 
for the final comparision but I am currently getting an error so i need to try and
figure that out tomorrow

DAY 73
16/09/2026

I started of the day with all the code closed on visual studio so I had to re open it. At first when
i reopened it i was getting alot of trouble and i didnt know what to do so with a quick google search i was able to figure out what to do and open the files properly 

so basically what i learned to make sure you have all the files you downloaded is downloaded properly is that you can do 

import os
print()

also i learnt that if you do ../save/etc you can folder one above into the other. I did not complete understand what was going on here so i had to continue googling to figure out what was wrong. Then  i leanred i could go back on my git hub and reopen everything so i was back to here i started yesterday

So now to address the problem i was having yesterday. Well simply put

The panadas dataframe for backtestinc couldnt find the Future Signal column
so i checked my Future Signal Column by typing in 

print(backtest_results.columns.tolist())

From what i saw i typed Singal not Signal so that caused on error so i fixed that. 

DAY 74 17/09/2026

Today, I continued with Stratification. 
final_signal_performance = backtest_results.groupby("Final Signal")["Future Return (%)"].agg(["mean", "count"])

we went to the final signal column and we grouped by Buy Sell Hold fomr here we used to future returns
to calculate the mean and the count. 

NB: .agg(["mean", "count"])
.agg mean to aggragate and calculate multiple stats at the same time rather than doing them separately
so what we did is find the mean the average return for each signal as well as a total count of each signal occuring. 

I spent some time writing code to make the terminal look better by adding spaces and indenting fixing decimal places. etc


Future Plans:
From next day I want to continue into 
Win rate by Final Signal -  how often each signal worked

Cumulative strategy return - what would happen if you followed the signals through the historical periods

Maximum drawdown - how large the worst historical decline was

But I need to do more research on this first. 

DAY 75 18/09/2026

Today I want to implement win rate by final signal

win rate by final signal  =  correct predictions * 100 / total predicitions

this was the line of code i wrote:
winrate_by_final_signal = backtest_results.groupby("Final Signal")["Prediction Result"].apply(lambda x: (x == "Correct").mean() * 100)

so we are doing here is going in the back test dataframe,  going to the final signal column ( Buy Sell Hold Strong buy Strong Sell) and grouping by if it was correct or incorrect ( Prediction Result)

.apply() works like a loop so in this case 
so what is doing is applying this function lambda to every single group of data we just created

lambda - is like defining a function but inside pandas so the variable x is going through the entire list and if x == correct it counts as 1 else its 0. So it then does is sums all the 1s and calcs the mean ( aka correct predicitions / total prediction) 

DAY 76 19/09/2026

Today I want the implement is Cumulative Statergy Return 

Rt - is the return over a period of time so in my case that would be in a period of 20 days. 
In this case Rt is given the position return (Signal t) * R asset 

Long position 
if the Stratergy has a Buy signal, it means you are holding the asset. Your return is the same as the market's return.

If your stratgery is to SELL and your return is opposite of the market's return

Flat position if Rt is 0 and there is no signal, no matter how much the asset moves up or down, the return for the day is 0.

I spent like an hour on this trying to properly understand it. 

So firstly we created a new columb called Stratergy Return (%)

np.where - this is like a i statement so 
The baasic stucture is np.where(condition, value_if_true, value_if_false)

eg np.where(5 > 3, "Yes", "No")
output = yes

and inside the backtest_result Dataframe we are going to Final Signal Columnand if we see Buy
then that means both buy and strong buy would return true and everything else would just be false

the same goes for sell 




backtest_results["Strategy Return (%)"] = np.where(backtest_results["Final Signal"].str.contains("BUY"),
backtest_results["Future Return (%)"], np.where(backtest_results["Final Signal"].str.contains("SELL"),
-backtest_results["Future Return (%)"], 0 ))


For sell we used to negative sign to reverse the sign of the return 

0 - means to HOLD


.cumprod = means cumulative product

Tomorrow I want to start the Maximum Draw down. 

DAY 77 
20/09/2026

