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
you get options to view charts, run calcs, see next day predicitons

