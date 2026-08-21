import math
import my_math

n = int(input("Enter a number: "))

sqrt = math.sqrt(n)
is_prime = my_math.is_prime(n)
factorial = my_math.factorial(n)

print(f"Square root of {n} is: {sqrt}")
print(f"{n} is a prime number: {is_prime}")
print(f"Factorial of {n} is: {factorial}")
