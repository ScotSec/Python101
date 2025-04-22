from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculate():
    print(logo)
    running = True
    first_number = " "

    while running:
        operations = { "+" : add, "-" : subtract, "*" : multiply, "/" : divide,}

        if first_number == " ":
            first_number = float(input("What's the first number?: "))
        else:
            first_number = result

        operation_choice = input("+\n-\n*\n/\nWhat operation do you wish to carry out?: ")
        second_number = float(input("What's the second number?: "))
        result = operations[operation_choice](first_number, second_number)

        print(f"{first_number} {operation_choice} {second_number} = {result}")
        continue_operations_choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if continue_operations_choice.lower() != "y":
            running = False
            calculate()

calculate()