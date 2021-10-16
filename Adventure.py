import time as tm
import random as rm


# Story intro
def displayIntro():
    print("\n")
    print("there is a wall in front of your house")
    tm.sleep(3)
    print("and one day you decided to jump over it and see what's behind")
    tm.sleep(3)
    print("it's a dark forest full of big trees")
    tm.sleep(3)
    print("you get in and now you are lost")
    tm.sleep(3)
    print("suddenly you met an old man with a big white beard")
    tm.sleep(3)


def chosenPath():
    global path
    print("the old man: 'Hello son! welcome to forbidden forest to go out")
    tm.sleep(1)
    print("you have to choose between those two roads to find your way home")
    # Input validation
    path = ""
    while path != "1" and path != "2":
        path = input("Now choose wisely 1 or 2: ")

    return path


# output for the chosen path
def checkPath(chosenpath):
    correctPath = rm.randint(1, 2)

    if chosenpath == correctPath:
        tm.sleep(2)
        print("Good choice now ! You back to your Home safely!")
    else:
        tm.sleep(2)
        print("Poor human! you had chose the road of death")

displayIntro()
chosenPath()
checkPath(chosenPath)

while True:
    Answer = str(input("Do you want to try again? (Y/N): "))
    if Answer == "Y" or Answer == "y":
        displayIntro()
        chosenPath()
        checkPath(chosenPath)
    else:
        exit()

