# Create functions
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
# Input
first_number = float(input("What is the first number?: "))
for symbol in operations:      # Print the example of symbol
    print(symbol)
operation_synbol = input("Pick an operation: ")
second_number = float(input("What is the next number?: "))

# Call function
answer = operations[operation_synbol](first_number, second_number)
print(f"{first_number} {operation_synbol} {second_number} = {answer}")

ask = input("Do you want to continue?: ")