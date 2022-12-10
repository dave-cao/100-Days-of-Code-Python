# Day 14 - Higher or Lower Game

# ===== Rules =====
# 1. Guess between two people...who has the higher follower count?
# 2. If you guess correctly, you get a point and move to the next round
# 3. Guess wrong and it's game over.
# =================


# 1. Compare two people with each other
# 2. If you guess correctly, "B" is moved to "A" and a new "B" is generated

import os
import random

import art
from game_data import data


def clear():
    clear_command = "clear"
    if os.name == "nt":
        clear_command = "cls"
    os.system(clear_command)


def check_winner(person_a, person_b):
    """Returns the person with more followers as a string. Both args are dictionaries
    'a' represents person_a
    'b' represents person_b
    """

    if person_a["follower_count"] > person_b["follower_count"]:
        return "a"
    else:
        return "b"


def print_welcome():
    """Clears screen and then prints logo"""
    clear()
    print(art.logo)


# Shuffle data and print welcome screen
random.shuffle(data)
print_welcome()

# Game variables
score = 0
data_index = 0
end_game = False

while not end_game:
    person_a = data[data_index]
    person_b = data[data_index + 1]

    # print data in readable format
    print(
        f'Compare A: {person_a["name"]}, a {person_a["description"]}, from {person_a["country"]}'
    )
    print(art.vs)
    print(
        f'Compare B: {person_b["name"]}, a {person_b["description"]}, from {person_b["country"]}'
    )

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print_welcome()

    # Decide if user is correct or not
    winner = check_winner(person_a, person_b)
    if guess == winner:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        end_game = True
        print(f"Sorry, that's wrong. Final score: {score}")

    # Update persons
    data_index += 1

    # use case if user goes out of range
    if data_index >= len(data) - 1:
        end_game = True
        print(f"You've won the game! Max score: {score}")
