# Step 1
import os
import random

import hangman_art
import hangman_words


def clear():
    clear_command = "clear"
    if os.name == "nt":
        clear_command = "cls"
    os.system(clear_command)


word = random.choice(hangman_words.word_list)
lives = 6

# Starting logo
print(hangman_art.logo)

# Display underscores
display = []
for _ in range(len(word)):
    display.append("_")


# Make the game repeatable
end_game = False
while not end_game:
    guess = input("Guess a letter: ").lower()

    clear()

    # Check to see if user guessed the same letter twice in a row
    if guess in display:
        print(f"You've already guessd the letter {guess}!")

    # If the user guesses correctly, put that letter in list
    for index, letter in enumerate(word):
        if guess == letter:
            display[index] = letter

    # Decrease lives if not correct
    if guess not in word:
        lives -= 1
        print(f"The letter {guess} is not in the word! You lose a life")

    print(hangman_art.stages[lives])
    print(f"{' '.join(display)}\n")

    # Check end game condition
    if "_" not in display:
        end_game = True
        print("You Win!")
    elif lives < 1:
        end_game = True
        print(f"You lose! The word was {word}")
