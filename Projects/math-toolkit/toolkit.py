import math
import my_math
print("--- Math Toolkit App ---")

n = int(input("Enter an integer: "))

sqrt = math.sqrt(n)
print(f"Standard Math -> Square root of {n} is: {sqrt}")

if my_math.is_prime(n):
    print(f"Custom Math   -> {n} is a prime number!")
else:
    print(f"Custom Math   -> {n} is NOT a prime number.")

fact_val = my_math.factorial(n)
print(f"Custom Math   -> The Factorial of {n} is: {fact_val}")