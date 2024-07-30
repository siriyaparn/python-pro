import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Create list for images
game_images = [rock, paper, scissors]

# Input player chioce
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
while player_choice not in [0, 1, 2]:
    player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print(f"Player choice: {player_choice}")
print(game_images[player_choice])

# Random computer chioce
computer_choice = random.randint(0, 2)
print(f"Computer choice: {computer_choice}")
print(game_images[computer_choice])

# Game condition
if player_choice == computer_choice:
    print("It's a draw!")
elif (player_choice == 0 and computer_choice == 2) or \
     (player_choice == 1 and computer_choice == 0) or \
     (player_choice == 2 and computer_choice == 1) :
    print("You win!")
else:
    print("You lose!!")