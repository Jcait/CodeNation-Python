# Challenges

## Challenge one

Create a Variable called Password
Check how many letters are in the password, if there are less than 8 print that the password is too short
Otherwise print the new password

Create a function that takes the input as the password and compares against the designated length.

```python
def newPassword():
    password = input("Please input your new password: ")
    if ( len(password) < 8):
        print(f"Your password is too short! it needs to be {8 - len(password)} characters longer")
    else:
        print(f"Your new password is: {password}")
newPassword()
```

## Challenge Two

Create a Variable called num
Check if Variable is divisible by 3 or 5, if it is print "This number is divisible by 3 or 5" to the console.
Otherwise print "This number is not divisible by 3 or 5" to the console

Create a function like last time, but a number is taken in the input and checked with an if or conditional rather than write about multiple ifs.

```python
def divThreeOrFive():
    num = int(input("Please enter a number: "))
    if (num % 3 == 0) or (num % 5 == 0):
        print("This number is divisible by 3 or 5")
    else:
        print("This number is not divisible by 3 or 5")
```

## Challenge Three

Create a Variable called num
if num is divisible by 7 print "Fizz" If num is divisible by 3 print "Buzz"
If num is divisible by 3 and 7 print "Fizzbuzz"
If num is divisble by neither print num.

Can edit the code in Challenge 2, just changing the or to an and and adding 2 more conditonals to check.

```python
def fizzBuzz():
    num = int(input("Please enter a number: "))
    if (num % 7 == 0) and (num % 3 == 0):
        print("FizzBuzz!")
    elif (num % 7 == 0):
        print("Buzz!!")
    elif (num % 3 == 0):
        print("Fizz!!")
    else:
        print(num)
```

## Challenge Four

Create a variable called word that takes a string.
create an if statement that checks if the last letter is the same as the first.
if it is return true otherwise return false

After researching the string methods for python most of the work can be done with .endswith() if using the first letter of the variable at index 0 which will return True or False depending on the word

```python
def firstIsLast():
    word = input("Please enter a word: ").strip()
    print(word.endswith(word[0]))

```

### Challenge Five

SKIP

### Challenge Six

Create Two Variables called num1 and num2
Create an if statement that checks if the result of the sum is even
if it is return a success message

```python
def isAnsEqual():
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    if ((num1 + num2) % 2 == 0):
        print("The answer is equal!")
    else:
        print("The answer is not equal")
```

### Challenge Seven

Create a variable called num
Check if the number is a palindrome (the same forwards and backwards)
First look into creating a list (array) for the input, once done we reverse the list and rejoin it as a string before comparing the new reverse number against the original one set. if they're the same then it a palindrome

```python
def numPalindrome():
    num = input("please enter a number: ")
    list_num = list(num)
    reverse_list = list(reversed(list_num))
    reverse_ans = "".join(reverse_list)
    if (num == reverse_ans):
        print("You number is a palindrome")
    else:
        print("This number is not a palindrome")

```
