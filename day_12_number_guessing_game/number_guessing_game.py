# Project 12 of 100 Day Python Bootcamp

# =========== Number Guessing Game =============

# The computer thinks of a number between 1 - 100 and you have to figure out what the
# number is. When you guess a number, the computer will tell you if it's higher or lower.
#
# On easy mode, you will get 10 attempts.
# On hard mode, you will get 5 attempts.
# ============================================

import random

import art

# Get a random number from 1 - 100
answer = random.randint(1, 100)

# welcome message
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


def main():
    # set difficulties
    attempts = 10
    if difficulty == "hard":
        attempts = 5

    end_game = False
    while not end_game and attempts > 0:
        guess = int(input("Make a guess: "))

        # decrease attempts every time user guesses wrong
        attempts -= 1

        # continue asking user for input until they get the correct answer
        if guess > answer:
            print("Too high.")
        elif guess < answer:
            print("Too low.")
        else:
            print(f"You got it! The answer was {answer}")
            end_game = True
            return

        # Tell user number of attempts left
        if attempts:
            print("Guess again.")
            print(f"The number of attempts you have is {attempts}")
        else:
            print("You've run out of guesses, you lose.")


main()
