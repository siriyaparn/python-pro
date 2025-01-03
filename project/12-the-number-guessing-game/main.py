# Import module
import random
from art import logo

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
random_number = random.randint(1,100)

if mode == "easy":
    attempt = 10
else:
    attempt = 5