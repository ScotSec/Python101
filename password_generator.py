# --- DISCLAIMER ---
# USE AT YOUR OWN RISK!
# ------------------

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
letter_storage = []
number_storage = []
symbol_storage = []
pw_passes = 0

print("Welcome to the PyPassword Generator!")

# Inputs with error handling
while True:
    try:
        nr_letters = int(input("How many letters would you like in your password?\n"))
        break
    except ValueError:
        print("Please input a number.")

while True:
    try:
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        break
    except ValueError:
        print("Please input a number.")

while True:
    try:
        nr_numbers = int(input(f"How many numbers would you like?\n"))
        break
    except ValueError:
        print("Please input a number.")


# Choose letters
for i in range(0, nr_letters):
    letter = random.randint(0, (len(letters) - 1))
    letter_storage.append(letters[letter])

# Choose symbols
for i in range(0, nr_symbols):
    symbol = random.randint(0, (len(symbols) - 1))
    symbol_storage.append(symbols[symbol])

# Choose numbers
for i in range(0, nr_numbers):
    number = random.randint(0, (len(numbers) - 1))
    number_storage.append(numbers[number])

# --- DEBUGGING : Uncomment to check storage contents --
# print(f"Letter Storage : {letter_storage}\nSymbol Storage : {symbol_storage}\nNumber Storage : {number_storage}")

# Combine lists
password_storage = letter_storage + symbol_storage + number_storage
print(f"Chosen characters : {password_storage}")

# Generate random password
print("Generating Password...")
while pw_passes < 1000:
    pw_passes += 1
    random.shuffle(password_storage)

# Convert to string and join list
password_storage= ''.join(map(str, password_storage))
print(f"Password: {password_storage}")
