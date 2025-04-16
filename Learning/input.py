name = input("What is your name? ")
print("Hello " + name)
birth_year = input("What is your birth year? ")

age = 2025 - int(birth_year)

print("You are " + str(age) + " years old!")

if(age > 30):
    print("You must be feeling old!")
