import pandas

file = pandas.read_csv("./nato_phonetic_alphabet.csv")
NATO_dict = {row.letter: row.code for (_, row) in file.iterrows()}


end_game = False
while not end_game:
    try:
        word = input("What is your word?: ")
        result = [NATO_dict[letter] for letter in word.upper()]
        print(result)
        end_game = True
    except KeyError:
        print("Sorry, only letters in the alphabet please")
