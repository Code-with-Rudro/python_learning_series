# Number Guessing Game:
# This is a simple number guessing game where the player has to guess a randomly generated number within a certain range. The game provides feedback on whether the player's guess is too low, too high, or correct. The player can choose the difficulty level, which determines the range of numbers and the number of attempts allowed.
from itertools import count
import random 

n = random.randint(1,100)



a = -1

guess = 0

while(a!=n):
    guess +=1
    a = int(input("Guess the number (Between 1 to 100): "))

    if(a > n):
        print("LOWER NUMBER PLEASE")
    else:
        print("HIGHER NUMBER PLEASE")
print("Your guess is right:", a, "correct guess", guess, "chanceses are you take.")

