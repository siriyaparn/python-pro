# Import module
import random
from art import logo

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play == 'y':
    print(logo)

# Create function to return a random card
def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # Ace = 11
    card = random.choice(cards)
    return card

# Create function to calculate score
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    # Check a blackjack: a hand with only 2 cards: Ace and 10 and returns 0 which will respresent a blackjack in our game
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Check for an ace(11): if the score is already over 21, replace 11 with 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Declear parameters
user_cards = []
computer_cards = []
user_score = -1
computer_score = -1
is_game_over = False

# Ramdom cards
for _ in range(2):
    # Append random cards to lists
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not is_game_over:
    # Calculate score
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards : {user_cards} , current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    # Game condition
    if user_score == 0 or computer_score == 0 or user_score > 21: 
        is_game_over = True   # End game
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == 'y':
            user_cards.append(deal_card())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)