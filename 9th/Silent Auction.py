
from art import logo
print(logo)

def find_highest_bidder (bidding_record):
    highest_bid = 0
    winner_name = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount> highest_bid:
            highest_bid = bid_amount
            winner_name = bidder
    print(f"The winner is {winner_name} with a bid of ${highest_bid}")


bidders = {}
should_continue = "yes"
while should_continue == "yes":
    bidder_name = input("Enter your name: ").lower()
    bid_price = int(input("Enter your Bid price: "))
    bidders[bidder_name] = bid_price

    while True:
        continue_or_not = input("Are there any other bidders? Type \"Yes\" to continue and \"No\" to End: ").lower()
        if continue_or_not == "yes":
            print("\n" * 100)
            break
        elif continue_or_not == "no":
            find_highest_bidder(bidders)
            should_continue = "no"
            break
        else:
            print("Invalid input. Please type 'Yes' or 'No'.")



