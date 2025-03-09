# Import module
import random
import game_data
from art import logo

# Display art logo
print(logo)

# Generate a random account from the game data
account = random.choice(game_data.data)
print(account['name'])