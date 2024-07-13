# Import module
import random

# Randomly choose a word from the word_list
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
print(f"Pssst, the solution word is {chosen_word}")

# Create an empty List
display = []
for _ in range(word_length):
    display.append("_")
print(display)

# Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in 
# the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end_of_game = False

while not end_of_game:
    # Input guess a letter
    guess = input("Guess a letter (Please input only one letter): ").lower()
    while len(guess) > 1 :
        guess = input("Guess a letter (Please input only one letter): ").lower()
    #print(guess)

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter 
    # Print display
    print(display)   

    if "_" not in display:
        end_of_game = True
        print("You win.")