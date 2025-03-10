# Import module
import random
import game_data
from art import logo

# Display art logo
print(logo)

# Generate a random account from the game data
a = random.choice(game_data.data)
print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
print("vs")

b = random.choice(game_data.data)
print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}.")
ans = input(f"Who has more followers? Type 'A' or 'B': ")