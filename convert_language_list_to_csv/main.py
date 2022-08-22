import pandas

with open("italian_top_k.txt", "r") as file:
    data = file.readlines()

new_data = {"word": [item.split()[0] for item in data]}

frame = pandas.DataFrame(new_data)

frame.to_csv("italian_top_k.csv")