# Activity 2

Create a program that stores what you eat today for
breakfast, lunch and dinner.
Print these.
Update each of these variables to what you will eat
tomorrow.
Print these.

## Step 1

We create the variables as we did in Activity one

```python
# Activity 2 Codenation

my_breakfast = "Cereal"
my_lunch = "Noodles"
my_dinner = "Mac n Cheese"

food = ["Cereal", "Noodles", "Mac n Cheese"]
```

For this activity, I believe it wants them as separate variables, but to make life easier.
They could also be stored in an array.

## Step 2

We print the first statement requested using string interpolation with the prefix f, like in activity 1.
As you can see below, string interpolation can also be used with arrays; we list the index so the whole array isn't printed.

```python
# Activity 2 Codenation

my_breakfast = "Cereal"
my_lunch = "Noodles"
my_dinner = "Mac n Cheese"

food = ["Cereal", "Noodles", "Mac n Cheese"]

print(f"My Meals are as follows: Breakfast: {my_breakfast}, Lunch: {my_lunch}, Dinner: {my_dinner}.")
print(f"My Meals are as follows: Breakfast: {food[0]}, Lunch: {food[1]}, Dinner: {food[2]}.")

```

## Step 3

The activity wants the variables updated; we can change them below the print methods since Python works from the top to the bottom of the file.

```python
print(f"My Meals are as follows: Breakfast: {my_breakfast}, Lunch: {my_lunch}, Dinner: {my_dinner}.")
print(f"My Meals are as follows: Breakfast: {food[0]}, Lunch: {food[1]}, Dinner: {food[2]}.")

 my_breakfast = "Omelette"
 my_lunch = "Leftover Pizza"
 my_dinner = "Burgers"
 food = ["Omelette", "Leftover Pizza", "Burgers"]
```

## Step 4

Since we haven't changed the variable names, we can just copy and paste the preceding code to achieve the desired result.

```python
print(f"My Meals are as follows: Breakfast: {my_breakfast}, Lunch: {my_lunch}, Dinner: {my_dinner}.")
print(f"My Meals are as follows: Breakfast: {food[0]}, Lunch: {food[1]}, Dinner: {food[2]}.")

 my_breakfast = "Omelette"
 my_lunch = "Leftover Pizza"
 my_dinner = "Burgers"
 food = ["Omelette", "Leftover Pizza", "Burgers"]

 print(f"My Meals are as follows: Breakfast: {my_breakfast}, Lunch: {my_lunch}, Dinner: {my_dinner}.")
print(f"My Meals are as follows: Breakfast: {food[0]}, Lunch: {food[1]}, Dinner: {food[2]}.")
```

## Extra

The above can also be achieved if we write two functions, one to print the variables and one to change the global variables. If we declare global before the variable name, then change it.
The below only shows it done with the food array (to save time), but it could work with any of our food variables.

```python
def changeVar():
   global food
   food = ["Omelette", "Leftover Pizza", "Burgers"]

def prog():
   print(f"My Meals are as follows: Breakfast: {food[0]}, Lunch: {food[1]}, Dinner: {food[2]}.")
   changeVar()
   print(f"My Meals are as follows: Breakfast: {food[0]}, Lunch: {food[1]}, Dinner: {food[2]}.")

prog()
```
