# A program that simulates a coffee machine
# This coffee machine only takes in coints for money
from data import MENU, resources


def process_coins(quarters, dimes, nickles, pennies):
    """Returns the total amount of money from quarters, dimes. nickels, and pennies
    Each arg is an int
    Returns a float with two decimals"""
    total = 0
    total += quarters * 0.25
    total += dimes * 0.10
    total += nickles * 0.05
    total += pennies * 0.01
    return round(total, 2)


def process_ingredients(coffee_choice):
    """Returns a dictionary of resources that you have left based on
    the user coffee choice. Returns a tuple with 0 as 0 index and 1 for the missing
    ingredient.
    coffee_choice: string of coffee choice
    resources: dictionary of ingredients you have left"""
    ingredients = MENU[coffee_choice]["ingredients"]
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
        if resources[ingredient] < 0:
            return (0, ingredient)
    return (1, resources)


def play_game():
    money = 0
    end_game = False
    while not end_game:
        # 1 Prompt user by asking "What would you like?"
        coffee_choice = input(
            "What would you like? (espresso/latte/cappuccino): "
        ).lower()

        # if user inputs "off" then turn machine off
        if coffee_choice == "off":
            return

        # if user inputs "report" then print current resources in machine
        if coffee_choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money}")
            continue

        # Check to see if sufficient resources
        new_resources = process_ingredients(coffee_choice)
        if not new_resources[0]:
            end_game = True
            print(f"Sorry there is not enough {new_resources[1]}.")
            return

        # Ask for coins
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))

        # Process coins
        cost = MENU[coffee_choice]["cost"]
        coin_total = process_coins(quarters, dimes, nickles, pennies)
        change = coin_total - cost

        #   If user didn't give enough money, then tell them
        if change < 0:
            print("Sorry, that's not enough money. Money refunded.")
            end_game = True
            return

        # update money in machine if everything goes well
        money += cost

        # give user the coffee
        print(f"Here is ${change} in change.")
        print(f"Here is your {coffee_choice}. Enjoy!")


play_game()
