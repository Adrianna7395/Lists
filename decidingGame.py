name = input("type your name: ")
print("welcome", name, "to this adventure")

answer = input("you are on a dirt road, you wanna go left or right? ").lower()

if answer == "left":
    answer = input("you come to a river. type walk or swim")
    if answer == "swim ":
        print("you were eaten by an alligator")
    elif answer == "walk ":
        print("you walked many miles and got lost")
    else:
        print("Not a valid option, you lose")
elif answer == "right":
    answer = input("you came to a bridge, do you want to cross it or head back (cross/back)? ")
    if answer == "back":
        print("you have got back and lost")
    elif answer == "cross":
        answer = input("you meet a stranger and talk to them (yes/no) ")
        if answer == "yes":
            print("you win")
        elif answer == "no":
            print("you lose")
        else:
            print("Not a valid option, you lose.")
    else:
        print("Not a valid option, you lose.")

else:
    print("Not a valid option, you lose")

print("thank you for playing a game")