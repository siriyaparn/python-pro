# Import module
import random
from art import logo
from game_data import data

# Display art logo
print(logo)

def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    print(f"{account_name}, a {account_descr}, form {account_country}")

# Generate a random account from the game data
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    ccount_b = random.choice(data)

print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
print("vs")
print(f"Compare B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")

# Ask user for a guess
ans = input(f"Who has more followers? Type 'A' or 'B': ")

# Check if user is correct
## Get follower count of each account
## Use if statement to check if user is correct


# Give user feedback on their guess
