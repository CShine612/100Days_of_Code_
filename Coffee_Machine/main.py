from prettytable import PrettyTable

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def coin_input():
    while True:
        quarters = input("How many quarters?")
        dimes = input("How many dimes?")
        nickles = input("How many nickles?")
        pennies = input("How many pennies?")
        if quarters.isnumeric() and dimes.isnumeric() and nickles.isnumeric() and pennies.isnumeric():
            total = (0.25 * int(quarters)) + (0.10 * int(dimes)) + (0.05 * int(nickles)) + (0.01 * int(pennies))
            break
        else:
            print("Please input numbers only")
    return total

while True:
    request = input("What would you like? (espresso/latte/cappuccino): ")
    if request.lower() == "off":
        break
    elif request.lower() == "report":
        table = PrettyTable()
        table.add_column("Reasorce", list(resources.keys()))
        table.add_column("Quantity", list(resources.values()))
        print(table)

        print("Water: " + str(resources["water"]) + "ml")
        print("Milk: " + str(resources["milk"]) + "ml")
        print("Coffee: " + str(resources["coffee"]) + "g")
        print("Money: $" + str(resources["money"]))
    elif request.lower() not in MENU.keys():
        print("Please make a valid selection")
    elif resources["water"] < MENU[request]["ingredients"]["water"] or resources["milk"] < MENU[request]["ingredients"]["milk"] or resources["coffee"] < MENU[request]["ingredients"]["coffee"]:
        print("Insufficient Resources")
    else:
        tendered = coin_input()
        if tendered < MENU[request]["cost"]:
            print("Insufficient Funds")
        else:
            change = tendered - MENU[request]["cost"]
            print("Here is your change: $" + str(change))
            resources["money"] += MENU[request]["cost"]
            resources["water"] -= MENU[request]["ingredients"]["water"]
            resources["milk"] -= MENU[request]["ingredients"]["milk"]
            resources["coffee"] -= MENU[request]["ingredients"]["coffee"]
            print(f"Here is your {request} enjoy")