# Activity One Code Nation python

my_name=  "Josh"
my_age = 32
fave_colour = "Blue"
print(f"My name is {my_name} i am {my_age} years old and my favourite color is {fave_colour}.")

food = ["Cereal", "Sandwhich", "Curry"]

def changeVar():
    global food
    food = ["Bacon", "Noodles", "Burger"]

def prog():
    print(f"My name is {my_name} i am {my_age} years old and my favourite color is {fave_colour}.")
    print(f"For breakfast I'll have {food[0]}, Lunch: {food[1]}, Dinner: {food[2]}.")
    changeVar()
    print(f"Tomorrow I'll have, Breakfast: {food[0]}, Lunch: {food[1]}, Dinner: {food[2]}.")    

prog()