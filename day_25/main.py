import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_colour_count = {"grey": 0, "red": 0, "black": 0}

for item in data["Primary Fur Color"]:
    if item == "Gray":
        fur_colour_count["grey"] += 1
    elif item == "Cinnamon":
        fur_colour_count["red"] += 1
    elif item == "Black":
        fur_colour_count["black"] += 1

count_formatted = {"Colour": list(fur_colour_count.keys()), "Count": list(fur_colour_count.values())}

count_data = pandas.DataFrame(count_formatted)
count_data.to_csv("squirrel_count.csv")