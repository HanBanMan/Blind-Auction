import art
print(art.logo)

more_bidders = "yes"
auction = {}
while more_bidders == "yes":
    name = input("What's your name? ").lower()
    price = int(input("What's your bid? $"))
    auction[name] = price
    more_bidders = input("Are there other bidders? Type \"Yes\" or \"No\".").lower()
    print("\n" * 100)

if more_bidders == "no":
    highest_bid = 0
    highest_bidder = ""
    for bid in auction:
        if auction[bid] > highest_bid:
            highest_bid += auction[bid]
            highest_bidder = bid
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
