
with open("Input/Names/invited_names.txt") as file:
    name_list = file.readlines()

with open("Input/Letters/starting_letter.txt") as file:
    letter = file.read()


for name in name_list:
    name = name.strip()
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as file:
        file.write(letter.replace("[name]", name))