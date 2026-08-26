# This is a calculator with exception handlings

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

print("====Welcome to Calculator====")

num1 = int(input("Enter first number: "))
operator = input("Enter Operation (+,-,*,/): ")
num2 = int(input("Enter second number: "))

try:
    if operator == "+":
        print(f"{num1} + {num2} = {add(num1,num2)}")
    elif operator == "-":
        print(f"{num1} - {num2} = {sub(num1,num2)}")
    elif operator == "*":
        print(f"{num1} * {num2} = {mul(num1,num2)}")
    elif operator == "/":
        print(f"{num1} / {num2} ={div(num1,num2)}")
    else:
        print("Invalid operator")

except ValueError:
    print("Invalid input. Please enter valid numbers and operator.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Thank you for using calculator")