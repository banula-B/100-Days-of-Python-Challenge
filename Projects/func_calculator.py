# This is a simple calculator built using functions.

print("Calculator")
print("")
print("1. Addition")
print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")
print("")

choice = int(input("Enter your choice (1-4): "))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

# def mul(num1, num2):
#     return num1 * num2

# def div(num1, num2):
#     return num1 / num2

if choice == 1:
    print("Sum of two numbers is: ", add(num1, num2))
elif choice == 2:
    print("Difference of two numbers is: ", sub(num1, num2))
# elif choice == 3:
#     print("Product of two numbers is: ", mul(num1, num2))
# elif choice == 4:
#     print("Division of two numbers is: ", div(num1, num2))
else:
    print("Invalid choice")

print("")
print("Thank you for using the calculator!")