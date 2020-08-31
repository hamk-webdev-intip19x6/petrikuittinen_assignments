""" TASK: To make a game, where player is trying to guess a random
number between 1...100. The player has maximum 10 guess attemps.
If the player guesses the correct number within those attempts, he wins.
The game tells if his guess is too small or large."""

import random

MAX_ATTEMPTS = 7  # maximum number of attempts
MIN_N = 1    # minimum integer to guess 
MAX_N = 100  # maximum integer to guess
n = random.randint(MIN_N, MAX_N)  # random integer between MIN_N and MAX_N


def ask_integer(s, error_message="Please give valid integers."):
    """print s and ask an integer from user. It will keep asking
until user provides a valid integer and then returns the integer"""
    while True:
        try:
            return int(input(s))
        except ValueError:
            print(error_message)

print("Guess a number between", MIN_N, "and", MAX_N)
attempts = 0
while attempts < MAX_ATTEMPTS:
    print("You have", MAX_ATTEMPTS-attempts, "attempts left")
    guess = ask_integer("Guess a number?")
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
    
