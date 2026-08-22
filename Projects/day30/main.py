# Importing tools from your newly created custom package
from my_utilities.strings import reverse_string, alternate_caps
from my_utilities.numbers import is_even

print("--- Package-Based Utility System ---")

# Test string utilities
sample_text = "Python Programming"
print(f"Original: {sample_text}")
print(f"Reversed: {reverse_string(sample_text)}")
print(f"Alternated: {alternate_caps(sample_text)}")

# Test number utilities
test_num = 42
print(f"\nIs {test_num} even? {is_even(test_num)}")