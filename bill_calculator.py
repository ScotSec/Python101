print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? £"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

tip_value = (bill / 100) * tip
total_cost = round(bill + tip_value, 2)
cost_each = round(total_cost / people, 2)
print(f"The total bill is: £{total_cost}")
print(f"The cost per person is: £{cost_each}")
