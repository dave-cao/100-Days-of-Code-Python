# A Rock paper scissors game
# Learning how to use modules and nested lists

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]


# Computer [tie, User wins, Comp wins]
#          [Comp wins, tie, User wins]
#          [User wins, Comp wins, tie]
#                User

# 0 = tie
# 1 = USer wins
# 2 = Comp wins

check_result = [[0, 1, 2], [2, 0, 1], [1, 2, 0]]

# Get computer choice by random
computer_choice = random.randint(0, 2)


# Get user choice
user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
)

# Print overall choices
print(choices[user_choice])
print(f"Computer chose\n{choices[computer_choice]}")


# Check who won
if not check_result[computer_choice][user_choice]:
    print("You tied!")
elif check_result[computer_choice][user_choice] == 1:
    print("You win!")
elif check_result[computer_choice][user_choice] == 2:
    print("You lose!")
else:
    print("Invalid number inputted")
