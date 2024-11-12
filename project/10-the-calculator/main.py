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

# Use a dictionary operations to perform the calculations
first_number = float(input("What is the first number?: "))

# Print the example of symbol
for symbol in operations:
    print(symbol)

operation_synbol = input("Pick an operation: ")
second_number = float(input("What is the next number?: "))