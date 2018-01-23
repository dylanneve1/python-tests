''' Number guessing '''

import random

x = 0

num = random.randint(1,100)

print("I'm thinking of a number between 1 and 100. Guess it!")

while x == 0:
    
    theGuess = int(input("Your guess: "))
    
    if theGuess == num:
        print("You got it!")
        x = 1
        
    elif theGuess > num:
        print("Try again, it's a smaller number")

    elif theGuess < num:
        print("Try again, it's a bigger number")

    else:
        print("That is not a valid number. Please try again")
