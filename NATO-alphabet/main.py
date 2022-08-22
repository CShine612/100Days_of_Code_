import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

def nato():
    word = input("Please enter a word: ")
    try:
        nato_word = [nato_dict[let] for let in word.upper()]
        print(nato_word)
    except KeyError:
        print("Sorry please enter only letters")
        nato()

nato()
