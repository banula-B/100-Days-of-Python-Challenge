# Simple number checker

# Get number from user
number = int(input("Enter a number: "))

# Check number and print category
if number < 10:
    print("Small")
elif number >= 10 and number <= 50:
    print("Medium")
else:
    print("Large")