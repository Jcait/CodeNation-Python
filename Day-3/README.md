# Day 3

## Functions

## Challenge

On the following slide is an example of a function that
includes a parameter.
Parameters are responsible for functions being able to work
on different data inputs.
Edit the snippet on the following slide to include two or
more parameters, a running order count that updates when
the function is called and change the .format method to
f string.

### example

```python
order_count = 0

def take_order(topping):
    global order_count
    print("Pizza with {}".format(topping))
    order_count += 1

take_order("Pineapple")
```

### My Code

Taking the brief, my take_order takes in 3 inputs from the customer and will also add money from the charge, The only issue there is at the moment that I know of is having a space between the toppings name will charge you for one extra, e.g "Extra Cheese" would charge £1.50

```python
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

print(take_order(input("What size pizza would you like?: "), input("Enter your toppings, please leave a space between each: "), input("Finally what crust would you like: ")))
```
