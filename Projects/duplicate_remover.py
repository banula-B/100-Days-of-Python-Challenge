# This is a simple program that removes duplicates from a list.


# Original list with duplicates
fruits = ["apple", "banana", "apple", "orange", "banana", "grape", "apple"]

# Convert original list into a set(to remove duplicates)
unique = set(fruits)

# Convert set into a list
unique_list = list(unique)

print(f"Original List: {fruits}")
print(f"Unique List: {unique_list}")
print(f"Items removed: {len(fruits) - len(unique_list)}")