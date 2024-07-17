# Simple function
def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")
greet()


# Function that allows for input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
greet_with_name("Alice")  
## Output
# Hello Alice
# How do you do Alice?


# Function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
greet_with("Alice", "New York")
## Output
# Hello Alice
# What is it like in New York?

# Function with keyword argument
greet_with(name = "Alice", location = "New York")
## Output
# Hello Alice
# What is it like in New York?