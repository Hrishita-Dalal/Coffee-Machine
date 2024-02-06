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
    "money": 0,
}


def check_resources(order_ingredients):
    check = True
    for resource in order_ingredients:
        if order_ingredients[resource] > resources[resource]:
            print(f"Sorry there is not enough {resource}.")
            check = False
    return check


def process_money(entry):
    money = int(input("Enter money in terms of rupees: "))
    if money == MENU[entry]["cost"]:
        resources["money"] += money
    elif money > MENU[entry]["cost"]:
        change = round(money - MENU[entry]["cost"], 2)
        print(f"Here is {change} rupees in change.")
        resources["money"] += (money - change)
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    return True


def make_coffee(order_ingredients):
    for resource in order_ingredients:
        resources[resource] -= order_ingredients[resource]
    print(f"Here is your {coffee}. Enjoy!")


while True:
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee == "report":    # gives information about resources
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: {resources['money']} rupees")
    elif coffee == "espresso" or coffee == "latte" or coffee == "cappuccino":
        resources_available = check_resources(MENU[coffee]["ingredients"])
        if resources_available:
            money_paid = process_money(coffee)
            if money_paid:
                make_coffee(MENU[coffee]["ingredients"])
    elif coffee == "off":    # turns the machine off
        break
    else:
        print("Enter a valid option.")
