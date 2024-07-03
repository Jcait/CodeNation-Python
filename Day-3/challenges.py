# Challenge one
import random
from decimal import Decimal

order_number = random.randint(1, 100)

def take_order(size, topping, crust):
    global order_number
    order_number+= 1
    print(f"Your {size.lower()} {topping.lower()} with {crust.lower()} crust Pizza is on it's way. Your order number is {order_number} and will cost £{round(Decimal(5.00)+ Decimal(topping_charge(topping)), 2)} ")

def topping_charge(topping):
    if topping.find(" ") > 0:
        toppings =topping.split()
        return float(0.75 * len(toppings))

# take_order("Medium", ["Pineapple", "Pepperoni", "Extra Cheese"], "Stuffed")

# print(take_order(input("What size pizza would you like?: "), input("Enter your toppings, please leave a space between each: "), input("Finally what crust would you like: ")))


# Challenfe 2
security_pin = random.randint(1, 1000)
account_balance = random.randint(150, 600)

def banking(enter_pin):
    if security_pin != enter_pin:
        pin_checker(enter_pin)
    bank_greet()

def bank_greet():
    print("Please enter the letter that meets your query, if you would like to [Q]uit, please press Q")
    print(f"You have £{round(Decimal(account_balance), 2)} funds at your disposal")
    bank_query = input("Are you here to make a [W]ithdrawel, [D]eposit, Take out a [L]oan or are you seeking financial [H]elp: ")
    bank_function(bank_query)

def bank_function(query):
        match query.lower():
            case "w":
                withdraw = int(input("How Much Will you be Withdrawing from your account?: "))
                withdrawel(withdraw)
            case "d":
                deposited = int(input("How much will you be depositing?: "))
                deposit(deposited)
            case "l":
                loan_amount = int(input("How big of a loan will you taking today? "))
                loan(loan_amount)
            case "h":
                print("We cannot currently offer this service due to legal worries.")
                print("Returning to home menu!")
                bank_greet()
            case "q":
                print("Thank you for banking with BANK")
                quit()
            case _:
                print("Please enter a valid Letter")
                bank_greet()

def withdrawel(withdraw):
    global account_balance
    if  withdraw > account_balance:
        print("You do not have the necessary funds to complete the transaction")
        print("Returning to Home Menu")
        bank_greet()
    else:
        account_balance -= withdraw
        print(f"You have withdrawn £{Decimal(withdraw)} from your account leaving you with £{Decimal(account_balance)} funds at your disposal")
        bank_greet()

def deposit(deposited):
    global account_balance
    account_balance += deposited
    print(f"You have deposited £{Decimal(deposited)} into your account, you have £{Decimal(account_balance)} funds avaliable")

def loan(loan_amount):
    print(f"Here at BANK we charge 2% interest on all loans (It's just easier that way) and expect payback within 5 years, your loan of £{loan_amount} can be paid over the course of 5 years at £{loan_calc(loan_amount)} a month")
    agreement = input("Do you agree to this loan? [Y]es/[N]o")
    loan_agreement(agreement, loan_amount)


def loan_agreement(agreement, loan_amount):
        global account_balance
        match agreement.lower():
            case "y":
                account_balance += loan_amount
                print("Thank you for doing business, please note if payment cannot be maintained we will seek recompense via other methods within our legal power.")
            case "n":
                print("Returning to home menu")
                bank_greet()
            case _:
                print("Please answer [Y]es or [N]o")
                loan_agreement(agreement)
    

def loan_calc(loan_amount):
    rate = 1 / 12
    months = 5 * 12
    value1 = ((1+rate)**float(months))-1
    value2 = (rate*(1+rate)**float(months))
    val3 = value1 / value2
    month_pay = loan_amount / val3

    return round(Decimal((month_pay)), 2)

def pin_checker(enter_pin):
    i = 1 
    while i < 3:
        enter_pin = input("Please enter your pin: ")

        if enter_pin == "":
            i+= 1
        elif security_pin == int(enter_pin):
            i = 4
            return enter_pin
        else:
            i+= 1
    print("You have run out of attempts, security will be with you shortly")
    quit()
    
print(f"Your security pin is {security_pin}")
banking(input("Please enter your pin: "))