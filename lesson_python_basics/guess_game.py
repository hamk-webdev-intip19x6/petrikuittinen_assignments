""" TASK: To make a game, where player is trying to guess a random
number between 1...100. The player has maximum 10 guess attemps.
If the player guesses the correct number within those attempts, he wins.
The game tells if his guess is too small or large."""

import random


MAX_ATTEMPTS = 5  # maximum number of attempts
MIN_N = 1    # minimum integer to guess 
MAX_N = 100  # maximum integer to guess
n = random.randint(MIN_N, MAX_N)  # random integer between MIN_N and MAX_N

attempts = 0
while attempts < MAX_ATTEMPTS:
    guess = int(input("Guess a number?"))
    attempts += 1
    if guess < n:
        print("Too small")
    elif guess > n:
        print("Too large")
    elif guess == n:
        print("Correct!")
        break
else:
    print("You ran out of attempts")
    print("The number was", n)
    
