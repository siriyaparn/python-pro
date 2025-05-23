# Import module
import random
from art import logo, vs
from game_data import data

# Display art logo
print(logo)

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return(f"{account_name}, a {account_descr}, form {account_country}")

def check_answer(user_guess, a_followers, b_followers):
    """Takes a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers: 
        return user_guess == "a"
    else:
        return user_guess == "b"

score = 0
game_should_conitnue = True
account_b = random.choice(data)

# Make a game repeatable
while game_should_conitnue:
    # Generate a random account from the game data
    # Making account at position B become the next account at position A
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        ccount_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess
    guess = input(f"Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen
    print("\n" * 20)

    # Check if user is correct
    ## Get follower count of each account
    a_follow_account = account_a["follower"]
    b_follow_account = account_b["follower"]

    ## Use if statement to check if user is correct
    is_correct = check_answer(guess, a_follow_account, b_follow_account)

    # Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_conitnue = False
