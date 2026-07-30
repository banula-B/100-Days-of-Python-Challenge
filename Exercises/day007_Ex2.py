# Age checker using if, elif, else

# Get age from user
age = int(input("Enter your age: "))


if age < 13:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teen")
else:
    print("Adult")