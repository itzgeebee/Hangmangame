# A simple code that conerts letters to NATO codes
import pandas

new_df = pandas.read_csv("NATO_alphabet/nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in new_df.iterrows()}

def nato_converter():
    name = input("Enter your name: ").upper()
    try:

        nato_name = [nato_dict[letter] for letter in name]

    except KeyError:
        nato_converter()
    else:
        print(nato_name)
nato_converter()