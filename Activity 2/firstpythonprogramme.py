# Activity 2 Codenation

my_breakfast = "Cereal"
my_lunch = "Noodles"
my_dinner = "Mac n Cheese"

food = ["Cereal", "Noodles", "Mac n Cheese"]

def changeVar():
    global food
    food = ["Omelette", "Leftover Pizza", "Burgers"]
     
def prog():
    print(f"My Meals are as follows: Breakfast: {food[0]}, Lunch: {food[1]}, Dinner: {food[2]}.")
    changeVar()
    print(f"My Meals are as follows: Breakfast: {food[0]}, Lunch: {food[1]}, Dinner: {food[2]}.")

prog()



# print(f"My Meals are as follows: Breakfast: {my_breakfast}, Lunch: {my_lunch}, Dinner: {my_dinner}.")
# print(f"My Meals are as follows: Breakfast: {food[0]}, Lunch: {food[1]}, Dinner: {food[2]}.")

#  my_breakfast = "Omelette"
#  my_lunch = "Leftover Pizza"
#  my_dinner = "Burgers"
#  food = ["Omelette", "Leftover Pizza", "Burgers"]

#  print(f"For tomorrow I will have: Breakfast{my_breakfast}, Lunch{my_lunch}, Dinner{my_dinner}")
#  print(f"My Meals are as follows: Breakfast: {food[0]}, Lunch: {food[1]}, Dinner: {food[2]}.")
