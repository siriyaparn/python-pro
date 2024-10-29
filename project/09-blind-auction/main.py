from art import logo
print(logo)

# Compare bids in dictionary
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {}
continue_bidding = True
while continue_bidding:
    # input
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))

    # Save data into dictionary {name:price}
    bids[name] = price

    # Whether if new bids need to be added
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if should_continue == 'no':
        continue_bidding = False
        find_highest_bidder(bids)
        print(bids)
    elif should_continue == "yes":
        print("\n" * 30)