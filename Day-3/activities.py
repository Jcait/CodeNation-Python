# Activity 1


# v_line = "  |  "
# h_line = "-------------"
# space_0 = " "
# space_1 = " "
# space_2 = " o "
# space_3 = " x "
# space_4 = " "
# space_5 = " x "
# space_6 = " x "
# space_7 = " "
# space_8 = " o "




# def checkWin(space1, space2, space3):

#     space_0 = " "
#     space_1 = " "
#     space_2 = "o"
#     space_3 = "x"
#     space_4 = " "
#     space_5 = "x"
#     space_6 = "x"
#     space_7 = " "
#     space_8 = "o"
#     space = " "
#     print(space1, space2, space3)
#     match(space_0,space_1,space_2):
#         case "o","o","o":
#             print("o is the winner")
#         case "x","x","x":
#             print("x is the winner")
#         case _:
#             print("anyone could win!")
    
#     # if space1 == "o" and space2 == "o" and space3 == "o":
#     #     print("o is the winner")
#     # elif space1 == "x" and space2 == "x" and space3 == "x":
#     #     print("x is the winner")
#     # else:
#     #     print("It can still be anyones game")

#     print(space, v_line, space,v_line, space)
#     print(space_0,v_line, space_1,v_line, space_2)
#     print(space,v_line, space, v_line, space)
#     print(h_line+h_line)
#     print(space, v_line, space, v_line, space)
#     print(space_3,v_line, space_4, v_line, space_5)
#     print(space, v_line, space, v_line, space)
#     print(h_line+h_line)
#     print(space, v_line, space,v_line, space)
#     print(space_6, v_line, space_7,v_line, space_8)
#     print(space,  v_line, space,v_line, space)

# checkWin("o","o","o")
# checkWin("x","x","x")
# checkWin("o","x","o")

# activity 2

# def ticketMachine():
#     age= int(input("Please enter your age: "))

#     match age:
#         case age if age < 18:
#             print("Your ticket will be £8.00")
#         case age if age > 18 and age < 60:
#             print("Your ticket will be £10.95")
#         case age if age > 60:
#             print("Your ticket will be £7.50")
    
#     if age < 18:
#         print("Your ticket will be £8.00")
#     elif age >18 and age < 60:
#         print("Your ticket will be £10.95")
#     else:
#         print("Your ticket will be £7.50")

# ticketMachine()

# test = print

# test("test")

drink = "tea"

def coffeeOrder(size):
    match size.lower():
        case size if size == "s" or size == "m" or size == "l" or  size =="xl":
            print(f"Your {size.upper()} {drink} will be ready shortly")
        case _:
            print(" ")

def price(size):
    match size.lower():
        case "s":
            print("your drink will cost you £3.00")
        case "m":
            print("Your drink will cost you £5.00")
        case "l":
            print("Your drink will cost you £6.50")
        case "xl":
            print("Your drink will cost you £7.00")
        case _:
            print("Please enter a valid size")

def placeOrder(size):
    global drink
    drink = "coffee"
    coffeeOrder(size)
    price(size)

placeOrder("xl")
        
