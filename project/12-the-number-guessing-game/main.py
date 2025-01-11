# Import module
import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
random_number = random.randint(1,100)

def easy():
    attempt = 10
    if attempt <= 10 and attempt != 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > random_number:
            print("Too high.")
            attempt -= 1
        elif guess < random_number:
            print("Too low.")
            attempt -= 1
        elif guess == random_number:
            print("You win!")
    elif attempt == 0:
        print("You lose.")

def hard():
    attempt = 5

if mode == "easy":
    easy()
else:
    hard()