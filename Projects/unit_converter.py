def km_to_miles(km):
    return km * 0.621371

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print("--- Multi-Unit Converter ---")
print("1. Kilometers to Miles\n2. Celsius to Fahrenheit")
choice = input("Select conversion: ")

if choice == "1":
    kilometers = float(input("Enter kilometers: "))
    miles = km_to_miles(kilometers)
    print(f"{kilometers} km is equal to {miles:.2f} miles.")
elif choice == "2":
    temp_c = float(input("Enter temperature in Celsius: "))
    temp_f = celsius_to_fahrenheit(temp_c)
    print(f"{temp_c}°C is equal to {temp_f:.2f}°F.")
else:
    print("Invalid Selection."