# Import module
import random
from art import logo, vs
from game_data import data

# Display art logo
print(logo)

def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return(f"{account_name}, a {account_descr}, form {account_country}")

# Generate a random account from the game data
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    ccount_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}.")
print(vs)
print(f"Against B: {format_data(account_b)}.")

# Ask user for a guess
guess = input(f"Who has more followers? Type 'A' or 'B': ").lower()

# Check if user is correct
## Get follower count of each account
a_follow_account = account_a["follower_count"]
b_follow_account = account_b["follower_count"]

## Use if statement to check if user is correct


# Give user feedback on their guess
