# Import module
import random

# Step 1: Picking random words and checking answers
# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
#print(chosen_word)

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter (Please input only one letter): ").lower()
while len(guess) > 1 :
    guess = input("Guess a letter (Please input only one letter): ").lower()
#print(guess)

# Check if the letter the user guessed (guess) is one of the letters in the chosen_word
for letter in range(len(chosen_word)):
    if guess == chosen_word[letter]:
        print("Right")
    else:
        print("Wrong")
