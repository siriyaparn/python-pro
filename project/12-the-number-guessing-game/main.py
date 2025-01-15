# Import module
import random
from art import logo

print(logo)

# Global variable
EASY_MODE_TURNS = 10
HARD_MODE_TURNS = 5

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

# Function to set difficulty
def set_difficulty():
    mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if mode == 'easy':
        return EASY_MODE_TURNS
    else:
        return HARD_MODE_TURNS

# Choosing random number between 1 and 100
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_number = random.randint(1,100)
print(f"Pssst, the correct answer is {random_number}")


turns = set_difficulty()
print(f"Ypu have {turns} attempts remaining to guess he number.")

# Repeat the guessing functionality if they get it wrong.
guess = 0
while guess != random_number:
    # Let user guess a number
    guess = int(input("Make a guess: "))
