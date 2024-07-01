import random
from colorama import Fore, Back, Style


print(Fore.RED + 'some red text')


print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Fore.BLUE)
print(Back.RED)
print(Style.BRIGHT + "Blinding")
print(Style.RESET_ALL)
print('back to normal now')




print("enter your dice number")

def  dice():
    num = int(input())
    num2 = random.randint(0, num)
    weapon= "spear"

    match num2:
        case num2 if num2 < 3 and weapon !="spear":
            print(Back.RED + "You have been slain by an ogre")
            print(Style.RESET_ALL)
        case num2 if num == 20:
            print(Back.BLUE + "You effortlessly behead the ogre")
            print(Style.RESET_ALL)
        case _:
            print(Back.GREEN +"You have defeated the ogre")
            print(Style.RESET_ALL)



dice()