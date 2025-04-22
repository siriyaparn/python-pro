from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create objects
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

# Print report
coffee_maker.report()
money_machine.report()

# Check resources sufficients
while is_on:
    options = menu.get_items()