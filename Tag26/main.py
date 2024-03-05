import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")

final_nato = {value.letter: value.code for (index, value) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
text = list(input("Enter a Word: ").upper())

value = [final_nato[letter] for letter in text]

print(value)

