# Import module
import random
import game_data
from art import logo

# Display art logo
print(logo)

# Generate a random account from the game data
account_a = random.choice(game_data.data)
account_b = random.choice(game_data.data)
if account_a == account_b:
    ccount_b = random.choice(game_data.data)
    
print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
print("vs")
print(f"Compare B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")

# Ask user for a guess
ans = input(f"Who has more followers? Type 'A' or 'B': ")

# Check if user is correct
## Get follower count of each account
## Use if statement to check if user is correct


# Give user feedback on their guess
