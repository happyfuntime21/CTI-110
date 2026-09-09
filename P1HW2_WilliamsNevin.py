#Nevin Williams
#9/9/26
#P1HW2
#Travel Price Calculator

print("This program calculates and displays travel expenses")

ub = int(input("\nEnter budget: "))
utd = input("\nEnter your travel destination: ")
usg = int(input("\nHow much do you think you will spend on gas?: "))
usa = int(input("\nApproximately, how much will you need for accomodation/hotel?: "))
usf = int(input("\nLast, how much do you need for food?: "))

print("------------Travel Expenses------------")
print("Location:",utd)
print("Initial Budget:",ub)

print("\nFuel:",usg)
print("Accomodation:",usa)
print("Food:",usf)

print("\nRemaining Balance:",ub-usg-usa-usf)

