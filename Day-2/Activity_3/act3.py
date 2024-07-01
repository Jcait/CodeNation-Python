from colorama import Fore, Back, Style

def ageChecker():
    age = int(input("What is your age?:"))
    if age >= 18:
        print(Back.GREEN + "Yes I can serve you")
        print(Style.RESET_ALL)
    else:
        print(Back.RED + "I'm sorry I can't serve you")
        print(Style.RESET_ALL)

ageChecker()