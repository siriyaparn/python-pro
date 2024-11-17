
from art import logo

# Create operation functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Add functions into a dictionary as the value
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Create calculator function
def calculator():
    print(logo)
    should_calculate = True
    first_number = float(input("What is the first number?: "))

    while should_calculate:
        
        for symbol in operations:      # Print the example of symbol
            print(symbol)
        operation_synbol = input("Pick an operation: ")
        second_number = float(input("What is the next number?: "))

        # Call function
        answer = operations[operation_synbol](first_number, second_number)
        print(f"{first_number} {operation_synbol} {second_number} = {answer}")

        choice = input(f"Type 'y' to continue calculating {answer}, or type 'n' to start a new calculation.")
        if choice == 'y':
            first_number = answer
        else:
            should_calculate = False
            print("/n" * 20)
            calculator()

# Call function calculator
calculator()