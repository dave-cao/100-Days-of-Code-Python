from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

end_game = False
my_coffee = CoffeeMaker()
my_money = MoneyMachine()
menu = Menu()
while not end_game:
    options = menu.get_items()
    coffee_choice = input(f"What would you like? ({options}): ").lower()

    if coffee_choice == "off":
        end_game = True
    elif coffee_choice == "report":
        my_coffee.report()
        my_money.report()
    else:
        # check if resources are sufficient
        my_drink = Menu().find_drink(coffee_choice)
        if my_coffee.is_resource_sufficient(my_drink) and my_drink:
            my_money.make_payment(my_drink.cost)
            my_coffee.make_coffee(my_drink)
