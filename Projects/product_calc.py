from functools import reduce

# Function to multiply two numbers
def multiply(x, y):
    return x * y

print("--- Product Calculator ---")

# Ask user for a series of numbers
user_input = input("Enter numbers separated by spaces (e.g., 2 3 4): ")

try:
    # Convert input string into a list of floats
    numbers = list(map(float, user_input.split()))
    
    if numbers:
        # reduce() applies multiply() cumulatively across the entire list
        total_product = reduce(multiply, numbers)
        print(f"\nThe numbers you entered: {numbers}")
        print(f"The cumulative product of these numbers is: {total_product}")
    else:
        print("No numbers were entered.")
        
except ValueError:
    print("Please enter valid numbers only.")