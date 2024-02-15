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
    },
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coin():
    total = int(input("How many quarters are you inserting:")) * 0.25
    total += int(input("How many dimes are you inserting:")) * 0.10
    total += int(input("How many quarters are you inserting:")) * 0.05
    total += int(input("How many quarters are you inserting:")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry not enough money. Money refunded")
        return False
