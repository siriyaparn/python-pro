# Menu
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "co,ffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients":{
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0,
    },
}
profit = 0 
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

def is_resources_sufficient(order_ingredients):
    """Returns True when the order can be made , False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not empty {item}")
            return False
    return True

def process_coin():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        is_resources_sufficient(drink["ingredients"])
        payment = process_coin()