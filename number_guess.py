''' Number guessing '''

import random

x = 0

num = random.randint(1,100)

print("I'm thinking of a number between 1 and 100. Guess it!")

while x == x:
    theGuess = int(input("Your guess: "))
    if theGuess == num:
        print("You got it!")
        x = 1
    else:
        print("Try again")
