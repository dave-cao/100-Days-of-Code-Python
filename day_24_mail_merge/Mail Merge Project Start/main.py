with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.readlines()

with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()


for name in names:
    dear_line = f"Dear {name}"
    letter[0] = dear_line

    with open(f"./Output/ReadyToSend/{name}.txt", "w") as file:
        file.write("".join(letter))
