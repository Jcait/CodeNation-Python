
#  Challenge 1

def newPassword():
    password = input("Please input your new password: ")
    if ( len(password) < 8):
        print(f"Your password is too short! it needs to be {8 - len(password)} characters longer")
    else:
        print(f"Your new password is: {password}")

# Challenge 2

def divThreeOrFive():
    num = int(input("Please enter a number: "))
    if (num % 3 == 0) or (num % 5 == 0):
        print("This number is divisible by 3 or 5")
    else:
        print("This number is not divisible by 3 or 5")


# Challenge 3

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

# Challenge 4

def firstIsLast():
    word = input("Please enter a word: ").strip()
    print(word.endswith(word[0]))

# Challrnge 6

def isAnsEqual():
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    if ((num1 + num2) % 2 == 0):
        print("The answer is equal!")
    else:
        print("The answer is not equal")

# Challenge 7

def numPalindrome():
    num = input("please enter a number: ")
    list_num = list(num)
    reverse_list = list(reversed(list_num))
    reverse_ans = "".join(reverse_list)
    if (num == reverse_ans):
        print("You number is a palindrome")
    else:
        print("This number is not a palindrome")
    
string = "sadsafdsafdsdsjgfbds,fdsfweofhwefdsmfewrewasdaslanasjfndsmlfdfssadsadawefewgwefwiooedwfww"

# Challenge 8

def findVowel():
    last_vowel = None
    last_vowel_num = 0
    string = "sadsafdsafdsdsjgfbds,fdsfweofhwefdsmfewrewasdaslanasjfndsmlfdfssadsadawefewgeeeuuuooowefwiooedwfwwi"
    vowels = ["a", "e", "i", "o", "u"]

    for x in vowels:
        if string.rfind(x) > last_vowel_num:
            last_vowel_num = string.rfind(x)
            last_vowel = x
    print(f"The last vowel used in {string} is {last_vowel}")


findVowel()
# numPalindrome()
# isAnsEqual()
# firstIsLast()
# newPassword()
# divThreeOrFive()
# fizzBuzz()
# Challenge 

