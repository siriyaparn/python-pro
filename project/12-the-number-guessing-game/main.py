# Import module
import random
from art import logo

print(logo)

# Function to check answer
def check_answer(user_guess, actual_answer):
    if user_guess > actual_answer:
        print("Too high.")
        attempt -= 1
    elif user_guess < actual_answer:
        print("Too low.")
        attempt -= 1
    else:
        print(f"You got it! The answer was {actual_answer}")

# Choosing random number between 1 and 100
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_number = random.randint(1,100)