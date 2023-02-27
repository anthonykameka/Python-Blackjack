from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()
items = menu.get_items().split("/")[:-1]

def turn_on():
    on = True
    while on:
        water = cm.resources["water"]
        milk = cm.resources["milk"]
        coffee = cm.resources["coffee"]
        choice = prompt()

        if choice == "off":
            on = False
        elif choice == "report":
            cm.report()
            mm.report()
        elif choice not in items:
            choice = prompt()
        else:

            drink = menu.find_drink(choice)
            print(f"the cost is {drink.cost}")
            if cm.is_resource_sufficient(drink):
                if mm.make_payment(drink.cost):
                    cm.make_coffee(drink)
                    water -= drink.ingredients["water"]
                    milk -= drink.ingredients["milk"]
                    coffee -= drink.ingredients["coffee"]
                    print(f"Here is your {drink.name} Enjoy!!")


def prompt():
    choice = input(f"What would you like? ({menu.get_items()}):\n")

    return choice


turn_on()