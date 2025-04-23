import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_continue = True

# Add new user cards based off provided input value
def calculate_user_cards(cards_amount):
    for i in range(0, cards_amount):
        new_card_value = add_card()
        user_cards.append(new_card_value)
    return user_cards

# Add new user cards based off provided input value
def calculate_computer_cards(cards_amount):
    for i in range(0, cards_amount):
        new_card_value = add_card()
        computer_cards.append(new_card_value)
    return computer_cards

# Calculate value of new card
def add_card():
    random_number = random.randint(0,12)
    card = cards[random_number]
    return card

# Checks user win condition and converts ace to 1 if required
def check_user_condition():
    calculate_user_cards(cards_amount=1)
    if sum(user_cards) > 21 and 11 not in user_cards:
        print(f"\nYour cards are {user_cards}\nYour score is {sum(user_cards)}\nThe The computers hand was {computer_cards}\nIts score was {sum(computer_cards)}\nYou lose!")
        exit()
    elif sum(user_cards) > 21 and 11 in user_cards:
        print(f"Your cards are {user_cards} and you went over 21!\n---Converting ace to the value of 1---")
        if 11 in user_cards:
            index = user_cards.index(11)
            user_cards[index] = 1
    elif sum(user_cards) == 21:
        print(f"\nYour cards are {user_cards}\nYour score is {sum(user_cards)}\nThe The computers hand was {computer_cards}\nIts score was {sum(computer_cards)}\nYou win!")
        exit()

def check_computer_condition():
    if sum(computer_cards) > 21 and 11 not in computer_cards:
        print(f"\nYour cards are {user_cards}\nYour score is {sum(user_cards)}\nThe The computers hand was {computer_cards}\nIts score was {sum(computer_cards)}\nYou win!")
        exit()
    elif sum(computer_cards) > 21 and 11 in computer_cards:
        print(f"The computers cards are {computer_cards} and it went over 21!\n---Converting ace to the value of 1---")
        if 11 in computer_cards:
            index = computer_cards.index(11)
            computer_cards[index] = 1
    elif sum(computer_cards) < 17:
        calculate_computer_cards(cards_amount=1)
    elif sum(computer_cards) == 21:
        print(f"\nYour cards are {user_cards}\nYour score is {sum(user_cards)}\nThe The computers hand was {computer_cards}\nIts score was {sum(computer_cards)}\nYou lose!")
        exit()

def check_win_condition():
    global user_continue
    if sum(user_cards) > sum(computer_cards) and sum(user_cards) < 21:
        print(f"\nYour cards are {user_cards}\nYour score is {sum(user_cards)}\nThe The computers hand was {computer_cards}\nIts score was {sum(computer_cards)}\nYou win!")
        exit()
    elif sum(computer_cards) > sum(user_cards) and sum(computer_cards) < 21:
        print(f"\nYour cards are {user_cards}\nYour score is {sum(user_cards)}\nThe The computers hand was {computer_cards}\nIts score was {sum(computer_cards)}\nYou lose!")
        exit()
    elif sum(user_cards) == sum(computer_cards):
        print(f"\nYour cards are {user_cards}\nYour score is {sum(user_cards)}\nThe The computers hand was {computer_cards}\nIts score was {sum(computer_cards)}\nIts a draw!")
        exit()
    elif sum(user_cards) < 21 and sum(computer_cards) > 21:
        print(f"\nYour cards are {user_cards}\nYour score is {sum(user_cards)}\nThe The computers hand was {computer_cards}\nIts score was {sum(computer_cards)}\nYou win!")
        exit()
    elif sum(user_cards) > 21 and sum(computer_cards) > 21 :
        print(f"\nYour cards are {user_cards}\nYour score is {sum(user_cards)}\nThe The computers hand was {computer_cards}\nIts score was {sum(computer_cards)}\nIts a draw!")
        exit()
    elif sum(computer_cards) < 17:
        check_computer_condition()
    user_continue = True



def run_application():
    global user_cards, computer_cards, user_continue, user_add_card
    user_cards = []
    computer_cards = []

    start = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start.lower() == "y":
        print(art.logo)
    else:
        exit()
    calculate_user_cards(cards_amount=2)
    calculate_computer_cards(cards_amount=2)
    print(f"Your cards are: {user_cards}\nYour total value is: {sum(user_cards)}")
    print(f"The computers card is: {computer_cards[0]}")
    user_add_card = ""

    while True:
        global user_continue

        if user_continue == True:
            user_add_card = input(f"Would you like to add another card? 'y' or 'n': ").lower()
        if user_add_card == "y" and user_continue != False:
            check_user_condition()
            print("\n")
            print(f"Your cards are: {user_cards}\nYour total value is: {sum(user_cards)}")
            print(f"The computers card is: {computer_cards[0]}")
        else:
            user_continue = False
            check_computer_condition()
            if sum(computer_cards) >= 17:
                check_win_condition()
            print("\n")
            print(f"Your cards are: {user_cards}\nYour total value is: {sum(user_cards)}")
            print(f"The The computers cards ard {computer_cards}\nIts score is {sum(computer_cards)}")


run_application()