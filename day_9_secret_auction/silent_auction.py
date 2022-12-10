# A secret auction program that allows different users to make bids.
# The winner is the one who bids the most

import os

import art


def clear():
    # Clears the screen
    clear_command = "clear"
    if os.name == "nt":
        clear_command = "cls"
    os.system(clear_command)


print(art.logo)


bid_log = {}
end_game = False
while not end_game:
    bid_name = input("What is your name? ")
    bid_price = int(input("What is your bid price? $"))

    # Log bidder into bid_log
    bid_log[bid_name] = bid_price

    # Ask if there are more bidders
    continue_game = input("Are there any other users who want to bid? Yes, No ").lower()
    clear()
    if continue_game == "no":
        end_game = True


# Print final results
highest_bid = 0
winner = {}
for bidder in bid_log:
    if bid_log[bidder] > highest_bid:
        highest_bid = bid_log[bidder]
        winner["name"] = bidder
        winner["price"] = highest_bid

print(f'The winner is {winner["name"]} with a bid price of ${winner["price"]}!')
