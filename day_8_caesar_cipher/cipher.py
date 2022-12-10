# This program will get a keyword from the user and use the caesar cipher
# encryption method to encrypt the word
import art

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


print(art.logo)


def caesar(text, shift, direction):
    # 1. Find all positions of text letters in alphabet
    message = ""
    alpha_len = len(alphabet)

    # Use case if decrypt vs encrypt
    if direction == "decode":
        shift *= -1

    for letter in text:
        # Check to see if letter is in alphabet
        if letter in alphabet:
            position = alphabet.index(letter)
            new_pos = position + shift

            # use case if number is greater than 26 or less then 0
            new_pos %= alpha_len

            message += alphabet[new_pos]
        else:
            message += letter

    print(f"The {direction}d text is {message}")


end_game = False
while not end_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    decision = input("End the program? yes or no ").lower()
    if decision == "yes":
        end_game = True
