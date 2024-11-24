# Import module
import random
from art import logo

# Declear parameters
user_cards = []
computer_cards = []

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play == 'y':
    print(logo)

# Create function to return a random card
def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # Ace = 11
    card = random.choice(cards)
    return card

for _ in range(2):
    # Append random cards to lists
    user_cards.append(deal_card())
    computer_cards.append(deal_card())