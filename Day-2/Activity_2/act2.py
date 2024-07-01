import random

print("enter your dice number")

def  dice():
    num = int(input())
    num2 = random.randint(0, int(num))
    print(f"you rolled a {random.randint(0, int(num))}")
    if num2 < 3:
        print("You have been slain by an ogre")
    else:
        print("You have defeated the ogre")

dice()