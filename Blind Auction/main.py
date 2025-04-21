from art import logo
print(logo)
print("Welcome to the blind auction application!")

def calculate_highest_bidder():
    highest_bidder_name = ""
    highest_bidder_value = 0
    for name in bids:
        bid_value = bids[name]
        if bid_value > highest_bidder_value:
            highest_bidder_name = name
            highest_bidder_value = bid_value
    print(f"The highest bidder was {highest_bidder_name} with a bid of £{highest_bidder_value}")


run = True
bids = {}
while run == True:
    name = input("What is your name?\n")
    price = input("What is your bid?\n£")
    bids[name] = int(price)
    continue_bidding = input("Are there other users who want to bid? Please enter Y/N.\n")
    if continue_bidding == "N":
        run = False
        calculate_highest_bidder()
    elif continue_bidding == "Y":
        print("\n" * 20)
