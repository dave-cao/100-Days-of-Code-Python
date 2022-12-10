# A calculator program

import art


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(art.logo)

    num1 = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)

    end_program = False
    while not end_program:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the second number?: "))

        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Change the new number to do the operation on ot the previous result
        num1 = answer

        # End condition or use previous answer to calulate with another number
        should_continue = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to to start a new calculation.: "
        ).lower()

        if should_continue == "n":
            end_program = True
            # recursion to start a brand new calculation
            calculator()


calculator()
