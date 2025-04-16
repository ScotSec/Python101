import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Global Variables
roll_options = [[rock, paper, scissors] , ["Rock", "Paper", "Scissors"]]


# Take user input
user_input = input("What do you choose, ROCK / PAPER / SCISSORS ?\n")
if user_input.lower() == "rock":
    user_choice = roll_options[0][0]
    user_text = roll_options[1][0]
    print(rock)
elif user_input.lower() == "paper":
    user_choice = roll_options[0][1]
    user_text = roll_options[1][1]
    print(paper)
elif user_input.lower() == "scissors":
    user_choice = roll_options[0][2]
    user_text = roll_options[1][2]
    print(scissors)
else:
    print("You did not pick a valid option.\nExiting.")
    exit()

print(f"You chose: {user_text}")


# Calculate and print computer roll
roll_int = random.randint(0 , 2)
computer_choice = roll_options[0][roll_int]
print(computer_choice)
print(f"Computer chose: {roll_options[1][roll_int]}")


# Calculate and print outcome
if computer_choice.lower() == rock and user_choice.lower() == scissors:
    print("You lose!")
elif computer_choice.lower() == paper and user_choice.lower() == rock:
    print("You lose!")
elif computer_choice.lower() == scissors and user_choice.lower() == paper:
    print("You lose!")
elif user_choice.lower() == rock and computer_choice.lower() == scissors:
    print("You win!")
elif user_choice.lower() == paper and computer_choice.lower() == rock:
    print("You win!")
elif user_choice.lower() == scissors and computer_choice.lower() == paper:
    print("You win!")
else:
    print("It's a Draw!")

exit()
