from art import logo
print(logo)

bids = {}
# Whether if new bids need to be added
should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n")

continue_bidding = True
while continue_bidding:
    # input
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))

    # Save data into dictionary {name:price}
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n")