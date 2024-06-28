# Activity 1

Create a program that stores someone’s name, age
and favourite colour, then print these in a complete
sentence.

## Step one

Create the Variables to store the data

```python
my_name=  "JJ"
my_age = 32
fave_colour = "Blue"
```

## Step Two

Print the variables in a complete sentence using string interpolation with the prefix f
for example f("STRING{VARIABLE}MORESTRING")

```python
my_name=  "Josh"
my_age = 32
fave_colour = "Blue"
print(f"My name is {my_name} i am {my_age} years old and my favourite color is {fave_colour}.")
```

This prints out the Following in the Terminal:
My name is JJ i am 32 years old and my favourite color is Blue.

## Addendum

We can also define a function to print this as well

```python
# Activity One Code Nation python

my_name=  "JJ"
my_age = 32
fave_colour = "Blue"

def prog():
    print(f"My name is {my_name} i am {my_age} years old and my favourite color is {fave_colour}.")

prog()
```
