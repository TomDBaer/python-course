MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
}


def report():
    """
    Print the current resources
    """
    print(
        f"""
            Water: {resources["water"]}
            Milk: {resources["milk"]}
            Coffee: {resources["coffee"]}
            Money: ${resources["money"]}
        """)
    pass


def money_input(name):
    pennies = int(input("How many Pennies?: ")) * 0.01
    nickles = int(input("How many Nickles?: ")) * 0.05
    dimes = int(input("How many Dimes?: ")) * 0.10
    quarters = int(input("How many Quarters?: ")) * 0.25
    summe = pennies + nickles + dimes + quarters
    if summe < MENU[name]['cost']:
        return f"Sorry, your {name} costs {MENU[name]['cost']} but you only gave {summe}"
    wechselgeld = summe - MENU[name]['cost']
    resources['money'] += MENU[name]['cost']
    remove_resource(name)
    return f"Money accepted, processing...\nYour exchange is {wechselgeld}"


def remove_resource(name):
    for ingredient in MENU[name]['ingredients']:
        resources[ingredient] -= MENU[name]['ingredients'][ingredient]


def check_resources(name):
    for ingredient in MENU[name]['ingredients']:
        if MENU[name]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient} in the tank")
            return False
    print(f"Your order '{name}' is processed")
    return True


def coffee_machine() -> None:
    system_operating = True

    # add money to the dict
    resources['money'] = 0

    while system_operating:
        eingabe = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if eingabe == "espresso":
            check = check_resources(eingabe)
            if check:
                change = money_input(eingabe)
                print(change)
        elif eingabe == "latte":
            check = check_resources(eingabe)
            if check:
                change = money_input(eingabe)
                print(change)
        elif eingabe == "cappuccino":
            check = check_resources(eingabe)
            if check:
                change = money_input(eingabe)
                print(change)
        elif eingabe == "report":
            report()
            print("You entered report")
        elif eingabe == "off":
            print("Maintenance")
            system_operating = False
        else:
            print("Sorry, I didn't get that")


coffee_machine()
