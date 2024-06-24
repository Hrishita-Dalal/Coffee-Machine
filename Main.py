import os
from Menu import Menu, MenuItem
from Coffee_Maker import CoffeeMaker
from Money_Machine import MoneyMachine


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True
while is_on:
    clear()
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
