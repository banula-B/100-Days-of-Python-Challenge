# Temperature checker using if, elif, else

# Get temperature in celsius from user
temperature = int(input("Enter the temperature in Celsius: "))


if temperature > 30:
    print("Hot")
elif temperature >= 20:
    print("Warm")
else:
    print("Cold")