print("Weclome to the weight convertor!")
print("This program will convert weights in lbs/kg's to the opposite format")

weight = float(input("Please input the weight you wish to have converted: "))
format = str(input("Is this weight kgs or lbs?: "))
lbs = (weight * 2.20462)
kgs = (weight * 0.453592)

if 'kgs' in format:
    print("The weight in lbs is: " + str(lbs))

if 'lbs' in format:
    print("The weight in kgs is: " + str(kgs))

if 'lbs' or 'kgs' not in str(format):
    print("Please re-run the program and select a valid format.")
    exit()
