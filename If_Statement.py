from random import randint
import time

def guessing_Game():
    print("Think of a Number between 0 to 10")
    time.sleep(3)                                                                   # function imported from librabry "time" to delay execution of time
    y = randint(0, 10)
    print("Is " , y , " the number you were thinking of?")                          # function randint generates a random number between a given range
    answer = input("Input 'y' for yes or 'n' for no: ")
    if(answer == "y"):
      print("Magical!")
    elif(answer == "n"):
       print("Huh... that's weird")
    else:
       print("You have to input either \"y\" or \"n\" ")
    return y

# if statements follow the typical "python" format which uses margins to indicate bodys.
# elseif is indicatet with the keyword elif
