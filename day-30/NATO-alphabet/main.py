import pandas as pd
#load csv
data = pd.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter:row.code for (index,row) in data.iterrows()}
def nato():
    try:
        input_word = input("Enter a word: ")
        result = [alphabet_dict[letter] for letter in input_word.upper()]
    except KeyError:
        print("Sorry only letters in the alphabet please.")
        nato()
    else:
        print(result)

nato()